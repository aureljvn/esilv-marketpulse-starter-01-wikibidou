# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- Source: `data/sample/bloomberg_reference_sample.json`
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
- Reference: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md` (not present in our repository)
- Live connectivity: not demonstrated
- The fixture states `"is_live_bloomberg_output": false`: values are illustrative teaching data reused from `data/sample/prices.csv`.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

Provider identifiers for comparison:

| Canonical | Yahoo | Bloomberg |
|---|---|---|
| AAPL | AAPL | AAPL US Equity |
| SP500 | ^GSPC | SPX Index |

## Inspected inputs

| Series | Provider identifier | Canonical ticker | Observations | Date range |
|---|---|---|---|---|
| Instrument | AAPL US Equity | AAPL | 21 | 2026-09-01 to 2026-09-30 |
| Benchmark | SPX Index | SP500 | 21 | 2026-09-01 to 2026-09-30 |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | teaching wrapper key, string `YYYY-MM-DD` |
| ticker | application mapping from `canonical_ticker` | AAPL or SP500, never the Bloomberg identifier |
| open | `open_value` | teaching wrapper key, convert to float |
| high | `high_value` | teaching wrapper key, convert to float |
| low | `low_value` | teaching wrapper key, convert to float |
| close | `close_value` | teaching wrapper key, convert to float |
| volume | `volume_value` | teaching wrapper key, convert to int |

Important: teaching wrapper key != Bloomberg LIVE field mnemonic.
No Bloomberg field mnemonic was observed in this session, so none is documented here.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity -> canonical AAPL
- Benchmark identifier: SPX Index -> canonical SP500
- Date representation: string `YYYY-MM-DD` in `observation_date`
- Input structure: JSON object with metadata and a `series` list; each series has `role`, `canonical_ticker`, `provider_identifier` and an `observations` list
- Missing fields: none in the fixture (all 6 keys present for the 42 observations)
- Special normalization notes: output rows must use the canonical ticker, numeric fields as float, volume as int; the result must match `data/sample/bloomberg_reference_expected.json`
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
