# TD11 - Dash Dashboard - Aurelien Juvin

## What changed
- Installed dash and plotly, recorded in requirements.txt.
- New src/dashboard.py: static Dash page built from build_market_snapshot() (TD10).
- Displays provider (Bloomberg stage - APPROVED_SAMPLE), instrument, benchmark,
  lookback, interval, the three performance values, and one base-100 chart with both series.

## Boundaries
- dashboard.py calls no provider (no Yahoo, no Bloomberg) and contains no formula:
  returns, relative performance and base 100 come from the snapshot.
- Values only get formatted for display.

## Validation
- python src/dashboard.py runs on http://127.0.0.1:8050/
- Instrument return +6.48%, benchmark return +2.15%, relative performance +4.33 pts,
  same values as python src/main.py (same snapshot).
- Both base-100 series start at 100.
