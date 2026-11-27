# Bloomberg Instructor Reference and Fallback Assets

## Purpose

This document supports TD09 and TD10 delivery when Bloomberg access is available, partially available or unavailable.

It defines four teaching assets:

```text
1. known-good instructor fallback fixture
2. reference mapping for the fallback fixture
3. expected canonical normalized result
4. explicit live vs approved-sample distinction
```

The fallback assets are not evidence of live Bloomberg connectivity.

They exist so students can continue provider-boundary and normalization work without fabricating Bloomberg access.

## Canonical MarketPulse identifiers

The common CORE pair remains:

```text
Instrument canonical ticker : AAPL
Benchmark canonical ticker  : SP500
```

Bloomberg identifiers used by the teaching sequence are:

```text
AAPL  -> AAPL US Equity
SP500 -> SPX Index
```

These provider identifiers must stay outside provider-neutral analytics.

## Teaching modes

The Bloomberg stage has two authorized modes.

### LIVE mode

Use when the instructor-approved Bloomberg environment successfully returns data.

Required documentation:

```text
mode = live
access method = actual classroom mechanism
observed fields = actual returned field names
identifiers = actual identifiers used
```

LIVE mode can support evidence of Bloomberg connectivity when the teaching environment permits it.

### APPROVED_SAMPLE mode

Use when the instructor-approved Bloomberg environment is unavailable or unsuitable for the scheduled lab.

Fallback files:

```text
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

Required documentation:

```text
mode = approved_sample
live connectivity = not demonstrated
sample provenance = instructor fallback fixture
```

APPROVED_SAMPLE mode supports:

- identifier mapping;
- provider-boundary reasoning;
- normalization implementation;
- canonical-row validation;
- alignment and analytics reuse.

It does not prove:

- a live Bloomberg session;
- a successful Bloomberg network request;
- workstation authorization;
- Bloomberg credentials or entitlements.

## Important provenance note

The fallback numeric values are illustrative teaching values reused from the MarketPulse starter dataset.

They are not certified Bloomberg historical observations.

The fallback file intentionally uses instructor wrapper keys such as:

```text
observation_date
open_value
high_value
low_value
close_value
volume_value
```

These are not claimed to be Bloomberg field mnemonics.

This distinction prevents the course material from inventing unverified Bloomberg field names.

## Reference fallback input

File:

```text
data/sample/bloomberg_reference_sample.json
```

Conceptual structure:

```text
approved sample metadata
        |
        v
AAPL US Equity
        |
        v
teaching-wrapper observations

SPX Index
        |
        v
teaching-wrapper observations
```

The fixture contains 21 aligned daily observations for each series, covering the full September 2026 teaching window used by the starter.

## Reference mapping for APPROVED_SAMPLE mode

The fallback wrapper mapping is fully defined:

| Teaching wrapper key | MarketPulse canonical field | Type |
|---|---|---|
| `observation_date` | `date` | string |
| application mapping | `ticker` | string |
| `open_value` | `open` | float |
| `high_value` | `high` | float |
| `low_value` | `low` | float |
| `close_value` | `close` | float |
| `volume_value` | `volume` | int |

Canonical ticker mapping:

```text
AAPL US Equity -> AAPL
SPX Index      -> SP500
```

## LIVE field mapping rule

Do not copy the fallback wrapper keys into the LIVE mapping and call them Bloomberg fields.

For LIVE mode, students must document what the actual approved environment returns.

Use this table during TD09:

| MarketPulse field | Observed LIVE Bloomberg field | Status |
|---|---|---|
| date | <record actual field or index> | confirm in class |
| ticker | application mapping | fixed |
| open | <record actual field> | confirm in class |
| high | <record actual field> | confirm in class |
| low | <record actual field> | confirm in class |
| close | <record actual field> | confirm in class |
| volume | <record actual field or approved rule> | confirm in class |

If a field is unavailable, record that fact.

Do not invent a mnemonic to make the table look complete.

## Expected canonical normalized result

File:

```text
data/sample/bloomberg_reference_expected.json
```

The expected result uses the same canonical row contract as CSV and Yahoo:

```python
{
    "date": "YYYY-MM-DD",
    "ticker": "AAPL",
    "open": 0.0,
    "high": 0.0,
    "low": 0.0,
    "close": 0.0,
    "volume": 0,
}
```

The concrete expected file provides exact values for the fallback fixture.

A correct normalization of the fallback input should match that file row for row.

## Suggested fallback normalization boundary

A teaching implementation may separate:

```text
load approved sample
        |
        v
read provider identifier
        |
        v
map wrapper keys
        |
        v
assign canonical ticker
        |
        v
canonical rows
```

Conceptual signatures:

```python
def load_bloomberg_reference_sample(path):
    ...


def normalize_bloomberg_reference_series(
    series,
):
    ...
```

The exact production Bloomberg acquisition mechanism is intentionally not defined here because it depends on the actual classroom environment.

## Validation checklist

Before class, the instructor should verify the fallback files:

```text
[ ] both JSON files parse
[ ] AAPL US Equity is present
[ ] SPX Index is present
[ ] canonical AAPL is present
[ ] canonical SP500 is present
[ ] both series contain 21 rows
[ ] dates are aligned
[ ] expected rows use canonical keys
[ ] no credential exists in either file
```

During APPROVED_SAMPLE mode, students should verify:

```text
[ ] mode is documented as approved_sample
[ ] no claim of live Bloomberg retrieval is made
[ ] provider identifiers are translated to canonical tickers
[ ] wrapper keys are translated to canonical fields
[ ] analytics.py remains unchanged
[ ] normalized output matches the expected reference
```

## TD09 use

TD09 should use these assets only when LIVE mode cannot be completed.

The student mapping document should state either:

```text
Access mode: LIVE
```

or:

```text
Access mode: APPROVED_SAMPLE
```

If APPROVED_SAMPLE is used, the mapping document must distinguish:

```text
teaching wrapper key
!=
Bloomberg LIVE field mnemonic
```

## TD10 use

TD10 may use the fallback fixture to prove:

```text
Bloomberg-stage provider boundary
+
identifier translation
+
normalization
+
canonical rows
+
shared analytics reuse
```

It may not be presented as proof of:

```text
live Bloomberg connectivity
```

The final provider mode must remain visible in output or documentation.

## Security

Never place in these assets:

- Bloomberg username;
- password;
- session token;
- API secret;
- workstation credential;
- copied private configuration;
- screenshot containing sensitive information.

No credential is required for the fallback fixture.

## Instructor decision record

Before TD09 starts, record one line in the teaching notes:

```text
Bloomberg mode for this session:
LIVE
or
APPROVED_SAMPLE
```

If the mode changes during class because of an outage, document the change honestly.

## Final principle

```text
No live access
!=
no learning

Approved sample
+
honest mode label
+
known expected result
=
valid normalization exercise
```

But:

```text
approved sample
!=
live Bloomberg evidence
```


## Cross-scenario recovery reference

For the canonical instructor response when Bloomberg availability overlaps with environment, Git, Dash or evidence issues, use:

```text
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
```
