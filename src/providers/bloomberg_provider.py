"""Bloomberg-stage provider for MarketPulse.

Mapping source: docs/BLOOMBERG_FIELD_MAPPING.md (TD09).

Access mode is APPROVED_SAMPLE: raw input comes from the instructor-approved
fallback fixture, not from a live Bloomberg connection. The keys
observation_date / open_value / ... are teaching wrapper keys, not
Bloomberg field mnemonics.
"""

from pathlib import Path
import json

PROVIDER_LABEL = "Bloomberg stage"
ACCESS_MODE = "APPROVED_SAMPLE"

SAMPLE_PATH = Path(__file__).resolve().parents[2] / "data" / "sample" / "bloomberg_reference_sample.json"

# Canonical MarketPulse ticker -> Bloomberg identifier
BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def fetch_raw_bloomberg_history(
    identifier,
    start_date=None,
    end_date=None,
):
    """Raw input boundary.

    In LIVE mode, only the instructor-approved classroom mechanism would go
    here. In APPROVED_SAMPLE mode, the series is read from the fixture.
    start_date / end_date are kept for the LIVE signature; the fixture
    already covers the common 1-month daily window.
    """
    if ACCESS_MODE != "APPROVED_SAMPLE":
        raise NotImplementedError(
            "LIVE Bloomberg access is not available in this environment"
        )

    with open(SAMPLE_PATH, encoding="utf-8") as file:
        fixture = json.load(file)

    for series in fixture["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError(f"No Bloomberg-stage series for {identifier}")


def normalize_bloomberg_history(
    raw_data,
    canonical_ticker,
):
    """Normalization boundary: teaching wrapper keys -> canonical rows."""
    if raw_data["canonical_ticker"] != canonical_ticker:
        raise ValueError(
            f"Series is for {raw_data['canonical_ticker']}, "
            f"not {canonical_ticker}"
        )

    rows = []

    for observation in raw_data["observations"]:
        rows.append({
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })

    if not rows:
        raise ValueError(f"No Bloomberg-stage rows for {canonical_ticker}")

    return rows


def fetch_bloomberg_prices(canonical_ticker):
    identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]
    raw_data = fetch_raw_bloomberg_history(identifier)
    return normalize_bloomberg_history(raw_data, canonical_ticker)
