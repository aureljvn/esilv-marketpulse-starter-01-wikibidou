# Checkpoint B - Come Leblois (sawee4)

Branch: feature/providers-and-dashboard (PR #5, TD08-TD11 in one PR as agreed with the instructor)

## Evidence
- 01_pull_request.png: my PR #5 "feat: TD08-TD11 - Yahoo, Bloomberg stage and Dash dashboard"
  (feature/providers-and-dashboard -> main), 4 commits, one per TD.
- 02_code_review.png: my review of Aurelien's PR #6 "feat: add TD07-TD11 work and Aurelien rendu".
  I checked out his branch and ran it locally: python src/main.py works (+4.33 percentage points),
  build_market_snapshot() returns the full contract, dashboard.py has no provider call or formula,
  analytics.py has no provider identifier.
- 03_yahoo_market_data.png: python src/main.py with "Provider : Yahoo Finance via yfinance",
  successful remote retrieval (period 1 month, interval Daily).
- 04_instrument_benchmark.png: same run, AAPL vs SP500 comparison
  (03 and 04 are the same screenshot: one run shows both the Yahoo retrieval and the comparison).

## Yahoo result (run on 2026-11-26, values depend on retrieval time)
- 23 aligned observations, 2026-10-26 to 2026-11-25
- AAPL period return: +3.39%
- SP500 period return: -6.43%
- Relative performance: +9.83 percentage points
- Base 100: AAPL 100.00 -> 103.39, SP500 100.00 -> 93.57

## My commits
- ada2fbb feat: add reusable market comparison analytics (TD07, PR #4, merged)
- 9e1dd5e feat: add Yahoo Finance provider (TD08)
- 842e331 docs: map Bloomberg stage to MarketPulse (TD09)
- 97bc537 feat: add Bloomberg provider boundary (TD10)
- 4c2fcc6 feat: add MarketPulse Dash dashboard (TD11)

## Notes
- Yahoo symbol ^GSPC stays in src/providers/yahoo_provider.py; the canonical ticker remains SP500.
- src/analytics.py was not modified after TD07.
- No secret appears in the screenshots.
