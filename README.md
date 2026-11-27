# MarketPulse - Team wikibidou

ESILV A4 - Python, Git, Linux (MESIFI472326).
Team repository forked from [tawounfouet/esilv-marketpulse](https://github.com/tawounfouet/esilv-marketpulse).

MarketPulse compares one instrument with its benchmark over the same period, from several provider stages, and shows the same result in the terminal and in a Dash dashboard.

## Market

| Role | Ticker | Name |
|---|---|---|
| Instrument | AAPL | Apple Inc. |
| Benchmark | SP500 | S&P 500 |

- Lookback: 1 month
- Interval: Daily
- Results: period return of each series, relative performance (percentage points), base-100 comparison

## Provider

Default: **Bloomberg stage - APPROVED_SAMPLE**.
Data comes from the instructor-approved fixture `data/sample/bloomberg_reference_sample.json`.
Live Bloomberg connectivity is **not** demonstrated.

The source is selected with `DATA_SOURCE` in `src/main.py`:

| DATA_SOURCE | Provider | Requirement |
|---|---|---|
| `bloomberg` (default) | Bloomberg stage, APPROVED_SAMPLE | none |
| `yahoo` | Yahoo Finance via yfinance | internet access |
| `csv` | Local sample files | none |

Identifier mapping: AAPL -> `AAPL US Equity` (Bloomberg) / `AAPL` (Yahoo), SP500 -> `SPX Index` (Bloomberg) / `^GSPC` (Yahoo). See `docs/BLOOMBERG_FIELD_MAPPING.md`.

## Installation

Python 3.10+ is required.

```bash
git clone https://github.com/aureljvn/esilv-marketpulse-starter-01-wikibidou.git
cd esilv-marketpulse-starter-01-wikibidou
python -m pip install -r requirements.txt
```

Direct dependencies: `yfinance`, `dash`, `plotly`.

## Run

Terminal:

```bash
python src/main.py
```

Dashboard (then open http://127.0.0.1:8050 in a browser, Ctrl + C to stop):

```bash
python src/dashboard.py
```

## Architecture

```text
providers/ (yahoo, bloomberg)  ->  canonical rows
analytics.py                   ->  alignment, period return, base 100, relative performance
main.py build_market_snapshot  ->  one shared result
main.py main() / dashboard.py  ->  terminal / Dash presentation
```

`analytics.py` contains no provider identifier. `dashboard.py` calls no provider and contains no formula.

## Environment constraints

- Bloomberg LIVE is not available outside the authorized classroom environment; the default run uses APPROVED_SAMPLE.
- `DATA_SOURCE = "yahoo"` needs internet access; Yahoo values change with the retrieval date.

## Evidence

- `rendu-TP/TP_Aurelien`, `rendu-TP/TP_Come`, `rendu-TP/TP_Gabin`: TD submissions per student
- `evidence/checkpoint-a/`, `evidence/checkpoint-b/`, `evidence/checkpoint-c/`: checkpoint evidence per GitHub username

## Team

| Name | GitHub |
|---|---|
| Côme Leblois | @sawee4 |
| Aurélien Juvin | @aureljvn |
| Gabin Poyet Poullet | @gabinpp3108 |
