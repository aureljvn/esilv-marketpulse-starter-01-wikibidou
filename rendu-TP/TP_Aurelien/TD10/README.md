# TD10 - Bloomberg Provider - Aurelien Juvin

## Access mode
APPROVED_SAMPLE (no live Bloomberg connectivity demonstrated).
Input: data/sample/bloomberg_reference_sample.json, mapping from docs/BLOOMBERG_FIELD_MAPPING.md (TD09).

## What changed
- New src/providers/bloomberg_provider.py:
  - BLOOMBERG_IDENTIFIERS: AAPL -> AAPL US Equity, SP500 -> SPX Index
  - fetch_raw_bloomberg_history(): raw input boundary (approved sample)
  - normalize_bloomberg_history(): wrapper keys -> canonical rows, canonical ticker preserved
  - fetch_bloomberg_prices(): raw input + normalization
- src/main.py:
  - build_market_snapshot() returns one shared result (provider, access mode, lookback,
    interval, instrument, benchmark, returns, relative performance, base 100)
  - main() only displays the snapshot; the terminal shows "Access mode: APPROVED_SAMPLE"
  - import-safe (if __name__ == "__main__"), ready for the TD11 dashboard
- src/analytics.py was not modified.

## Validation
- Normalized rows match data/sample/bloomberg_reference_expected.json (42/42 rows).
- AAPL +6.48%, SP500 +2.15%, relative performance +4.33 percentage points,
  base 100: AAPL 100.00 -> 106.48, SP500 100.00 -> 102.15.
- Importing src/main.py does not run the terminal program.
