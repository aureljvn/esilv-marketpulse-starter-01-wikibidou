
# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

### Source

`data/sample/bloomberg_reference_sample.json`

### Reference

`docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md`

### Live connectivity

Not demonstrated.

The data is an instructor-approved teaching sample.
It is not certified Bloomberg historical market data.

The sample values are illustrative teaching values
reused from the local CSV dataset.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

The following mappings use teaching wrapper keys
from the approved sample.

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | observation_date | Teaching wrapper key |
| ticker | application mapping | AAPL or SP500 |
| open | open_value | Teaching wrapper key |
| high | high_value | Teaching wrapper key |
| low | low_value | Teaching wrapper key |
| close | close_value | Teaching wrapper key |
| volume | volume_value | Teaching wrapper key |

### Important distinction

Teaching wrapper key != Bloomberg LIVE field mnemonic.

These keys describe the structure of the approved teaching
sample. They must not be presented as Bloomberg LIVE
field mnemonics.

## Instrument input

Provider identifier: AAPL US Equity

Canonical ticker: AAPL

Source:
data/sample/bloomberg_reference_sample.json

Date representation:
YYYY-MM-DD (string)

Input structure:
JSON object containing an instrument series
and an observations list.

Available observation keys:
- observation_date
- open_value
- high_value
- low_value
- close_value
- volume_value

Missing fields:
None in the provided instrument observations.

## Benchmark input

Provider identifier: SPX Index

Canonical ticker: SP500

Source:
data/sample/bloomberg_reference_sample.json

Date representation:
YYYY-MM-DD (string)

Input structure:
JSON object containing a benchmark series
and an observations list.

Available observation keys:
- observation_date
- open_value
- high_value
- low_value
- close_value
- volume_value

Missing fields:
None in the provided benchmark observations.

Note:
The sample contains volume_value with a value of 0
for the benchmark. This is a provided value, not
a missing field.

## Canonical MarketPulse model

The expected canonical row structure is:

- date: str
- ticker: str
- open: float
- high: float
- low: float
- close: float
- volume: int

Expected canonical tickers:
- AAPL
- SP500

Provider identifiers must remain at the provider boundary.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity
- Benchmark identifier: SPX Index
- Date representation: YYYY-MM-DD
- Input structure: JSON series with observations lists
- Missing fields: None in the provided sample
- Special normalization notes:
  - observation_date maps to date
  - open_value maps to open
  - high_value maps to high
  - low_value maps to low
  - close_value maps to close
  - volume_value maps to volume
  - AAPL US Equity maps to canonical ticker AAPL
  - SPX Index maps to canonical ticker SP500
  - Teaching wrapper keys are not Bloomberg LIVE field mnemonics

Expected canonical reference:

`data/sample/bloomberg_reference_expected.json`

Live connectivity:
Not demonstrated.
