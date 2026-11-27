"""Unit tests for MarketPulse, using the data from our TDs."""

import csv
from pathlib import Path

import pytest

from analytics import (
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.bloomberg_provider import fetch_bloomberg_prices

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "sample"


def load_sample_rows(ticker):
    """Read data/sample/prices.csv and keep one ticker, close as a number."""
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return [
            {"date": row["date"], "ticker": row["ticker"], "close": float(row["close"])}
            for row in csv.DictReader(file)
            if row["ticker"] == ticker
        ]


@pytest.fixture
def aapl():
    return load_sample_rows("AAPL")


@pytest.fixture
def sp500():
    return load_sample_rows("SP500")


def test_period_return_of_aapl(aapl):
    # TD07: AAPL closes at 250.00 then 266.20 -> (266.20 / 250 - 1) * 100 = 6.48 %
    assert calculate_period_return(aapl) == pytest.approx(6.48, abs=0.01)


def test_relative_performance_is_aapl_minus_sp500(aapl, sp500):
    # TD07: 6.48 % - 2.15 % = +4.33 percentage points (positive: AAPL beat the index)
    relative = calculate_relative_performance(
        calculate_period_return(aapl),
        calculate_period_return(sp500),
    )
    assert relative == pytest.approx(4.33, abs=0.01)


def test_base_100_starts_at_100(aapl):
    # TD07: base 100 goes from 100.00 to 106.48 for AAPL
    base_100 = calculate_base_100(aapl)
    assert base_100[0]["value"] == pytest.approx(100.0)
    assert base_100[-1]["value"] == pytest.approx(106.48, abs=0.01)


def test_bloomberg_provider_returns_canonical_rows():
    # TD10: the provider must translate "SPX Index" back to our ticker SP500
    rows = fetch_bloomberg_prices("SP500")
    assert len(rows) == 21
    assert all(row["ticker"] == "SP500" for row in rows)
    assert isinstance(rows[0]["close"], float)
    assert set(rows[0]) == {"date", "ticker", "open", "high", "low", "close", "volume"}
