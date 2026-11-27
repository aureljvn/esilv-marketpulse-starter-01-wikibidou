import csv
import json
from pathlib import Path

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.bloomberg_provider import (
    ACCESS_MODE as BLOOMBERG_ACCESS_MODE,
)
from providers.bloomberg_provider import (
    PROVIDER_LABEL as BLOOMBERG_PROVIDER_LABEL,
)
from providers.bloomberg_provider import (
    fetch_bloomberg_prices,
)
from providers.yahoo_provider import (
    PROVIDER_LABEL as YAHOO_PROVIDER_LABEL,
)
from providers.yahoo_provider import (
    YAHOO_SYMBOLS,
    fetch_yahoo_prices,
)

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "sample"

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"
YAHOO_PERIOD = "1mo"
YAHOO_INTERVAL = "1d"

# "bloomberg" = Bloomberg stage (TD10)
# "yahoo"     = remote Yahoo Finance data (TD08)
# "csv"       = local sample files (fallback)
DATA_SOURCE = "bloomberg"
CSV_PROVIDER_LABEL = "Local sample files (data/sample)"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def normalize_price_row(row):
    return {
        "date": row["date"],
        "ticker": row["ticker"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "volume": int(row["volume"]),
    }


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    first_observation = prices[0]
    close = first_observation["close"]
    return float(close)


def get_last_close(prices):
    last_observation = prices[-1]
    close = last_observation["close"]
    return float(close)


def get_first_date(prices):
    first_observation = prices[0]
    return first_observation["date"]


def get_last_date(prices):
    last_observation = prices[-1]
    return last_observation["date"]


def load_csv_series(instrument, benchmark):
    normalized_prices = [normalize_price_row(row) for row in load_prices()]

    instrument_prices = filter_prices(normalized_prices, instrument["ticker"])
    benchmark_prices = filter_prices(normalized_prices, benchmark["ticker"])

    return instrument_prices, benchmark_prices


def load_yahoo_series(instrument, benchmark):
    instrument_prices = fetch_yahoo_prices(
        symbol=YAHOO_SYMBOLS[instrument["ticker"]],
        canonical_ticker=instrument["ticker"],
        period=YAHOO_PERIOD,
        interval=YAHOO_INTERVAL,
    )

    benchmark_prices = fetch_yahoo_prices(
        symbol=YAHOO_SYMBOLS[benchmark["ticker"]],
        canonical_ticker=benchmark["ticker"],
        period=YAHOO_PERIOD,
        interval=YAHOO_INTERVAL,
    )

    return instrument_prices, benchmark_prices


def load_bloomberg_series(instrument, benchmark):
    instrument_prices = fetch_bloomberg_prices(instrument["ticker"])
    benchmark_prices = fetch_bloomberg_prices(benchmark["ticker"])

    return instrument_prices, benchmark_prices


def load_provider_series(data_source, instrument, benchmark):
    """Return (provider label, access mode, instrument rows, benchmark rows)."""
    if data_source == "bloomberg":
        rows = load_bloomberg_series(instrument, benchmark)
        return (BLOOMBERG_PROVIDER_LABEL, BLOOMBERG_ACCESS_MODE) + rows

    if data_source == "yahoo":
        rows = load_yahoo_series(instrument, benchmark)
        return (YAHOO_PROVIDER_LABEL, "REMOTE") + rows

    if data_source == "csv":
        rows = load_csv_series(instrument, benchmark)
        return (CSV_PROVIDER_LABEL, "LOCAL_SAMPLE") + rows

    raise ValueError(f"Unknown data source: {data_source}")


def build_market_snapshot(data_source=DATA_SOURCE):
    """Shared application result for the terminal (TD10) and Dash (TD11)."""
    instruments = load_instruments()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    provider, access_mode, instrument_prices, benchmark_prices = load_provider_series(
        data_source, instrument, benchmark
    )

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    return {
        "provider": provider,
        "access_mode": access_mode,
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_prices": aligned_instrument,
        "benchmark_prices": aligned_benchmark,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": calculate_relative_performance(
            instrument_return,
            benchmark_return,
        ),
        "instrument_base_100": calculate_base_100(aligned_instrument),
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }


def display_market_summary(asset, prices, show_currency=True):
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)
    currency = f" {asset['currency']}" if show_currency else ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Market       : {asset['market']}")
    print(f"Observations : {len(prices)}")
    print(f"First date   : {get_first_date(prices)}")
    print(f"Last date    : {get_last_date(prices)}")
    print(f"First close  : {first_close:.2f}{currency}")
    print(f"Last close   : {last_close:.2f}{currency}")


def display_base_100(ticker, base_100):
    first_value = base_100[0]["value"]
    last_value = base_100[-1]["value"]
    print(f"{ticker:<6}: {first_value:.2f} -> {last_value:.2f}")


def main():
    snapshot = build_market_snapshot()

    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]

    print("=== MarketPulse ===")
    print()
    print("Provider")
    print(snapshot["provider"])
    print()
    print("Access mode")
    print(snapshot["access_mode"])
    print()
    print("Market configuration")
    print(f"Instrument : {instrument['ticker']} - {instrument['name']}")
    print(f"Benchmark  : {benchmark['name']}")
    print(f"Period     : {snapshot['lookback']}")
    print(f"Interval   : {snapshot['interval']}")
    print()
    print("Instrument")
    display_market_summary(
        instrument,
        snapshot["instrument_prices"],
        show_currency=True,
    )
    print(f"Period return : {snapshot['instrument_return']:.2f}%")
    print()
    print("Benchmark")
    display_market_summary(
        benchmark,
        snapshot["benchmark_prices"],
        show_currency=False,
    )
    print(f"Period return : {snapshot['benchmark_return']:.2f}%")
    print()
    print("Relative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']} : "
        f"{snapshot['relative_performance']:+.2f} percentage points"
    )
    print()
    print("Base 100")
    display_base_100(instrument["ticker"], snapshot["instrument_base_100"])
    display_base_100(benchmark["ticker"], snapshot["benchmark_base_100"])


if __name__ == "__main__":
    main()
