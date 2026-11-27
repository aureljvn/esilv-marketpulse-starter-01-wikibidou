# Checkpoint C - Come Leblois (sawee4)

## Evidence
- 01_final_market_data.png: python src/main.py on the final merged team main,
  Bloomberg stage / APPROVED_SAMPLE, AAPL vs SP500, 1 month, Daily.
- 02_dash_dashboard.png: python src/dashboard.py on the final merged team main:
  provider and access mode, instrument, benchmark, lookback, interval,
  three performance values and the base-100 chart with both series.
- 03_final_pull_request.png: my PR #5 "feat: TD08-TD11 - Yahoo, Bloomberg stage and Dash dashboard"
  (feature/providers-and-dashboard -> main), which contains my TD09, TD10 and TD11 work.
  Reviewed by Aurelien and merged.
- 04_reproducible_run.png: fresh clone of the team repository into a separate folder,
  new virtual environment, python -m pip install -r requirements.txt, then python src/main.py.

## Final provider
Bloomberg stage - APPROVED_SAMPLE. Live Bloomberg connectivity is not demonstrated.
Yahoo Finance remains available with DATA_SOURCE = "yahoo" in src/main.py (internet access required).

## Reproducible run (2026-11-27)
- git clone https://github.com/aureljvn/esilv-marketpulse-starter-01-wikibidou.git marketpulse-repro
- python -m venv .venv
- .venv\Scripts\python -m pip install -r requirements.txt  -> yfinance, dash, plotly installed
- .venv\Scripts\python src/main.py  -> AAPL +6.48 %, SP500 +2.15 %, +4.33 percentage points

## My late-stage contribution
- TD07: src/analytics.py (PR #4, merged).
- TD08: Yahoo provider (src/providers/yahoo_provider.py).
- TD09: docs/BLOOMBERG_FIELD_MAPPING.md.
- TD10: src/providers/bloomberg_provider.py and build_market_snapshot() in src/main.py.
- TD11: src/dashboard.py.
- TD08-TD11 were merged into team main through PR #5; team main uses this implementation.
- Review of Aurelien's PR #6 (tested locally, approved).
- TD12: final validation on merged main and fresh-clone reproducibility test.
  The team final integration PR #9 (path fix, team README) was made by Aurelien and reviewed by Gabin.
