# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

```text
Source:
data/sample/bloomberg_reference_sample.json

Reference:
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
(not present in this repository at the time of writing;
the mapping below follows the fixture's own schema_note)

Live connectivity:
not demonstrated
```

The fixture declares itself as:

```text
sample_kind              : instructor_approved_fallback_fixture
access_mode              : approved_sample
is_live_bloomberg_output : false
```

Its values are illustrative teaching values reused from `data/sample/prices.csv`.
They are not certified Bloomberg historical observations.

This document must not be presented as proof of LIVE Bloomberg connectivity.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

The provider identifier is not the canonical ticker:

```text
AAPL US Equity  ->  AAPL
SPX Index       ->  SP500
```

Bloomberg identifiers stay at the provider boundary.
`analytics.py` only receives `AAPL` and `SP500`.

## Inspected inputs

### Instrument

```text
role                : instrument
provider_identifier : AAPL US Equity
canonical_ticker    : AAPL
observations        : 21
first date          : 2026-09-01
last date           : 2026-09-30
missing values      : none
```

First observation:

```json
{
  "observation_date": "2026-09-01",
  "open_value": 249.2,
  "high_value": 251.5,
  "low_value": 248,
  "close_value": 250,
  "volume_value": 38000000
}
```

### Benchmark

```text
role                : benchmark
provider_identifier : SPX Index
canonical_ticker    : SP500
observations        : 21
first date          : 2026-09-01
last date           : 2026-09-30
missing values      : none
volume_value        : 0 on all 21 observations
```

First observation:

```json
{
  "observation_date": "2026-09-01",
  "open_value": 6592,
  "high_value": 6615,
  "low_value": 6580,
  "close_value": 6600,
  "volume_value": 0
}
```

## Field mapping

Important:

```text
teaching wrapper key
!=
Bloomberg LIVE field mnemonic
```

The keys below are teaching wrapper keys defined by the fallback fixture.
No Bloomberg LIVE field name is claimed or invented here.

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | Teaching wrapper key. Already `YYYY-MM-DD` string. |
| ticker | application mapping from `canonical_ticker` | `AAPL` or `SP500`. Never the Bloomberg identifier. |
| open | `open_value` | Teaching wrapper key. Convert to `float`. |
| high | `high_value` | Teaching wrapper key. Convert to `float`. |
| low | `low_value` | Teaching wrapper key. Convert to `float`. |
| close | `close_value` | Teaching wrapper key. Convert to `float`. |
| volume | `volume_value` | Teaching wrapper key. Convert to `int`. `0` for SPX Index. |

## Target canonical row

```python
{
    "date": "2026-09-01",
    "ticker": "SP500",
    "open": 6592.0,
    "high": 6615.0,
    "low": 6580.0,
    "close": 6600.0,
    "volume": 0,
}
```

## TD10 handoff

- Access mode: APPROVED_SAMPLE (live connectivity not demonstrated)
- Instrument identifier: `AAPL US Equity` -> canonical `AAPL`
- Benchmark identifier: `SPX Index` -> canonical `SP500`
- Date representation: `observation_date`, string `YYYY-MM-DD`
- Input structure: JSON object with metadata keys and a `series` list; each series has `role`, `canonical_ticker`, `provider_identifier` and an `observations` list
- Missing fields: none in the fixture
- Special normalization notes:
  - select a series by `provider_identifier`, then emit the canonical ticker;
  - some prices are stored as JSON integers (e.g. `248`, `6600`): convert all prices with `float()`;
  - convert volume with `int()`;
  - SPX Index volume is always `0`: an index has no traded volume, keep `0`;
  - keep the canonical row order `date, ticker, open, high, low, close, volume`.
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json` (42 rows: 21 AAPL + 21 SP500)

## Security

No credential, session token or terminal information is included in this document.
