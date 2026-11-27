# Yahoo Finance Instructor Reference

## Purpose

This document supports TD08 delivery.

It provides:

```text
known-good teaching shape
+
canonical output contract
+
symbol mapping
+
temporary-outage fallback
```

It is not a source of fixed market prices.

Yahoo Finance values vary with retrieval time.

## Teaching scope

TD08 CORE uses:

```text
Instrument canonical ticker : AAPL
Yahoo symbol                : AAPL

Benchmark canonical ticker  : SP500
Yahoo symbol                : ^GSPC

Lookback                    : 1mo
Interval                    : 1d
```

The provider library is:

```text
yfinance
```

Describe it as a community Python package used to access Yahoo Finance data.

Do not present it as the official Yahoo Finance API.

## Known-good retrieval shape

Reference experiment:

```python
import yfinance as yf

history = yf.Ticker("AAPL").history(
    period="1mo",
    interval="1d",
    auto_adjust=False,
)

print(history.head())
print(history.columns)
```

Expected conceptual structure:

```text
date-like index
Open
High
Low
Close
Volume
```

Other provider-added columns may also be present.

Students should inspect the actual returned columns rather than assuming undocumented fields.

## Reference provider function

```python
import yfinance as yf


def fetch_yahoo_prices(
    symbol,
    canonical_ticker,
    period="1mo",
    interval="1d",
):
    history = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
    )

    if history.empty:
        raise ValueError(
            f"No Yahoo Finance data returned for {symbol}"
        )

    rows = []

    for timestamp, row in history.iterrows():
        rows.append({
            "date": timestamp.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })

    return rows
```

The important teaching contract is not the exact syntax.

It is:

```text
Yahoo-specific input
        |
        v
provider adapter
        |
        v
MarketPulse canonical rows
```

## Expected canonical row

A normalized row should have this shape:

```python
{
    "date": "YYYY-MM-DD",
    "ticker": "AAPL",
    "open": 0.0,
    "high": 0.0,
    "low": 0.0,
    "close": 0.0,
    "volume": 0,
}
```

The zeros above are placeholders for type and schema demonstration.

They are not expected market values.

For the benchmark, the provider receives:

```text
^GSPC
```

but the canonical row must contain:

```text
ticker = SP500
```

## Architectural acceptance check

TD08 is correct when this remains true:

```text
CSV provider
      |
      v
canonical rows
      |
      +-------------------+
                          |
Yahoo provider            |
      |                   |
      v                   |
canonical rows            |
      |                   |
      +-------------------+
               |
               v
same TD07 analytics.py
```

No Yahoo-specific identifier should be required inside:

```text
src/analytics.py
```

## Minimum instructor validation

Before class, validate that the chosen environment can perform:

```text
python -m pip install yfinance
```

and that this reference call returns non-empty data:

```python
yf.Ticker("AAPL").history(
    period="1mo",
    interval="1d",
    auto_adjust=False,
)
```

Also check:

```text
AAPL
^GSPC
```

independently.

Do not record fixed prices in the teaching contract.

## Temporary-outage fallback

If Yahoo Finance is unavailable:

```text
1. verify network access
2. verify AAPL and ^GSPC separately
3. verify local provider code against this reference
4. retry once
5. continue architecture work with local CSV
6. keep analytics.py unchanged
7. record that remote evidence is still pending
```

Do not:

```text
fabricate Yahoo output
copy an old screenshot and present it as current
replace remote evidence with CSV without instructor approval
rewrite analytics to hide the provider failure
```

The instructor decides the recovery procedure for Checkpoint B if the external service remains unavailable.

## Common teaching diagnostics

### Empty history

Check:

```text
symbol
internet access
period
interval
```

### Unexpected columns

Use:

```python
print(history.columns)
```

Teach students to inspect actual provider output.

### Different observation counts

This is acceptable.

Use:

```python
align_series(...)
```

from TD07 rather than assuming equal raw list lengths.

### Benchmark identifier confusion

Repeat:

```text
SP500
=
canonical MarketPulse ticker

^GSPC
=
Yahoo-specific symbol
```

## Security

Yahoo Finance retrieval through yfinance does not require students to commit credentials for this lab.

Students must still inspect screenshots and Git changes before publishing evidence.

Never include unrelated secrets from the development environment.


## Cross-scenario recovery reference

For the canonical instructor response when Yahoo failure overlaps with GitHub, environment, Dash or evidence issues, use:

```text
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
```
