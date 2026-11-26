"""Bloomberg-stage provider for MarketPulse.

Access mode: APPROVED_SAMPLE.
Raw input comes from the instructor-approved fixture
data/sample/bloomberg_reference_sample.json (see docs/BLOOMBERG_FIELD_MAPPING.md).
This does not prove live Bloomberg connectivity.
"""

from pathlib import Path
import json

ACCESS_MODE = "APPROVED_SAMPLE"

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}

SAMPLE_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "sample"
    / "bloomberg_reference_sample.json"
)


def fetch_raw_bloomberg_history(identifier):
    with open(SAMPLE_PATH, encoding="utf-8") as file:
        sample = json.load(file)

    for series in sample["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError(f"No Bloomberg-stage data for {identifier}")


def normalize_bloomberg_history(raw_series, canonical_ticker):
    rows = []

    for observation in raw_series["observations"]:
        rows.append({
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })

    return rows


def fetch_bloomberg_prices(canonical_ticker):
    identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]
    raw_series = fetch_raw_bloomberg_history(identifier)
    return normalize_bloomberg_history(raw_series, canonical_ticker)
