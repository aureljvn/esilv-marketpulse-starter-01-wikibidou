# MarketPulse Libraries and Dependencies

## 1. Purpose

This document defines the Python libraries and external technology dependencies used across the 12 MarketPulse labs.

It distinguishes:

```text
Python standard library
+
direct external dependencies
+
transitive dependencies
+
environment-specific dependencies
+
optional or excluded dependencies
```

The objective is to keep the 18-hour CORE dependency model:

```text
small
+
progressive
+
explainable
+
reproducible
```

This document complements:

```text
requirements.txt
```

`requirements.txt` answers:

```text
What must pip install?
```

This document answers:

```text
Why is this dependency present?
When is it introduced?
Is it CORE?
Is it direct, transitive or environment-specific?
```

## 2. Dependency philosophy

MarketPulse does not introduce a library only because it is common in data engineering or finance.

A dependency is added when a lab creates a concrete need for it.

The progression is:

```text
TD01-TD07
Python Standard Library
        |
        v
TD08
+ yfinance
        |
        +-> pandas transitively
        |
        v
TD09-TD10
Bloomberg LIVE environment
or
stdlib APPROVED_SAMPLE fallback
        |
        v
TD11
+ dash
+ plotly
        |
        v
TD12
dependency verification
+
reproducibility
```

The CORE avoids unnecessary dependency growth.

## 3. Dependency decision table

| Library / technology | Category | First TD | pip required | CORE | Purpose |
|---|---|---:|---:|---:|---|
| Python | Runtime | TD01 | No | Yes | Execute MarketPulse |
| `pathlib` | Python standard library | TD01-TD02 | No | Yes | File and directory paths |
| `csv` | Python standard library | TD02 | No | Yes | Read local market CSV data |
| `json` | Python standard library | TD02 | No | Yes | Read metadata and fallback JSON data |
| Git | Tool | TD01 | No | Yes | Version control |
| GitHub | Platform | TD01 | No | Yes | Shared repository, Pull Requests and review |
| Linux | Environment | TD01 | No | Yes | Terminal and execution environment |
| Bash / shell | Tool | TD01 | No | Yes | Command-line workflow |
| `yfinance` | Direct external dependency | TD08 | Yes | Yes | Yahoo Finance market-data access |
| Yahoo Finance | External data provider | TD08 | No Python install | Yes | Remote market-data source |
| `pandas` | Transitive dependency | TD08 | Installed indirectly | No direct teaching requirement | Table-like structures returned by yfinance |
| Bloomberg | External professional provider | TD09 | Environment dependent | Conditional | Professional market-data stage |
| Bloomberg Python connector | Environment-specific dependency | TD09-TD10 | Depends | Conditional | LIVE Bloomberg access only if validated by ESILV |
| `dash` | Direct external dependency | TD11 | Yes | Yes | Web dashboard |
| `plotly` | Direct external dependency | TD11 | Yes | Yes | Base-100 comparison chart |
| `PyYAML` | Optional / excluded from CORE | None | No | No | YAML parsing is not required |
| `numpy` | Excluded from CORE | None | No | No | Not needed for required calculations |
| `requests` | Excluded from CORE | None | No | No | No direct HTTP layer is required |
| `pytest` | Excluded from CORE | None | No | No | Automated test framework is outside the 18-hour CORE |

## 4. Python standard library

The first part of the sequence intentionally uses only Python's standard library.

### 4.1 pathlib

Imported as:

```python
from pathlib import Path
```

Used for:

```text
repository-relative paths
data/sample paths
JSON fallback paths
```

Why it is useful pedagogically:

```text
portable path handling
+
clearer code than manual path concatenation
```

No installation is required.

### 4.2 csv

Imported as:

```python
import csv
```

Introduced in TD02.

Primary use:

```python
csv.DictReader(...)
```

MarketPulse uses it to load:

```text
data/sample/prices.csv
```

No installation is required.

### 4.3 json

Imported as:

```python
import json
```

Introduced in TD02.

Used to load:

```text
data/sample/instruments.json
```

It is reused by the Bloomberg APPROVED_SAMPLE scaffold for:

```text
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

No installation is required.

## 5. yfinance

### Status

```text
DIRECT EXTERNAL DEPENDENCY
CORE
```

Introduced in:

```text
TD08 - Yahoo Finance
```

Installation:

```bash
python -m pip install yfinance
```

It must then be recorded in:

```text
requirements.txt
```

Typical import:

```python
import yfinance as yf
```

MarketPulse uses it to retrieve:

```text
AAPL
^GSPC
```

where:

```text
AAPL
=
canonical instrument ticker
+
Yahoo symbol

SP500
=
canonical benchmark ticker

^GSPC
=
Yahoo-specific benchmark symbol
```

Important:

```text
yfinance
!=
official Yahoo Finance API
```

It is a community Python package used for the teaching provider stage.

## 6. pandas

### Status

```text
TRANSITIVE DEPENDENCY
NOT A DIRECT CORE TEACHING DEPENDENCY
```

`yfinance` returns table-like objects backed by pandas.

Students may therefore encounter concepts such as:

```text
DataFrame
columns
index
iterrows()
```

However:

```text
TD08 is not a pandas course.
```

The CORE does not require a separate pandas learning objective.

Do not add `pandas` manually to `requirements.txt` unless student code imports it directly.

The dependency rule is:

```text
installed transitively by yfinance
!=
direct MarketPulse dependency
```

## 7. Bloomberg

### Status

```text
PROFESSIONAL DATA PROVIDER
ENVIRONMENT-SPECIFIC PYTHON DEPENDENCY
```

Introduced in:

```text
TD09 - Bloomberg Introduction
TD10 - Bloomberg Provider
```

Bloomberg is part of the provider progression, but the repository intentionally does not freeze a guessed Bloomberg Python package.

The authorized modes are:

```text
LIVE
or
APPROVED_SAMPLE
```

### 7.1 LIVE mode

If the ESILV environment provides a validated Python access mechanism, the instructor documents the exact connector used.

Only then may a Bloomberg-specific Python dependency be added.

Rule:

```text
validated classroom connector
=
allowed dependency

guessed internet package
=
not allowed
```

### 7.2 APPROVED_SAMPLE mode

No Bloomberg-specific Python package is needed.

The fallback path uses:

```text
json
+
pathlib
```

with:

```text
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

Reference:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md
```

Important:

```text
APPROVED_SAMPLE
!=
LIVE Bloomberg evidence
```

## 8. Dash

### Status

```text
DIRECT EXTERNAL DEPENDENCY
CORE
```

Introduced in:

```text
TD11 - Dash Dashboard
```

Installation:

```bash
python -m pip install dash
```

Required entry in:

```text
requirements.txt
```

Typical import:

```python
from dash import Dash, dcc, html
```

Role:

```text
presentation layer
```

Dash does not own:

```text
provider acquisition
normalization
alignment
period return
base 100
relative performance
```

It consumes:

```python
build_market_snapshot(...)
```

## 9. Plotly

### Status

```text
DIRECT EXTERNAL DEPENDENCY
CORE
```

Introduced in:

```text
TD11 - Dash Dashboard
```

Installation:

```bash
python -m pip install plotly
```

Required entry in:

```text
requirements.txt
```

Typical import:

```python
import plotly.graph_objects as go
```

CORE use:

```text
Instrument vs Benchmark
Base-100 comparison chart
```

Plotly formats and renders already-calculated values.

It does not calculate MarketPulse business metrics.

## 10. Dependency introduction by lab

### TD01 - Bootstrap + Linux

Python dependencies:

```text
none outside the standard library
```

Tools:

```text
Python
Git
GitHub
Linux
Bash / shell
```

### TD02 - Python + CSV / JSON

New Python modules:

```text
pathlib
csv
json
```

All are standard library modules.

### TD03 - Git Local Workflow

New Python dependency:

```text
none
```

### TD04 - Branches + Merge

New Python dependency:

```text
none
```

### TD05 - Remote Branch + Pull Request

New Python dependency:

```text
none
```

### TD06 - Code Review

New Python dependency:

```text
none
```

### TD07 - Data Normalization + Comparison

New Python dependency:

```text
none
```

The analytical functions are intentionally implemented with plain Python.

### TD08 - Yahoo Finance

New direct dependency:

```text
yfinance
```

Transitive dependency encountered:

```text
pandas
```

### TD09 - Bloomberg Introduction

Fixed new Python dependency:

```text
none
```

Bloomberg access mechanism:

```text
environment-specific
```

### TD10 - Bloomberg Provider

Fixed new Python dependency:

```text
none
```

APPROVED_SAMPLE uses:

```text
json
pathlib
```

LIVE mode may add one instructor-validated Bloomberg connector.

### TD11 - Dash Dashboard

New direct dependencies:

```text
dash
plotly
```

### TD12 - Integration + Release

New dependency:

```text
none
```

TD12 verifies:

```text
requirements.txt
+
fresh installation
+
runtime reproducibility
```

## 11. CORE requirements.txt evolution

### TD01-TD07

The starter may remain:

```text
# no external dependency required
```

### TD08 onward

Add:

```text
yfinance
```

### TD11 onward

The normal external CORE set becomes:

```text
yfinance
dash
plotly
```

This is the expected generic final dependency shape when Yahoo support remains in the student implementation.

If the LIVE Bloomberg implementation imports an instructor-approved connector, add that dependency only when the actual environment requires it.

## 12. Why some common libraries are excluded

### PyYAML

The repository contains:

```text
config/settings.yml
```

but this file is a human-readable configuration contract in the CORE.

Parsing YAML is not required.

Therefore:

```text
PyYAML
=
optional extension
```

### numpy

The required calculations are simple enough to implement with plain Python.

The CORE does not need NumPy for:

```text
period return
date alignment
base 100
relative performance
```

### requests

Yahoo access is delegated to `yfinance`.

Bloomberg access is environment-specific.

The CORE therefore does not require a custom HTTP client.

### pytest

The 18-hour CORE does not include an automated testing framework.

Validation is performed through:

```text
execution
+
Git review
+
checkpoint evidence
+
student explanation
```

A testing framework may be introduced later as a professional extension.

## 13. Standard library vs external dependency

A useful rule for students is:

```text
import csv
import json
from pathlib import Path
```

does not imply:

```bash
pip install csv
pip install json
pip install pathlib
```

They are part of Python.

In contrast:

```python
import yfinance
from dash import Dash
import plotly.graph_objects
```

requires external packages to be installed.

## 14. Direct vs transitive dependency

MarketPulse distinguishes:

```text
direct dependency
=
our code intentionally imports and uses it

transitive dependency
=
installed because another dependency needs it
```

Example:

```text
MarketPulse
  |
  +-> yfinance
         |
         +-> pandas
```

If MarketPulse code does not import pandas directly, pandas should not automatically become a direct project dependency.

## 15. Reproducibility rule

At TD12, the team validates:

```bash
python -m pip install -r requirements.txt
python src/main.py
python src/dashboard.py
```

The dependency file must represent the actual project.

Avoid:

```text
missing direct dependency
unused dependency
local-only package assumption
undocumented proprietary connector
```

## 16. Visual technology stack

The README highlights technologies that are significant to the learning path:

```text
Python
Git
GitHub
Linux
Bash
Yahoo Finance / yfinance
Dash
Plotly
Bloomberg
```

Standard modules such as:

```text
csv
json
pathlib
```

remain documented here rather than being presented as separate top-level technologies.

## 17. Final dependency model

```text
Python Standard Library
├── pathlib
├── csv
└── json

Direct external Python dependencies
├── yfinance
├── dash
└── plotly

Transitive
└── pandas
    via yfinance

Environment-specific
└── Bloomberg connector
    only if validated by ESILV

Explicitly outside CORE
├── PyYAML
├── numpy
├── requests
└── pytest
```

The intended result is a dependency model that remains small enough for students to understand completely.


## 18. Advanced dependency isolation

The advanced track must not silently expand the CORE dependency contract.

Rule:

```text
advanced-only dependency
=
document in the advanced support

advanced-only dependency
!=
automatic root requirements.txt dependency
```

A package belongs in the root:

```text
requirements.txt
```

only when the actual MarketPulse application imports it as part of the selected CORE implementation.

Current P1 advanced impact:

```text
Linux advanced labs
=
no new Python dependency

Git advanced labs
=
no new Python dependency

Dash advanced labs
=
Dash / Plotly already exist in the TD11 CORE dependency model

SSH / systemd advanced labs
=
system capabilities, not Python CORE dependencies

Bloomberg reference-data advanced lab
=
environment-specific
no connector added without validated LIVE implementation
```

A `PENDING_EXTERNAL` support must never cause speculative dependency installation.

The frozen CORE dependency model above therefore remains unchanged.
