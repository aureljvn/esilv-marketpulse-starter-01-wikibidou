# Bloomberg Provider Scaffold

## Purpose

This scaffold supports TD10.

It keeps the provider boundary explicit without inventing a Bloomberg connector.

Use it together with:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
```

The student implementation target remains:

```text
src/providers/bloomberg_provider.py
```

## Shared identifier mapping

```python
BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}
```

These are provider identifiers.

The canonical tickers remain:

```text
AAPL
SP500
```

## APPROVED_SAMPLE scaffold

The repository contains:

```text
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

A simple fallback loader can start with:

```python
import json
from pathlib import Path


REFERENCE_SAMPLE = Path(
    "data/sample/bloomberg_reference_sample.json"
)


def load_bloomberg_reference_sample(
    path=REFERENCE_SAMPLE,
):
    with open(path, encoding="utf-8") as file:
        return json.load(file)
```

Select one approved series:

```python
def find_reference_series(
    payload,
    provider_identifier,
):
    for series in payload["series"]:
        if (
            series["provider_identifier"]
            == provider_identifier
        ):
            return series

    raise ValueError(
        "Approved Bloomberg-stage series not found: "
        f"{provider_identifier}"
    )
```

Normalize that series:

```python
def normalize_reference_series(series):
    canonical_ticker = series["canonical_ticker"]
    rows = []

    for observation in series["observations"]:
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
```

These keys are teaching wrapper keys.

They are not claimed Bloomberg field mnemonics.

## APPROVED_SAMPLE provider path

A small provider function can be:

```python
def fetch_approved_sample_prices(
    provider_identifier,
):
    payload = load_bloomberg_reference_sample()

    series = find_reference_series(
        payload,
        provider_identifier,
    )

    return normalize_reference_series(series)
```

Example:

```python
instrument_prices = fetch_approved_sample_prices(
    "AAPL US Equity"
)

benchmark_prices = fetch_approved_sample_prices(
    "SPX Index"
)
```

The returned rows should use:

```text
AAPL
SP500
```

as canonical tickers.

## Expected-result check

The exact expected canonical result for the fallback fixture is stored in:

```text
data/sample/bloomberg_reference_expected.json
```

The normalized result should match its rows when ordered consistently.

This is a reference comparison, not an automated test-framework requirement.

## LIVE acquisition boundary

LIVE acquisition depends on the instructor-approved classroom environment.

Keep that dependency in one function:

```python
def fetch_raw_bloomberg_history(
    identifier,
    start_date,
    end_date,
):
    # The instructor supplies or demonstrates
    # the environment-specific implementation.
    raise NotImplementedError
```

Students must not replace the function body with a guessed internet package.

## LIVE normalization boundary

Use the actual field names recorded in:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

Conceptual signature:

```python
def normalize_bloomberg_history(
    raw_data,
    canonical_ticker,
):
    ...
```

The result must use:

```text
date
ticker
open
high
low
close
volume
```

If a source field is unavailable, follow the instructor-approved rule documented during TD09.

Do not fabricate provider data.

## Shared analytics contract

Both LIVE and APPROVED_SAMPLE paths must stop at canonical rows.

After that point, reuse:

```python
align_series(...)
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

Do not implement Bloomberg-specific analytics functions.

## Access-mode label

The application output must make the selected mode visible:

```text
LIVE
or
APPROVED_SAMPLE
```

A fallback run must not be labelled as live Bloomberg retrieval.

## Security

Never place Bloomberg credentials in this provider scaffold.

The fallback path requires no Bloomberg credential.
