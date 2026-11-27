# MarketPulse Application Snapshot Contract

## 1. Purpose

MarketPulse has two CORE presentation paths:

```text
terminal
+
Dash
```

Both must display the same application result.

The project must not evolve into:

```text
terminal
=
one provider call
+
one set of calculations

dashboard
=
another provider call
+
another set of calculations
```

The shared boundary is:

```python
build_market_snapshot(...)
```

This function produces one reusable application-level result.

## 2. Architectural position

The CORE flow is:

```text
provider-specific input
        |
        v
canonical rows
        |
        v
shared analytics
        |
        v
build_market_snapshot()
        |
        +-------------------+
        |                   |
        v                   v
terminal presentation   Dash presentation
```

The snapshot sits after acquisition, normalization, alignment and analytics.

It sits before presentation.

## 3. CORE file location

The 18-hour CORE keeps the frozen flat Python structure:

```text
src/
├── main.py
├── analytics.py
├── dashboard.py
└── providers/
    ├── __init__.py
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

No new application package is required.

For the CORE, `build_market_snapshot(...)` lives in:

```text
src/main.py
```

This is deliberate.

The course avoids adding another module solely for architectural purity.

A later professional refactor may move application orchestration into a dedicated module.

## 4. Import-safety rule

Because `src/dashboard.py` may import `build_market_snapshot` from `src/main.py`, importing `main.py` must not immediately execute the terminal program.

Keep:

```python
if __name__ == "__main__":
    main()
```

The intended pattern is:

```python
def build_market_snapshot(...):
    ...


def main():
    snapshot = build_market_snapshot(...)
    ...


if __name__ == "__main__":
    main()
```

This allows:

```python
from main import build_market_snapshot
```

inside `src/dashboard.py` without triggering terminal output as an import side effect.

## 5. Required snapshot shape

The CORE snapshot contains exactly the information both presentation paths need:

```python
{
    "provider": "...",
    "lookback": "...",
    "interval": "...",
    "instrument": {
        "ticker": "...",
        "name": "...",
    },
    "benchmark": {
        "ticker": "...",
        "name": "...",
    },
    "instrument_return": ...,
    "benchmark_return": ...,
    "relative_performance": ...,
    "instrument_base_100": [...],
    "benchmark_base_100": [...],
}
```

The function may internally use the team's currently authorized provider path.

A generic provider-selection framework is not required.

## 6. Field contract

### provider

Human-readable provider context.

Examples:

```text
CSV
Yahoo Finance via yfinance
Bloomberg - LIVE
Bloomberg stage - APPROVED_SAMPLE
```

The string must describe the actual execution honestly.

In particular:

```text
APPROVED_SAMPLE
!=
LIVE Bloomberg
```

### lookback

CORE value:

```text
1 month
```

A team may internally represent the provider request as `1mo`, but the snapshot should remain presentation-friendly.

### interval

CORE value:

```text
Daily
```

### instrument

Required shape:

```python
{
    "ticker": "AAPL",
    "name": "Apple Inc.",
}
```

### benchmark

Required shape:

```python
{
    "ticker": "SP500",
    "name": "S&P 500",
}
```

Provider-specific identifiers do not replace these canonical tickers.

### instrument_return

Numeric period return expressed as a percentage value.

Example interpretation:

```text
6.48
=
+6.48%
```

Do not store the formatted string `"+6.48%"` as the analytical value.

Formatting belongs to presentation.

### benchmark_return

Same contract as `instrument_return`.

### relative_performance

Numeric difference:

```text
instrument_return
-
benchmark_return
```

The presentation unit is percentage points.

### instrument_base_100

List of rows:

```python
[
    {
        "date": "YYYY-MM-DD",
        "ticker": "AAPL",
        "value": 100.0,
    },
    ...
]
```

### benchmark_base_100

Same structure with canonical benchmark ticker:

```text
SP500
```

The first aligned value of each series must be 100.

## 7. Snapshot invariants

A valid CORE snapshot satisfies:

```text
[ ] provider is honest
[ ] lookback = 1 month
[ ] interval = Daily
[ ] instrument ticker is canonical
[ ] benchmark ticker is canonical
[ ] returns are numeric
[ ] relative performance = instrument - benchmark
[ ] instrument base 100 is not empty
[ ] benchmark base 100 is not empty
[ ] both base-100 series use aligned dates
[ ] both base-100 series start at 100
```

## 8. Provider boundary rule

`build_market_snapshot(...)` may orchestrate an authorized provider path.

It may call provider functions indirectly or directly from the application orchestration layer.

However:

```text
src/dashboard.py
```

must not call:

```text
fetch_yahoo_prices(...)
fetch_bloomberg_prices(...)
fetch_raw_bloomberg_history(...)
```

or equivalent provider-specific functions.

The dashboard consumes the snapshot.

The dashboard does not own acquisition.

## 9. Analytics rule

The snapshot builder reuses:

```text
align_series()
calculate_period_return()
calculate_base_100()
calculate_relative_performance()
```

It must not duplicate these formulas.

Avoid:

```python
def build_market_snapshot(...):
    # duplicate period return formula here
    ...
```

Instead:

```text
provider rows
      |
      v
analytics.py
      |
      v
snapshot
```

## 10. Terminal contract

The terminal path becomes conceptually:

```python
def main():
    snapshot = build_market_snapshot()
    print_market_snapshot(snapshot)
```

The exact print helper name is not mandatory.

The important rule is:

```text
terminal
consumes snapshot
```

The terminal must not independently recompute a second set of returns.

## 11. Dashboard contract

TD11 uses:

```python
from main import build_market_snapshot


snapshot = build_market_snapshot()
```

The Dash layout reads:

```text
snapshot["provider"]
snapshot["instrument"]
snapshot["benchmark"]
snapshot["lookback"]
snapshot["interval"]
snapshot["instrument_return"]
snapshot["benchmark_return"]
snapshot["relative_performance"]
snapshot["instrument_base_100"]
snapshot["benchmark_base_100"]
```

The dashboard may format those values.

It must not recalculate them.

## 12. Presentation formatting

Keep raw business values and display formatting separate.

Good:

```python
instrument_return = snapshot["instrument_return"]

display_value = f"{instrument_return:+.2f}%"
```

Avoid:

```python
snapshot["instrument_return"] = "+6.48%"
```

The snapshot is application data.

The presentation layer decides how the value looks.

## 13. Minimal reference implementation shape

This is a structural example, not provider-specific code:

```python
def build_market_snapshot():
    instrument = ...
    benchmark = ...

    instrument_prices = ...
    benchmark_prices = ...

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    instrument_return = calculate_period_return(
        aligned_instrument
    )

    benchmark_return = calculate_period_return(
        aligned_benchmark
    )

    relative_performance = (
        calculate_relative_performance(
            instrument_return,
            benchmark_return,
        )
    )

    instrument_base_100 = calculate_base_100(
        aligned_instrument
    )

    benchmark_base_100 = calculate_base_100(
        aligned_benchmark
    )

    return {
        "provider": ...,
        "lookback": "1 month",
        "interval": "Daily",
        "instrument": {
            "ticker": instrument["ticker"],
            "name": instrument["name"],
        },
        "benchmark": {
            "ticker": benchmark["ticker"],
            "name": benchmark["name"],
        },
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": relative_performance,
        "instrument_base_100": instrument_base_100,
        "benchmark_base_100": benchmark_base_100,
    }
```

## 14. CORE validation

Before TD11 presentation work is considered correctly wired, verify:

```text
[ ] build_market_snapshot() returns one dictionary
[ ] all required keys are present
[ ] main() consumes the snapshot
[ ] dashboard.py consumes the snapshot
[ ] terminal and dashboard values match for the same run
[ ] dashboard.py contains no provider-specific request
[ ] dashboard.py contains no return formula
[ ] analytics.py remains the calculation source
[ ] provider label reflects LIVE vs APPROVED_SAMPLE honestly
```

## 15. Non-goals

The CORE snapshot contract does not require:

```text
dataclasses
Pydantic
typed dictionaries
service classes
dependency injection
plugin registry
generic provider factory
serialization framework
API layer
automated test framework
```

Those may be explored later as professional extensions.

## 16. Final principle

```text
Acquire once
normalize once
calculate once
present many times
```

For MarketPulse:

```text
providers
   |
   v
analytics
   |
   v
snapshot
   |
   +----------+
   |          |
   v          v
terminal     Dash
```
