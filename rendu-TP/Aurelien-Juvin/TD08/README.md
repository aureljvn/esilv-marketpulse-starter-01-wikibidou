# TD08 - Yahoo Finance - Aurelien Juvin

## What changed
- Installed `yfinance` and recorded it in `requirements.txt`.
- New provider `src/providers/yahoo_provider.py` with `fetch_yahoo_prices()`:
  retrieves 1 month of daily prices and returns canonical MarketPulse rows
  (date, ticker, open, high, low, close, volume).
- Symbol mapping: AAPL -> AAPL, SP500 -> ^GSPC. The Yahoo symbol `^GSPC`
  is only used in the provider; the canonical ticker stays SP500.
- `src/main.py` now fetches instrument and benchmark from Yahoo, then reuses
  the TD07 functions (`align_series`, period return, base 100, relative performance).
- `src/analytics.py` was not modified.

## Result (run on 2026-11-26, values depend on retrieval time)
- 23 aligned observations, 2026-10-26 to 2026-11-25
- AAPL period return: +3.39%
- SP500 period return: -6.43%
- Relative performance: +9.83 percentage points
- Base 100: AAPL 100.00 -> 103.39, SP500 100.00 -> 93.57

## Key concepts
- yfinance is a community library, not the official Yahoo Finance API.
- Canonical ticker (SP500) vs provider symbol (^GSPC).
- The provider normalizes Yahoo data into the same row format as the CSV,
  so the analytics layer works unchanged.

## Checkpoint B notes
- 01_pull_request.png: my PR #2 "feat: display data provider label" (feature/display-provider-label -> main), reviewed by Come (sawee4), merged.
- 02_code_review.png: my review of Come's PR #1 "feat: display market metadata".
- Both reviews were submitted with the "Request changes" status by mistake, while their content was an approval
  (no blocking issue found). I confirmed my approval in a follow-up "approved" comment.
- The team worked in pairs for TD05-TD06: Gabin did not open a PR, so the review rotation was Aurelien <-> Come.
