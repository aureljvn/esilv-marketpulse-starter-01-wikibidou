# MarketPulse Teaching Readiness and Dry Run Plan

## 1. Purpose

R1 to R5 closed the documentation remediation cycle.

R6 validates that the teaching repository can actually be used as a progressive classroom system.

The objective is not to redesign MarketPulse.

The objective is to prove that the documented path can be executed, taught and recovered under realistic student conditions.

```text
R1-R5
documentation consistency
        |
        v
R6
teaching execution readiness
        |
        v
Teaching Baseline
```

## 2. Scope

R6 covers:

```text
starter runtime
student bootstrap
TD01-TD12 execution path
cross-TD state transitions
checkpoint evidence
provider fallbacks
instructor recovery paths
final teaching baseline
```

R6 does not add new business scope.

R6 does not turn optional professional extensions into CORE requirements.

## 3. Validation principles

Every readiness claim must be classified as one of:

```text
EXECUTED
=
command or program was actually run

INSPECTED
=
repository artifact was reviewed directly

EXTERNAL VERIFY
=
requires an environment or service unavailable to the current validation runner

NOT TESTED
=
no evidence yet
```

No simulated success is allowed for an unavailable external dependency.

## 4. R6 roadmap

```text
R6.1  Starter runtime baseline
R6.2  Clean-clone and student bootstrap portability
R6.3  Wave 1 dry run - TD01 to TD02
R6.4  Wave 2 dry run - TD03 to TD06
R6.5  Wave 3 dry run - TD07 to TD08
R6.6  Wave 4 dry run - TD09 to TD12
R6.7  Checkpoint and evidence dry run
R6.8  Instructor contingency and provider fallback validation
R6.9  Teaching baseline freeze
```

## 5. R6.1 - Starter runtime baseline

Status:

```text
DONE
```

### 5.1 Source baseline

Validated against the current `main` repository state after R5 closure.

Relevant starter artifacts:

```text
requirements.txt
src/main.py
data/sample/instruments.json
data/sample/prices.csv
config/settings.yml
docs/labs/TD01_BOOTSTRAP_LINUX.md
```

### 5.2 Environment evidence

Executed in an isolated runtime:

```text
Python 3.13.5
Git 2.47.3
```

The repository starter does not require an external Python package for TD01 or TD02.

The command:

```bash
python -m pip install -r requirements.txt
```

completed without requiring a package installation.

### 5.3 Starter data evidence

Executed checks:

```bash
head data/sample/prices.csv
grep -c AAPL data/sample/prices.csv
grep -c SP500 data/sample/prices.csv
```

Observed counts:

```text
AAPL  = 21
SP500 = 21
```

This matches the TD01 expected observations.

### 5.4 Runtime evidence

Executed:

```bash
python src/main.py
```

Observed output:

```text
=== MarketPulse ===

Instrument
AAPL - Apple Inc.
Last price: 266.20 USD

Benchmark
SP500 - S&P 500
Last level: 6742.00

Period: 1 month
Interval: Daily

Observations
AAPL: 21
SP500: 21
```

The result matches the TD01 documented expected output.

### 5.5 Syntax evidence

Executed:

```bash
python -m py_compile src/main.py
```

Result:

```text
PASS
```

### 5.6 R6.1 acceptance criteria

```text
[x] Python runtime available
[x] Git executable available
[x] TD01 requirements install path is valid
[x] starter CSV is readable
[x] starter JSON is readable by the application
[x] AAPL observation count is 21
[x] SP500 observation count is 21
[x] python src/main.py executes successfully
[x] output matches the TD01 contract
[x] src/main.py compiles successfully
```

R6.1 conclusion:

```text
PASS
```

## 6. R6.2 - Clean-clone and student bootstrap portability

Status:

```text
ACCEPTED - PRE-CLASS CHECKS
```

Validate from a genuinely fresh checkout:

```text
new environment
      |
      v
clone or fork
      |
      v
repository root
      |
      v
Python + Git checks
      |
      v
starter data inspection
      |
      v
python src/main.py
```

### 6.1 Repository accessibility inspection

The instructor repository reports:

```text
visibility    = public
private       = false
allow_forking = true
default branch = main
HTTPS clone URL is published
```

Classification:

```text
INSPECTED
```

### 6.2 Local-only dependency scan

Repository search found no CORE runtime dependency on:

```text
os.environ
getenv
dotenv
absolute workstation path
localhost-only service
```

The starter application reads only versioned sample data.

The repository ignore rules exclude local `.env` files.

Classification:

```text
INSPECTED
```

### 6.3 TD01 shell command dry run

Using the exact versioned starter runtime and sample data, the following commands were executed successfully:

```bash
pwd
ls
ls data/sample
cat data/sample/instruments.json
head data/sample/prices.csv
grep AAPL data/sample/prices.csv
grep SP500 data/sample/prices.csv
python --version
git --version
python src/main.py
```

Observed runtime versions:

```text
Python 3.13.5
Git 2.47.3
```

The MarketPulse output remained identical to the documented TD01 output.

Classification:

```text
EXECUTED
```

### 6.4 Team bootstrap safety

`TEAM_TEMPLATE.md` requires only:

```text
TD group
team number
full name
GitHub username
repository name
```

It explicitly forbids:

```text
personal email address
student identification number
phone number
home address
password
access token
private key
cloud billing information
```

Classification:

```text
INSPECTED
```

### 6.5 Remaining external verification

The automated execution sandbox cannot currently resolve `github.com` through its shell network path.

A direct shell command such as:

```bash
git clone https://github.com/tawounfouet/esilv-marketpulse.git
```

therefore cannot be used here as evidence of student-network clone portability.

The repository itself remains accessible through the authenticated repository connector.

This limitation must not be reported as a repository failure.

Classification:

```text
EXTERNAL VERIFY
```

### 6.6 R6.2 acceptance criteria

```text
[ ] actual git clone from the intended student environment
[x] repository is public and forkable
[x] default branch and HTTPS clone endpoint are exposed
[x] no untracked generated file is required by the starter runtime
[x] no local secret or local-only config is required
[x] required TD01 Linux inspection commands execute
[x] python src/main.py works from reconstructed exact versioned starter files
[x] TEAM_TEMPLATE.md can become TEAM.md without requiring sensitive data
```

R6.2 conclusion:

```text
READY FOR EXTERNAL CLONE VERIFY
```

R6.2 does not block the remaining local pedagogical dry run.

## 7. R6.3 - Wave 1 dry run

Status:

```text
DONE
```

Validated:

```text
TD01 Bootstrap + Linux
TD02 Python + CSV / JSON
```

### 7.1 TD01 execution result

The starter path was executed with the versioned CORE assets.

Validated commands include:

```bash
pwd
ls
ls data/sample
cat data/sample/instruments.json
head data/sample/prices.csv
grep AAPL data/sample/prices.csv
grep SP500 data/sample/prices.csv
python --version
git --version
python src/main.py
```

Results:

```text
Python runtime available
Git runtime available
AAPL rows = 21
SP500 rows = 21
starter output matches the documented TD01 output
```

Classification:

```text
EXECUTED
```

### 7.2 TD02 end-state implementation

A temporary teaching working tree was created from the exact starter code.

The TD02 instructions were then applied without changing repository architecture.

Implemented helpers:

```python
get_first_close(...)
get_last_close(...)
display_market_summary(...)
```

The implementation preserves:

```text
csv.DictReader
json.load
filter_prices(...)
src/main.py entry point
standard-library-only dependency model
```

### 7.3 Numeric conversion evidence

The raw CSV close value was confirmed as:

```text
str
```

The helper return values were confirmed as:

```text
float
```

Observed values:

```text
AAPL
first close = 250.0
last close  = 266.2

SP500
first close = 6600.0
last close  = 6742.0
```

Classification:

```text
EXECUTED
```

### 7.4 TD02 target output

Executed:

```bash
python src/main.py
```

Observed output:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close  : 250.00 USD
Last close   : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close  : 6600.00
Last close   : 6742.00
```

This matches the documented TD02 target behaviour.

### 7.5 TD02 syntax validation

Executed:

```bash
python -m py_compile src/main.py
```

Result:

```text
PASS
```

### 7.6 TD02 -> TD03 working-tree handoff

A local Git baseline was created only for dry-run verification.

After applying the TD02 changes:

```bash
git status --short
```

reported:

```text
 M src/main.py
```

The repository `.gitignore` correctly suppresses generated Python cache files.

Executed:

```bash
git diff --check
```

Result:

```text
PASS
```

The meaningful TD02 change therefore remains available for TD03 exactly as intended:

```text
TD02
working Python change
      |
      v
TD03
git status
git diff
git add
git commit
git log
```

### 7.7 Scope protection

The dry run confirmed that TD02 does not require:

```text
pandas
return calculations
base-100 calculations
relative performance
feature branches
Pull Requests
```

The Wave 1 scope remains focused on Linux inspection and basic Python data handling.

### 7.8 Timing interpretation

The technical path contains no newly discovered hidden setup or refactor.

The documented 80-minute CORE plus 10-minute buffer remains structurally plausible.

Actual classroom completion time remains a teaching observation rather than machine-execution evidence.

Classification:

```text
INSPECTED
```

### 7.9 R6.3 acceptance criteria

```text
[x] TD01 starter executes
[x] TD01 Linux inspection commands are coherent
[x] TD02 starts from the TD01 state
[x] JSON metadata loads correctly
[x] CSV observations load correctly
[x] AAPL and SP500 each contain 21 rows
[x] close values are converted from str to float
[x] reusable first/last close helpers work
[x] reusable market summary works
[x] TD02 target output is reproducible
[x] no return calculation is introduced
[x] no external Python dependency is introduced
[x] TD02 leaves a meaningful src/main.py working-tree change for TD03
[x] generated Python cache files remain ignored
[x] git diff --check passes
```

R6.3 conclusion:

```text
PASS
```

## 8. R6.4 - Wave 2 dry run

Status:

```text
ACCEPTED - PRE-CLASS CHECKS
```

Validated scope:

```text
TD03 Git Local Workflow
TD04 Branches + Merge
TD04 -> TD05 Team Baseline Gate
TD05 remote branch mechanics
TD06 review and integration mechanics
```

The GitHub Pull Request and review UI still require one real team-fork verification.

### 8.1 Validation topology

The dry run used:

```text
student-a working repository
student-b working repository
team.git bare shared remote
integrator working repository
```

This provided a real Git remote and independent local histories without creating artificial branches or Pull Requests in the instructor repository.

For the Git-only mechanics, the temporary harness used a reduced sample CSV with the same MarketPulse code shape and the same first and last dates.

The authoritative 21-row AAPL/SP500 starter-data validation remains R6.3.

### 8.2 TD03 - local Git workflow

Starting state:

```text
src/main.py modified
=
real TD02-style Python change
```

Executed:

```bash
git status
git diff
git add src/main.py
git diff --staged
git commit
git log --oneline
git show HEAD
python src/main.py
```

Observed transition:

```text
working tree
      |
      v
staged src/main.py
      |
      v
feat: improve MarketPulse market summary
      |
      v
clean main
```

Validation:

```text
git diff --check = PASS
git diff --staged --check = PASS
runtime after commit = PASS
working tree after commit = clean
```

Classification:

```text
EXECUTED
```

### 8.3 TD04 - branch isolation and merge

Created:

```text
feature/display-observation-dates
```

The branch added only:

```text
get_first_date(...)
get_last_date(...)
date presentation in the reusable summary
```

Executed:

```bash
git switch -c feature/display-observation-dates
git status
git diff
python src/main.py
git add src/main.py
git diff --staged
git commit
git log --oneline --graph --decorate --all
git diff main..feature/display-observation-dates
git switch main
git merge feature/display-observation-dates
git branch -d feature/display-observation-dates
```

The branch diff was limited to:

```text
src/main.py
10 insertions
```

Git selected a valid fast-forward merge.

No artificial merge commit was forced.

After merge:

```text
feature visible from main
feature commit still visible in history
MarketPulse runtime = PASS
working tree = clean
```

Classification:

```text
EXECUTED
```

### 8.4 Team Baseline Gate - divergent local histories

The dry run deliberately created two valid but different TD04 histories.

Before synchronization:

```text
student-a/main != student-b/main
```

Student B then executed the documented safety sequence:

```bash
git switch main
git status
git branch archive/td04-local
git fetch origin
git reset --hard origin/main
```

After synchronization:

```text
student-b HEAD = origin/main
archive/td04-local = previous student-b TD04 history
working tree = clean
MarketPulse runtime = PASS
```

The test proved both required properties:

```text
common shared baseline established
+
local learning history preserved
```

This confirms the controlled hard reset is technically justified by the safety branch and clean-tree preconditions.

Classification:

```text
EXECUTED
```

### 8.5 TD05 - remote branch mechanics

From the synchronized shared baseline, two distinct student contributions were created.

Student A:

```text
branch
=
feature/display-provider-label

commit
=
feat: display provider label

changed file
=
src/main.py
```

Student B:

```text
branch
=
docs/improve-execution-docs

commit
=
docs: clarify MarketPulse execution

changed file
=
docs/EXECUTION.md
```

Executed for both students:

```bash
git switch main
git pull --ff-only
git switch -c <feature-branch>
git add <intended-file>
git diff --staged --check
git commit
git push -u origin <feature-branch>
```

The shared remote then contained:

```text
main
feature/display-provider-label
docs/improve-execution-docs
```

Both local feature branches tracked their corresponding remote branches.

The candidate changes were inspectable as:

```text
origin/main
      |
      +--> origin/feature/display-provider-label

origin/main
      |
      +--> origin/docs/improve-execution-docs
```

Classification:

```text
EXECUTED
```

### 8.6 Pull Request boundary

The following Pull Request properties were validated structurally from the actual branch state and from the TD05 contract:

```text
source = pushed student feature branch
target = team main
diff = intended branch change only
PR remains open until TD06
```

However, the dry-run environment does not contain a disposable student team fork.

No artificial Pull Request was created in:

```text
tawounfouet/esilv-marketpulse
```

because that would pollute the instructor repository with synthetic teaching evidence.

Required remaining check:

```text
open one real PR inside a disposable or actual team fork
verify source branch
verify target branch
verify title and description
verify Files changed
leave PR open
```

Classification:

```text
EXTERNAL VERIFY
```

### 8.7 TD06 - review semantics

The two remote candidate diffs were inspected before integration.

Provider-label candidate:

```text
files changed = src/main.py only
scope = 2 inserted lines
runtime = PASS
blocking issue = none
review outcome = APPROVE
```

Execution-documentation candidate:

```text
files changed = docs/EXECUTION.md only
scope = documentation only
blocking issue = none
review outcome = APPROVE
```

No correction commit was manufactured because no real defect was found.

This validates the TD06 rule:

```text
no real defect
      |
      v
meaningful review
      |
      v
approval
```

rather than:

```text
review exercise
      |
      v
fake defect
      |
      v
fake fix commit
```

Classification:

```text
EXECUTED for diff inspection and integration logic
INSPECTED for GitHub review-outcome semantics
```

### 8.8 Reviewed integration and synchronization

After inspection, both branches were integrated into the shared remote main.

The resulting graph contained:

```text
reviewed provider-label integration
+
reviewed execution-documentation integration
+
previous TD04 baseline
+
previous TD03 commit
```

Both student environments then executed:

```bash
git switch main
git pull --ff-only
git status
python src/main.py
```

Final state:

```text
student-a HEAD = origin/main
student-b HEAD = origin/main
student-a working tree = clean
student-b working tree = clean
student-a runtime = PASS
student-b runtime = PASS
```

Classification:

```text
EXECUTED
```

### 8.9 TD06 -> TD07 handoff

Wave 2 now leaves:

```text
one synchronized main
+
established branch workflow
+
established remote push workflow
+
review-before-merge rule
+
clean working trees
```

TD07 can therefore introduce:

```text
src/analytics.py
```

as the next real feature instead of reteaching the collaboration workflow.

### 8.10 R6.4 acceptance criteria

```text
[x] TD03 starts from a meaningful TD02 working-tree change
[x] git status and git diff expose that change
[x] intended work can be staged deliberately
[x] git diff --staged represents the next commit
[x] meaningful local commit can be created and inspected
[x] TD04 starts from clean main
[x] feature branch isolates observation-date work
[x] feature branch compares cleanly against main
[x] fast-forward merge works and is accepted
[x] branch can be deleted without losing history
[x] two divergent TD04 local mains can be reproduced
[x] archive/td04-local preserves pre-alignment history
[x] controlled reset aligns another student to origin/main
[x] remote feature branches can be pushed with upstream tracking
[x] remote candidate diffs contain only intended work
[ ] actual GitHub Pull Request opened in a team fork
[ ] actual GitHub Files changed view verified in a team fork
[ ] actual review submitted by another student account
[ ] actual PR merged through the GitHub UI after review
[x] no fake correction commit is required when review finds no defect
[x] reviewed branch integration mechanics work
[x] all student mains can synchronize to the integrated remote main
[x] MarketPulse remains executable after synchronization
[x] Wave 2 leaves a clean handoff for TD07
```

R6.4 conclusion:

```text
LOCAL AND REMOTE GIT MECHANICS PASS
GITHUB PR/REVIEW UI VERIFY REMAINS
```

R6.4 does not block the Wave 3 dry run.

## 9. R6.5 - Wave 3 dry run

Status:

```text
ACCEPTED - PRE-CLASS CHECKS
```

Validated:

```text
TD07 Data Normalization + Comparison
TD08 Yahoo Finance provider contract
TD07 -> TD08 analytics reuse
```

Yahoo LIVE installation and retrieval still require an external network-enabled environment.

### 9.1 TD07 - canonical numeric rows

The exact starter sample was used:

```text
AAPL  = 21 observations
SP500 = 21 observations
```

Local CSV rows were normalized before analytics.

Validated types:

```text
date   -> str
ticker -> str
open   -> float
high   -> float
low    -> float
close  -> float
volume -> int
```

Classification:

```text
EXECUTED
```

### 9.2 TD07 - common-date alignment

Implemented and executed:

```python
index_by_date(...)
align_series(...)
```

Observed result:

```text
instrument raw rows = 21
benchmark raw rows  = 21
common dates        = 21
first common date   = 2026-09-01
last common date    = 2026-09-30
```

Every aligned instrument row uses the same date as the corresponding benchmark row.

Classification:

```text
EXECUTED
```

### 9.3 TD07 - period return

Executed against aligned rows.

Observed values:

```text
AAPL
first close = 250.00
last close  = 266.20
period return = 6.48000000%

SP500
first close = 6600.00
last close  = 6742.00
period return = 2.15151515%
```

No return value was hard-coded.

Classification:

```text
EXECUTED
```

### 9.4 TD07 - relative performance

Executed:

```text
instrument return
-
benchmark return
=
relative performance
```

Observed result:

```text
6.48000000
-
2.15151515
=
4.32848485 percentage points
```

The subtraction direction matches the functional contract.

Classification:

```text
EXECUTED
```

### 9.5 TD07 - base 100

Executed:

```python
calculate_base_100(...)
```

Observed values:

```text
AAPL
100.00000000 -> 106.48000000

SP500
100.00000000 -> 102.15151515
```

Both series start at exactly 100.

The final base-100 values are mathematically consistent with the period returns.

Classification:

```text
EXECUTED
```

### 9.6 TD07 - analytics isolation

The dry-run `src/analytics.py` contains only provider-neutral functions:

```text
index_by_date
align_series
calculate_period_return
calculate_base_100
calculate_relative_performance
```

A scan confirmed zero occurrences of:

```text
AAPL
SP500
^GSPC
Yahoo
Bloomberg
```

Classification:

```text
EXECUTED
```

### 9.7 TD07 terminal result

Executed:

```bash
python src/main.py
```

Observed output:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Period return : 6.48%

Benchmark
SP500 - S&P 500
Period return : 2.15%

Relative performance
AAPL vs SP500 : +4.33 percentage points

Base 100
AAPL  : 100.00 -> 106.48
SP500 : 100.00 -> 102.15
```

Executed:

```bash
python -m py_compile src/analytics.py src/main.py
```

Result:

```text
PASS
```

### 9.8 TD08 - dependency boundary

The TD08 dry-run dependency file contains one new direct dependency:

```text
yfinance
```

No transitive package such as `pandas` was added manually.

The current public yfinance reference still documents support for:

```text
Ticker.history(...)
period = 1mo
interval = 1d
auto_adjust = False
```

The validation runner cannot resolve external package hosts through its shell network path.

Therefore:

```text
requirements contract = INSPECTED
current call signature = INSPECTED
actual pip installation = EXTERNAL VERIFY
```

### 9.9 TD08 - Yahoo provider contract

Implemented the documented provider boundary:

```python
fetch_yahoo_prices(
    symbol,
    canonical_ticker,
    period="1mo",
    interval="1d",
)
```

A controlled yfinance-compatible test double was injected only at the external acquisition boundary.

The provider implementation itself remained unchanged from the teaching shape.

Validated calls:

```text
AAPL
period=1mo
interval=1d
auto_adjust=False

^GSPC
period=1mo
interval=1d
auto_adjust=False
```

Classification:

```text
EXECUTED WITH CONTROLLED PROVIDER DOUBLE
```

This is not classified as Yahoo LIVE evidence.

### 9.10 TD08 - canonical ticker preservation

The simulated provider returned Yahoo-shaped rows for:

```text
AAPL
^GSPC
```

The normalized MarketPulse rows preserved:

```text
AAPL  -> AAPL
^GSPC -> SP500
```

Validated canonical row types:

```text
date   -> str
ticker -> str
open   -> float
high   -> float
low    -> float
close  -> float
volume -> int
```

The provider-specific benchmark symbol did not propagate into analytics.

Classification:

```text
EXECUTED
```

### 9.11 TD08 - unequal provider calendars

The controlled provider double deliberately returned:

```text
AAPL raw rows  = 21
SP500 raw rows = 20
```

One benchmark date was omitted intentionally.

The unchanged TD07 alignment produced:

```text
aligned AAPL  = 20
aligned SP500 = 20
```

Every aligned pair shared the same date.

This proves TD08 does not rely on equal raw row counts or list position.

Classification:

```text
EXECUTED
```

### 9.12 TD08 - analytics reuse proof

A hash of `src/analytics.py` was captured before the TD08 provider work.

After provider creation and Yahoo-path orchestration:

```text
src/analytics.py hash unchanged
```

The same functions were reused:

```text
align_series(...)
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

No Yahoo-specific branch was added to analytics.

Classification:

```text
EXECUTED
```

### 9.13 TD08 - empty-provider behaviour

The provider was also exercised with an unsupported symbol whose controlled history was empty.

Observed result:

```text
ValueError:
No Yahoo Finance data returned for INVALID
```

MarketPulse therefore does not silently run analytics on an empty provider result.

Classification:

```text
EXECUTED
```

### 9.14 TD08 terminal result with provider double

Executed through the Yahoo orchestration path:

```text
Provider
Yahoo Finance via yfinance

Market configuration
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Period     : 1 month
Interval   : Daily

Aligned observations : 20
Instrument return : 6.48%
Benchmark return  : 2.15%

Relative performance
AAPL vs SP500 : +4.33 percentage points

Base 100 starts : 100.00 / 100.00
```

This validates the provider-to-analytics wiring.

It is not Yahoo LIVE market evidence.

### 9.15 Remaining external Yahoo verification

The following commands require a network-enabled student or instructor environment:

```bash
python -m pip install yfinance
python -m pip show yfinance
python src/main.py
```

The LIVE provider check must confirm non-empty current data for:

```text
AAPL
^GSPC
```

Required evidence:

```text
successful remote retrieval
canonical AAPL rows
canonical SP500 rows
common aligned dates
provider label = Yahoo Finance via yfinance
```

Classification:

```text
EXTERNAL VERIFY
```

No static CSV run or controlled provider double may be presented as successful Yahoo LIVE evidence.

### 9.16 Git workflow inheritance

TD07 and TD08 correctly instruct students to reuse the established:

```text
branch
push
Pull Request
review
merge
```

workflow.

The local and remote Git mechanics were already executed in R6.4.

The GitHub Pull Request and review UI remain part of the external team-fork verification already recorded by R6.4.

### 9.17 R6.5 acceptance criteria

```text
[x] TD07 creates src/analytics.py
[x] CSV rows are normalized before analytics
[x] AAPL and SP500 align on 21 common starter dates
[x] period return is calculated from aligned rows
[x] AAPL starter return = 6.48%
[x] SP500 starter return = 2.15151515%
[x] relative performance = instrument minus benchmark
[x] relative performance = 4.32848485 percentage points
[x] both base-100 series start at 100
[x] final base-100 values match period-return mathematics
[x] analytics.py contains no provider-specific identifier
[x] python src/main.py reproduces the TD07 target output
[x] TD08 dependency contract contains yfinance as the direct dependency
[x] current yfinance history call shape remains compatible with the teaching snippet
[x] Yahoo provider normalizes provider-shaped rows to the canonical schema
[x] AAPL remains canonical AAPL
[x] ^GSPC becomes canonical SP500
[x] period=1mo is passed to both provider calls
[x] interval=1d is passed to both provider calls
[x] auto_adjust=False is passed explicitly
[x] unequal raw provider calendars are aligned by common date
[x] TD07 analytics.py remains byte-for-byte unchanged during TD08 wiring
[x] empty provider output raises an explicit error
[ ] yfinance installed from PyPI in a network-enabled teaching environment
[ ] Yahoo LIVE AAPL retrieval returns non-empty data
[ ] Yahoo LIVE ^GSPC retrieval returns non-empty data
[ ] Checkpoint B Yahoo evidence captured from an actual successful remote retrieval
```

R6.5 conclusion:

```text
TD07 ANALYTICS PASS
TD08 PROVIDER CONTRACT PASS
YAHOO LIVE VERIFY REMAINS
```

R6.5 does not block the Wave 4 dry run.

## 10. R6.6 - Wave 4 dry run

Status:

```text
ACCEPTED - PRE-CLASS CHECKS
```

Validated:

```text
TD09 Bloomberg Introduction
TD10 Bloomberg Provider
TD11 Dash Dashboard contract
TD12 Integration + Release contract
```

Selected Bloomberg teaching mode for this dry run:

```text
APPROVED_SAMPLE
```

No claim of LIVE Bloomberg connectivity is made.

### 10.1 Dry-run finding - fallback window mismatch

The first end-to-end run uncovered a real contract mismatch.

Before remediation:

```text
snapshot lookback = 1 month
snapshot interval = Daily

Bloomberg APPROVED_SAMPLE fixture
=
4 AAPL observations
+
4 SP500 observations
```

The provider boundary and calculations worked technically, but the final presentation claimed a one-month comparison while the fallback fixture covered only:

```text
2026-09-01
to
2026-09-04
```

This was not acceptable for the frozen CORE contract.

### 10.2 Remediation - full one-month fallback

The approved Bloomberg fallback was expanded from the canonical starter CSV.

After remediation:

```text
AAPL fallback observations  = 21
SP500 fallback observations = 21
expected canonical rows     = 42

first date = 2026-09-01
last date  = 2026-09-30
```

Updated repository assets:

```text
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
```

The values remain explicitly:

```text
illustrative teaching values
not certified Bloomberg historical observations
```

The wrapper keys remain explicitly:

```text
teaching wrapper keys
not Bloomberg LIVE field mnemonics
```

Classification:

```text
REMEDIATED
```

### 10.3 TD09 - mapping contract

A representative TD09 mapping document was produced in the disposable dry-run repository.

Validated content:

```text
Access mode = APPROVED_SAMPLE
Live connectivity = not demonstrated

AAPL
-> AAPL US Equity

SP500
-> SPX Index

observation_date -> date
open_value       -> open
high_value       -> high
low_value        -> low
close_value      -> close
volume_value     -> volume
```

The mapping also preserved:

```text
ticker
=
application mapping to AAPL or SP500
```

and contained a usable TD10 handoff.

A security scan found no credential field or sensitive session value.

Classification:

```text
EXECUTED / INSPECTED
```

### 10.4 TD10 - APPROVED_SAMPLE provider normalization

The documented Bloomberg provider scaffold was implemented in the disposable dry-run repository.

Executed boundaries:

```text
load_bloomberg_reference_sample(...)
find_reference_series(...)
normalize_reference_series(...)
fetch_approved_sample_prices(...)
```

Identifier mapping:

```text
AAPL
-> AAPL US Equity
-> canonical AAPL rows

SP500
-> SPX Index
-> canonical SP500 rows
```

The provider returned:

```text
AAPL rows  = 21
SP500 rows = 21
```

The combined normalized result was compared with:

```text
data/sample/bloomberg_reference_expected.json
```

Result:

```text
42 / 42 rows exact match
```

Classification:

```text
EXECUTED
```

### 10.5 TD10 - shared analytics reuse

The Bloomberg rows were passed to the same TD07 functions:

```text
align_series(...)
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

No Bloomberg-specific analytical function was introduced.

Observed results on the full teaching window:

```text
AAPL period return
=
+6.48%

SP500 period return
=
+2.15151515%

relative performance
=
+4.32848485 percentage points

AAPL base 100
=
100.00 -> 106.48

SP500 base 100
=
100.00 -> 102.15151515
```

These values are consistent with the TD07 local-data dry run because the approved fallback intentionally reuses the starter teaching values.

Classification:

```text
EXECUTED
```

### 10.6 TD10 - build_market_snapshot contract

Implemented:

```python
build_market_snapshot(...)
```

The returned dictionary contained exactly the required CORE keys:

```text
provider
lookback
interval
instrument
benchmark
instrument_return
benchmark_return
relative_performance
instrument_base_100
benchmark_base_100
```

Validated invariants:

```text
provider
=
Bloomberg stage - APPROVED_SAMPLE

lookback
=
1 month

interval
=
Daily

instrument ticker
=
AAPL

benchmark ticker
=
SP500

returns
=
numeric

relative performance
=
instrument return - benchmark return

base-100 row counts
=
21 + 21

both base-100 series start at 100

both base-100 series use identical aligned dates
```

Classification:

```text
EXECUTED
```

### 10.7 TD10 - import-safe main.py

Executed an import-only check for:

```text
src/main.py
```

Observed terminal output during import:

```text
none
```

The dry-run implementation preserved:

```python
if __name__ == "__main__":
    main()
```

Running:

```bash
python src/main.py
```

produced:

```text
Provider
Bloomberg stage - APPROVED_SAMPLE

Instrument : AAPL - Apple Inc.
Benchmark  : SP500 - S&P 500
Period     : 1 month
Interval   : Daily

Instrument return : +6.48%
Benchmark return  : +2.15%

Relative performance
AAPL vs SP500 : +4.33 percentage points
```

Classification:

```text
EXECUTED
```

### 10.8 TD11 - dependency state

Validation environment state:

```text
plotly = installed
dash = not installed
yfinance = not installed
```

Actual Plotly figure construction was therefore executable.

The external package installation path remained unavailable because the shell environment could not reach the package index.

The final direct dependency contract remains:

```text
yfinance
dash
plotly
```

No transitive dependency was promoted manually.

Classification:

```text
Plotly = EXECUTED
Dash installation = EXTERNAL VERIFY
```

### 10.9 TD11 - dashboard isolation

A representative `src/dashboard.py` was executed with:

```text
real plotly.graph_objects
+
controlled minimal Dash dependency double
```

The double replaced only the unavailable external Dash package.

The MarketPulse application code, provider code, analytics code and snapshot builder were unchanged.

The dashboard:

```text
imports build_market_snapshot
builds the snapshot once
reads provider context
reads instrument context
reads benchmark context
reads three performance values
reads both base-100 series
builds one Plotly figure
```

A source scan confirmed zero dashboard calls to:

```text
fetch_yahoo_prices(...)
fetch_bloomberg_prices(...)
fetch_raw_bloomberg_history(...)
```

and zero dashboard calls to:

```text
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

Classification:

```text
EXECUTED WITH CONTROLLED DASH DEPENDENCY DOUBLE
```

This is not classified as a real Dash server run.

### 10.10 TD11 - real Plotly comparison figure

The actual installed Plotly library created:

```text
1 Figure
2 Scatter traces
```

Observed traces:

```text
AAPL  = 21 points
SP500 = 21 points
```

Both traces start at:

```text
100
```

The dashboard values were compared directly with the snapshot values.

Result:

```text
instrument return = identical
benchmark return = identical
relative performance = identical
```

No analytical value was recomputed in the dashboard.

Classification:

```text
EXECUTED
```

### 10.11 TD11 - current API compatibility inspection

The current official Dash API reference still documents:

```python
app.run(debug=False)
```

and the current Plotly graph-object API still supports:

```text
go.Figure()
go.Scatter(...)
Figure.add_trace(...)
Figure.update_layout(...)
```

The TD11 teaching shape is therefore not relying on a removed API.

Classification:

```text
INSPECTED
```

### 10.12 TD12 - source and dependency reconciliation

The simulated final source tree contained direct imports for:

```text
yfinance
dash
plotly
```

The simulated final `requirements.txt` contained exactly:

```text
yfinance
dash
plotly
```

Result:

```text
direct external imports
=
declared direct dependencies
```

No guessed Bloomberg Python connector was added for APPROVED_SAMPLE mode.

Classification:

```text
EXECUTED
```

### 10.13 TD12 - README runtime contract

The simulated final README documented all three required commands:

```bash
python -m pip install -r requirements.txt
python src/main.py
python src/dashboard.py
```

The final provider statement remained:

```text
Bloomberg stage - APPROVED_SAMPLE
```

with an explicit statement that LIVE Bloomberg connectivity was not demonstrated.

Classification:

```text
INSPECTED
```

### 10.14 TD12 - fresh local clone

A new bare Git remote was created from the simulated integrated release.

A second directory then performed a genuinely fresh Git clone from that remote.

From the fresh clone:

```bash
python src/main.py
python -m py_compile     src/analytics.py     src/main.py     src/dashboard.py     src/providers/bloomberg_provider.py     src/providers/yahoo_provider.py
```

all succeeded.

The dashboard module also executed successfully against the external controlled Dash dependency double.

After execution:

```text
git status = clean
tracked __pycache__ / *.pyc files = 0
```

This validates repository completeness and relative-path portability independently of the original working directory.

Classification:

```text
EXECUTED
```

### 10.15 TD12 - clean dependency installation boundary

Executed from the fresh clone:

```bash
python -m pip install -r requirements.txt
```

The command could not complete because the validation environment cannot access the external package index.

The failure occurred while resolving:

```text
yfinance
```

This is consistent with the network limitation already recorded during R6.5.

It is not classified as a missing or invalid repository dependency.

Required remaining verification:

```text
network-enabled environment
+
python -m pip install -r requirements.txt
+
python src/main.py
+
python src/dashboard.py
```

Classification:

```text
EXTERNAL VERIFY
```

### 10.16 Git workflow inheritance

TD09 through TD12 reuse the standard:

```text
branch
push
Pull Request
review
merge
```

workflow already validated mechanically in R6.4.

No synthetic GitHub Pull Request or review was created in the instructor repository during R6.6.

Actual GitHub PR/review UI verification remains the same external item recorded in R6.4.

### 10.17 R6.6 acceptance criteria

```text
[x] TD09 supports explicit APPROVED_SAMPLE mode
[x] TD09 maps AAPL to AAPL US Equity
[x] TD09 maps SP500 to SPX Index
[x] wrapper keys are labelled as teaching keys
[x] LIVE connectivity is explicitly not claimed
[x] no Bloomberg credential is required by the fallback
[x] fallback fixture covers the full 1-month teaching window after remediation
[x] fallback fixture contains 21 AAPL observations
[x] fallback fixture contains 21 SP500 observations
[x] expected canonical reference contains 42 rows
[x] TD10 normalized output matches all 42 expected rows
[x] canonical tickers remain AAPL and SP500
[x] TD07 analytics are reused unchanged
[x] build_market_snapshot(...) exists in the dry-run implementation
[x] snapshot contains all 10 required keys
[x] snapshot lookback = 1 month
[x] snapshot interval = Daily
[x] snapshot provider label is honest
[x] snapshot base-100 series contain 21 aligned rows each
[x] src/main.py is import-safe
[x] terminal path consumes the shared snapshot
[x] terminal path executes in APPROVED_SAMPLE mode
[x] dashboard imports build_market_snapshot(...)
[x] dashboard contains no provider request
[x] dashboard contains no analytical formula
[x] real Plotly figure contains AAPL and SP500
[x] both Plotly traces contain 21 points
[x] terminal and dashboard consume identical business values
[x] final direct-import dependency set matches requirements.txt
[x] final README contains the three required commands
[x] fresh local clone reproduces the terminal path
[x] fresh clone compiles the full final Python source tree
[x] fresh clone remains Git-clean after runtime validation
[ ] dash installed from package index in a network-enabled clean environment
[ ] python src/dashboard.py served with the real Dash package in a clean environment
[ ] full python -m pip install -r requirements.txt succeeds from a network-enabled clean environment
[ ] actual TD09-TD12 Pull Request/review cycle verified through GitHub team-fork UI
```

R6.6 conclusion:

```text
TD09 APPROVED_SAMPLE MAPPING PASS
TD10 PROVIDER + SNAPSHOT PASS
TD11 PRESENTATION CONTRACT PASS
TD12 CLEAN-CLONE STRUCTURE PASS
REAL DASH INSTALL / FULL PIP / GITHUB UI VERIFY REMAIN
```

R6.6 does not block the checkpoint/evidence dry run.

## 11. R6.7 - Checkpoint and evidence dry run

Status:

```text
ACCEPTED - PRE-CLASS CHECKS
```

Validated:

```text
Checkpoint A
Checkpoint B
Checkpoint C
individual README contract
directory naming
screenshot naming
external-evidence recovery semantics
```

No synthetic screenshot was created or treated as proof.

### 11.1 Canonical package shape

A disposable evidence tree was created with one representative GitHub username:

```text
evidence/
|-- checkpoint-a/
|   +-- alice-martin/
|       |-- README.md
|       |-- 01_terminal_python.png
|       |-- 02_git_status_log.png
|       +-- 03_branch_merge.png
|
|-- checkpoint-b/
|   +-- alice-martin/
|       |-- README.md
|       |-- 01_pull_request.png
|       |-- 02_code_review.png
|       |-- 03_yahoo_market_data.png
|       +-- 04_instrument_benchmark.png
|
+-- checkpoint-c/
    +-- alice-martin/
        |-- README.md
        |-- 01_final_market_data.png
        |-- 02_dash_dashboard.png
        |-- 03_final_pull_request.png
        +-- 04_reproducible_run.png
```

The PNG files in this structural test were empty placeholders used only to validate package naming.

They were not treated as evidence.

Validated counts:

```text
Checkpoint A = 3 required screenshots
Checkpoint B = 4 required screenshots
Checkpoint C = 4 required screenshots

Total required screenshots = 11

Individual README files = 3
```

Classification:

```text
EXECUTED
```

### 11.2 Filename contract

Every required screenshot name matches:

```text
two-digit number
+
underscore
+
lowercase snake case
+
.png
```

Validated names:

```text
Checkpoint A
01_terminal_python.png
02_git_status_log.png
03_branch_merge.png

Checkpoint B
01_pull_request.png
02_code_review.png
03_yahoo_market_data.png
04_instrument_benchmark.png

Checkpoint C
01_final_market_data.png
02_dash_dashboard.png
03_final_pull_request.png
04_reproducible_run.png
```

No conflicting filename was found in the canonical checkpoint document or closing TD files.

Classification:

```text
EXECUTED / INSPECTED
```

### 11.3 Individual README contract

Each disposable checkpoint README listed exactly the screenshot filenames required for its package.

The canonical README contract can express:

```text
student name
GitHub username
branch
main commits
Pull Request
reviewed Pull Request
work completed
main difficulty
evidence filenames
```

The GitHub username remains the individual evidence-directory key.

Sensitive identifiers such as:

```text
personal email
student identifier
phone
home address
password
token
private key
cloud billing data
```

are not required.

Classification:

```text
EXECUTED / INSPECTED
```

### 11.4 Checkpoint A - fast-forward evidence defect

The initial checkpoint contract had a real sequencing defect.

TD04 allowed:

```text
valid fast-forward merge
+
feature-branch deletion
```

before Checkpoint A capture.

After branch deletion, a fast-forward history can appear fully linear and no longer provide enough visible branch evidence for:

```text
03_branch_merge.png
```

This would encourage students to force unnecessary merge commits or capture ambiguous evidence.

Classification:

```text
DEFECT FOUND
```

### 11.5 Checkpoint A remediation

The canonical evidence contract and TD04 now require capture:

```text
after successful merge
+
before deleting the merged feature branch
```

Recommended evidence commands:

```bash
git branch
git branch --merged
git log --oneline --graph --decorate --all
```

A real fast-forward merge was executed in the dry run.

Before deletion:

```text
feature/display-observation-dates
+
main
```

both pointed to the integrated feature commit.

`git branch --merged` listed the feature branch as merged.

After deletion, the feature commit remained in history.

This proves the revised evidence sequence works without forcing a merge commit.

Classification:

```text
EXECUTED
```

Remediation commits:

```text
a336fd66801019e3881fb46a57f5b3b59e94470a
docs: harden checkpoint evidence capture rules

125431d770c5f2e29f9c3ec6c9346c16f318cbe8
docs: make TD04 branch evidence fast-forward safe
```

### 11.6 Checkpoint A evidence feasibility

Required proof:

```text
01_terminal_python.png
=
local terminal + MarketPulse execution

02_git_status_log.png
=
local Git state + attributable history

03_branch_merge.png
=
local branch and merge evidence
```

All three evidence meanings are producible from the normal TD01-TD04 workflow.

No external market-data service is required.

No artificial merge is required.

Classification:

```text
PASS
```

### 11.7 Checkpoint B - GitHub contribution evidence

Required:

```text
01_pull_request.png
02_code_review.png
```

The evidence semantics are coherent with TD05-TD06:

```text
PR authored by the student
+
review performed by the student on another team member's PR
```

The same screenshot must not be copied across students as proof of personal Git contribution.

The dry-run environment cannot impersonate a second student account and no synthetic instructor-repository PR was created.

Classification:

```text
CONTRACT PASS
ACTUAL MULTI-USER GITHUB UI = EXTERNAL VERIFY
```

### 11.8 Checkpoint B - Yahoo external dependency defect

The original contract required:

```text
03_yahoo_market_data.png
```

immediately after TD08 but did not define a canonical response to a genuine Yahoo outage.

That could make an otherwise valid student checkpoint impossible to complete at the scheduled time for reasons outside the student's control.

Classification:

```text
DEFECT FOUND
```

### 11.9 Checkpoint B remediation

The canonical evidence contract now defines:

```text
READY
PENDING_EXTERNAL
COMPLETE
```

For a documented Yahoo outage:

```text
03_yahoo_market_data.png
=
PENDING_EXTERNAL
```

while the other Checkpoint B evidence can still be submitted and explained.

The student later captures the real Yahoo evidence during an instructor-approved recovery window.

Explicitly forbidden substitutions:

```text
local CSV presented as Yahoo
controlled provider double presented as Yahoo LIVE
old unrelated screenshot
fabricated remote values
```

TD08 now points directly to this canonical recovery rule.

Classification:

```text
REMEDIATED
```

Remediation commit:

```text
b03c8760ecc29cfb1843753f61ce0402881ced40
docs: define TD08 Yahoo evidence recovery
```

### 11.10 Checkpoint B evidence feasibility

Required proof categories:

```text
01_pull_request.png
=
GitHub UI / individual contribution

02_code_review.png
=
GitHub UI / different-student review

03_yahoo_market_data.png
=
real remote Yahoo retrieval

04_instrument_benchmark.png
=
application behaviour for AAPL + SP500
1 month + Daily
```

The contract no longer requires fabrication when Yahoo is unavailable.

Remaining real-world verification:

```text
team-fork PR
different-account review
successful Yahoo remote retrieval
```

Classification:

```text
CONTRACT PASS
EXTERNAL CAPTURE REMAINS
```

### 11.11 Checkpoint C - final provider evidence

The canonical contract now explicitly accepts the actual authorized final provider mode.

Examples:

```text
Yahoo Finance via yfinance
Bloomberg - LIVE
Bloomberg stage - APPROVED_SAMPLE
```

If APPROVED_SAMPLE is used:

```text
APPROVED_SAMPLE
!=
LIVE Bloomberg evidence
```

The exact mode must remain visible.

This is consistent with the TD09-TD10 fallback contract and R6.6.

Classification:

```text
PASS
```

### 11.12 Checkpoint C - dashboard evidence

`02_dash_dashboard.png` requires a functional comparative dashboard, not merely a running server.

Visible evidence must include:

```text
Instrument
Benchmark
Lookback
Interval
Instrument return
Benchmark return
Relative performance
Base-100 comparison
```

R6.6 proved that the snapshot and real Plotly figure can supply all of these values.

A real Dash browser capture still requires Dash to be installed in a network-enabled teaching environment.

Classification:

```text
CONTRACT PASS
REAL DASH CAPTURE = EXTERNAL VERIFY
```

### 11.13 Checkpoint C - attributable late-stage PR

The final PR screenshot does not require every student to author a duplicate release PR.

Allowed evidence:

```text
one meaningful attributable PR
from TD09, TD10, TD11 or TD12
```

This prevents artificial duplicate release work while preserving individual traceability.

Classification:

```text
PASS
```

### 11.14 Checkpoint C - reproducibility recovery

The canonical contract now requires a successful clean or freshly prepared run that makes the documented sequence understandable:

```bash
git clone ...
cd esilv-marketpulse-gXX-tYY
python -m pip install -r requirements.txt
python src/main.py
python src/dashboard.py
```

A package-index or platform outage may temporarily produce:

```text
PENDING_EXTERNAL
```

but a failed installation cannot be submitted as successful reproducibility evidence.

A proprietary LIVE provider does not have to work outside its authorized environment.

The documented authorized fallback may be used for the clean-run provider path when appropriate.

TD12 now points to this rule.

Classification:

```text
REMEDIATED
```

Remediation commit:

```text
c33855343905e750b491edc096c4fb221420a2a9
docs: align TD12 reproducibility evidence recovery
```

### 11.15 Shared vs individual screenshot rule

The dry run confirms an important distinction:

```text
application screenshots
may naturally look similar across team members

but

Git contribution screenshots
must remain individually attributable
```

Examples of inherently individual evidence:

```text
Pull Request author
review author
commit author
late-stage PR
```

Examples of potentially similar team-state evidence:

```text
terminal application output
instrument vs benchmark result
final dashboard
reproducible runtime
```

Copying another student's personal contribution screenshot is not valid evidence.

Classification:

```text
PASS
```

### 11.16 Security dry run

The evidence contract was checked against the onboarding and TEAM template privacy rules.

No required checkpoint field needs:

```text
password
API key
GitHub token
SSH private key
Bloomberg credential
cloud credential
payment information
student identifier
personal email address
phone
home address
```

Students are explicitly instructed to inspect screenshots before committing them.

Classification:

```text
PASS
```

### 11.17 R6.7 acceptance criteria

```text
[x] Checkpoint A has exactly 3 required screenshots
[x] Checkpoint B has exactly 4 required screenshots
[x] Checkpoint C has exactly 4 required screenshots
[x] optional advanced screenshot remains optional
[x] all 11 required filenames satisfy the canonical naming rule
[x] each checkpoint directory also requires README.md
[x] README evidence lists can match directory contents exactly
[x] evidence directories are keyed by GitHub username
[x] no sensitive personal field is required
[x] Checkpoint A terminal evidence is producible
[x] Checkpoint A Git history evidence is producible
[x] Checkpoint A fast-forward branch evidence defect was identified
[x] Checkpoint A capture now occurs before branch deletion
[x] fast-forward evidence works with git branch --merged
[x] no artificial merge commit is required
[x] Checkpoint B PR evidence is individually attributable
[x] Checkpoint B review evidence requires another student
[x] Yahoo evidence requires a real remote retrieval
[x] Yahoo outage recovery no longer requires fabricated proof
[x] PENDING_EXTERNAL is limited to genuine external blockers
[x] Checkpoint C final provider may honestly use APPROVED_SAMPLE
[x] APPROVED_SAMPLE cannot be labelled Bloomberg LIVE
[x] Checkpoint C dashboard evidence requires the comparative view
[x] Checkpoint C late-stage PR does not require duplicate release PRs
[x] Checkpoint C reproducibility requires a successful clean run
[x] failed dependency installation cannot count as successful evidence
[x] application-state screenshots may be similar across teammates
[x] personal Git-contribution screenshots must remain individual
[x] screenshot security rules cover credentials and secrets
[ ] actual team-fork Pull Request screenshots captured
[ ] actual different-student review screenshots captured
[ ] actual Yahoo remote screenshot captured
[ ] actual real-Dash browser screenshot captured
[ ] actual clean network-enabled reproducibility screenshot captured
```

R6.7 conclusion:

```text
EVIDENCE CONTRACT PASS
FAST-FORWARD CAPTURE DEFECT REMEDIATED
EXTERNAL OUTAGE RECOVERY REMEDIATED
NO ARTIFICIAL SCREENSHOT REQUIRED
REAL PLATFORM CAPTURES REMAIN
```

R6.7 does not block instructor contingency validation.

## 12. R6.8 - Instructor contingency and provider fallback validation

Status:

```text
DONE
```

Canonical operational reference:

```text
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
```

Validated scenarios:

```text
student environment failure
GitHub access delay or outage
Yahoo provider failure
Bloomberg LIVE unavailable
Dash dependency issue
late student synchronization
merge conflict
missing checkpoint evidence
```

The objective of R6.8 is not to prove that external services are always available.

It is to prove that their unavailability has a safe, honest and teachable recovery path.

### 12.1 Recovery vocabulary

The playbook standardizes these outcomes:

```text
CONTINUE_LOCAL
PAIR_TEMPORARILY
APPROVED_SAMPLE
PENDING_EXTERNAL
ARCHIVE_AND_ALIGN
RESOLVE_AND_VALIDATE
```

This avoids using one generic fallback for unrelated failures.

Classification:

```text
INSPECTED
```

### 12.2 Student environment failure

Existing onboarding already permits temporary pairing when one student's environment is broken.

R6.8 formalizes:

```text
broken individual environment
        |
        +--> pair temporarily
        |
        +--> or use fresh environment
        |
        v
continue learning
        |
        v
restore individual traceability later
```

Temporary pairing does not authorize:

```text
shared GitHub credentials
copied personal evidence
another student's commits presented as personal work
```

R6.6 already proved that the application can be reproduced from a fresh local clone when the required local dependencies are available.

Classification:

```text
INSPECTED + PRIOR EXECUTION REUSED
```

### 12.3 GitHub unavailable - local work then delayed push

A disposable repository executed this sequence with no remote configured:

```bash
git switch -c feature/offline-work
# meaningful change
git add notes.txt
git commit
```

A shared bare remote was created only afterward.

The original local branch was then published:

```bash
git remote add origin <shared-remote>
git push -u origin feature/offline-work
```

Validated invariant:

```text
local feature HEAD
=
remote feature HEAD
```

The work did not need to be recreated or rebased merely because the remote was temporarily unavailable.

Required GitHub PR/review evidence remains external until the actual platform action occurs.

Classification:

```text
EXECUTED
```

### 12.4 Yahoo provider failure

The contingency reuses the already executed R6.5 behaviour:

```text
empty provider result
-> explicit ValueError

Yahoo unavailable
-> local CSV may continue analytics learning

Yahoo screenshot
-> PENDING_EXTERNAL
```

The fallback boundary is explicit:

```text
local CSV
=
teaching continuity

local CSV
!=
Yahoo remote evidence
```

No provider failure is allowed to trigger Yahoo-specific logic inside `analytics.py`.

The current validation environment also directly confirms:

```text
yfinance = unavailable
```

Classification:

```text
EXECUTED / OBSERVED
```

### 12.5 Bloomberg LIVE unavailable

The authorized response is:

```text
LIVE unavailable
        |
        v
instructor approval
        |
        v
APPROVED_SAMPLE
```

R6.6 executed the complete fallback with the remediated full teaching window:

```text
AAPL  = 21 rows
SP500 = 21 rows

normalized expected result
=
42 / 42 exact rows
```

The mode remains labelled:

```text
Bloomberg stage - APPROVED_SAMPLE
```

and never becomes fake LIVE evidence.

Classification:

```text
EXECUTED
```

### 12.6 Dash dependency issue

The validation environment directly reports:

```text
dash = unavailable
plotly = available
```

The recovery contract preserves the architecture:

```text
Dash unavailable
        |
        +--> do not move dashboard logic into main.py
        +--> do not duplicate analytics
        |
        v
validate terminal + snapshot
        |
        v
install Dash later
        |
        v
capture real dashboard evidence
```

R6.6 already proved the upstream snapshot and actual Plotly figure remain valid independently of the missing Dash package.

The real Dash screenshot remains:

```text
PENDING_EXTERNAL
```

until Dash is genuinely installed and running.

Classification:

```text
OBSERVED + PRIOR EXECUTION REUSED
```

### 12.7 Late student synchronization

R6.8 executed a shared-remote scenario where:

```text
student local main
!=
new origin/main
```

Before alignment:

```bash
git branch archive/pre-sync
```

Then:

```bash
git fetch origin
git reset --hard origin/main
```

Validated invariants:

```text
archive/pre-sync
=
old local HEAD

new local HEAD
=
origin/main

working tree
=
clean
```

The student history remained recoverable.

The playbook explicitly forbids this reset when:

```text
working tree is dirty
local work is not preserved
authoritative baseline is unclear
```

Classification:

```text
EXECUTED
```

### 12.8 Controlled merge conflict

R6.8 created two incompatible edits to the same tracked line.

Observed merge state:

```text
merge return code != 0
git status -> UU config.txt
```

The final content was chosen deliberately, staged and committed.

After resolution:

```text
working tree = clean
chosen final content preserved
```

The recovery required no destructive random command and no artificial history rewrite.

Classification:

```text
EXECUTED
```

### 12.9 Missing checkpoint evidence

The playbook distinguishes two fundamentally different cases.

External blocker:

```text
Yahoo unavailable
GitHub unavailable
package index unavailable
        |
        v
PENDING_EXTERNAL
```

Locally controllable omission:

```text
forgotten screenshot
wrong filename
capture not performed
        |
        v
recapture real current state
or instructor live micro-validation
```

A locally forgotten screenshot is not reclassified as an external outage.

If the historical state no longer exists, the student must not rewrite Git history merely to manufacture a prettier image.

Classification:

```text
INSPECTED
```

### 12.10 Evidence security stop condition

The playbook defines hard stop conditions for:

```text
secret visible in Git or evidence
wrong origin before destructive synchronization
dirty working tree before reset --hard
provider mode mislabelling
fabricated remote evidence
analytics rewrite intended only to hide provider failure
unpreserved local work before destructive action
```

A screenshot containing a secret must be retaken or sanitized from real state before submission.

If a credential has already entered Git history, normal checkpoint work stops and the institution's credential-rotation or incident procedure takes precedence.

Classification:

```text
INSPECTED
```

### 12.11 Centralization

The new operational guide is:

```text
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
```

Cross-references were added to:

```text
docs/03_GITHUB_TEAM_WORKFLOW.md
docs/09_YAHOO_FINANCE_INSTRUCTOR_REFERENCE.md
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
```

Relevant canonical sources remain:

```text
docs/01_STUDENT_ONBOARDING.md
docs/04_CHECKPOINTS_AND_EVIDENCE.md
docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md
docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
```

The playbook coordinates those documents rather than redefining their normal teaching contracts.

### 12.12 R6.8 acceptance criteria

```text
[x] student environment failure has a non-blocking recovery path
[x] temporary pairing does not replace individual evidence
[x] fresh environment is an authorized recovery option
[x] GitHub outage does not require discarding local work
[x] local feature commit can be pushed after remote recovery
[x] delayed remote push preserves the original feature HEAD
[x] missing GitHub UI evidence remains external rather than fabricated
[x] Yahoo outage is separated from analytics correctness
[x] local CSV may preserve analytics learning during Yahoo outage
[x] local CSV cannot substitute for Yahoo remote evidence
[x] empty Yahoo provider output fails explicitly
[x] Bloomberg LIVE outage has an authorized APPROVED_SAMPLE path
[x] Bloomberg fallback keeps canonical AAPL and SP500
[x] Bloomberg fallback covers the full one-month teaching window
[x] APPROVED_SAMPLE remains visibly different from LIVE
[x] Dash absence does not justify presentation or analytics duplication
[x] terminal and snapshot remain valid recovery anchors
[x] real Dash evidence remains pending until real Dash runs
[x] late synchronization preserves old local history before alignment
[x] controlled reset ends with HEAD = origin/main
[x] merge conflict produces a visible conflict state
[x] merge conflict can be resolved by deliberate human choice
[x] locally forgotten evidence is not PENDING_EXTERNAL
[x] external evidence blockers may use PENDING_EXTERNAL
[x] missing historical screenshot does not justify Git-history fabrication
[x] secret exposure is a hard stop condition
[x] recovery outcomes are centralized in one instructor playbook
[x] Yahoo reference links to the playbook
[x] Bloomberg reference links to the playbook
[x] Git workflow links to the playbook
[x] no recovery path requires fabricated provider output
[x] no recovery path requires fabricated GitHub review activity
```

R6.8 conclusion:

```text
PASS

8 / 8 contingency scenarios have an explicit recovery path.
Executable Git recovery scenarios were run successfully.
Provider and dependency outage paths preserve honest evidence semantics.
No contingency requires fabricated success.
```

## 13. R6.9 - Teaching baseline freeze

Status:

```text
DONE
```

Release manifest:

```text
docs/16_TEACHING_BASELINE_RELEASE.md
```

### 13.1 Freeze decision

Final decision:

```text
TEACHING BASELINE READY
WITH EXTERNAL PRE-CLASS CHECKS
```

The baseline is frozen because no unresolved repository-side or pedagogical blocker remains.

The remaining verification items depend on real external environments and have been converted into explicit pre-class gates rather than false completion claims.

### 13.2 Review-lot disposition

The remaining REVIEW lots are accepted as follows:

```text
R6.2
-> ACCEPTED - Pre-class Gate A
-> real student-environment clone/fork

R6.4
-> ACCEPTED - Pre-class Gate B
-> real team-fork PR/review UI

R6.5
-> ACCEPTED - Pre-class Gate C
-> yfinance install + Yahoo LIVE

R6.6
-> ACCEPTED - Gates B/C/D/E/F as applicable
-> real external packages, provider environment and final reproduction

R6.7
-> ACCEPTED - Gates B/C/E/F for real captures
-> real platform screenshots
```

None of these accepted lots contains an unresolved `NOT TESTED` repository contract.

### 13.3 Global repository gate

Final inspection confirmed:

```text
canonical readiness files checked = 11
missing canonical readiness files = 0
TD01-TD12 present in lab index = 12 / 12
repository visibility = public
default branch = main
repository archived = false
HTTPS clone endpoint = published
```

The only `NOT TESTED` occurrence in this R6 document is the validation-classification definition itself.

### 13.4 Freeze-time corrections

The final scan found and corrected two stale closure traces:

```text
docs/05_TARGET_REPOSITORY_STRUCTURE.md
=
starter structure now lists readiness/reference docs 09 through 16

docs/labs/TD12_INTEGRATION_AND_RELEASE.md
=
removed stale claim that readiness validation is still the next remediation stage
```

The root README now exposes the baseline release status and links to the R6 operational documents.

### 13.5 Pre-class gates

The release manifest defines:

```text
Gate A - bootstrap / clone
Gate B - GitHub collaboration
Gate C - Yahoo
Gate D - Bloomberg mode
Gate E - Dash
Gate F - final clean reproduction
```

These gates verify mutable external conditions close to the session where they matter.

A failed gate uses the recovery playbook.

It does not authorize fabricated success.

### 13.6 R6.9 acceptance criteria

```text
[x] R6.1 starter runtime is DONE
[x] R6.2 local bootstrap contract is accepted with external Gate A
[x] R6.3 Wave 1 is DONE
[x] R6.4 Git mechanics are accepted with external Gate B
[x] R6.5 analytics/provider contract is accepted with external Gate C
[x] R6.6 end-to-end application contract is accepted with external Gates
[x] R6.7 evidence contract is accepted with real-capture Gates
[x] R6.8 contingency validation is DONE
[x] all 12 TDs remain indexed
[x] three checkpoint contracts remain defined
[x] current repository is public on main
[x] no canonical readiness reference is missing
[x] no unresolved repository-side NOT TESTED item remains
[x] external checks are centralized as pre-class gates
[x] recovery paths are centralized
[x] stale TD12 readiness wording is removed
[x] starter structure reflects readiness documents
[x] README exposes baseline status
[x] release manifest exists
[x] baseline verdict is explicit
```

R6.9 conclusion:

```text
PASS

TEACHING BASELINE READY
WITH EXTERNAL PRE-CLASS CHECKS
```

R6 is closed.

## 14. Status board

| Lot | Scope | Status |
|---|---|---|
| R6.1 | Starter runtime baseline | DONE |
| R6.2 | Clean-clone and student bootstrap portability | ACCEPTED - PRE-CLASS CHECKS |
| R6.3 | Wave 1 dry run | DONE |
| R6.4 | Wave 2 dry run | ACCEPTED - PRE-CLASS CHECKS |
| R6.5 | Wave 3 dry run | ACCEPTED - PRE-CLASS CHECKS |
| R6.6 | Wave 4 dry run | ACCEPTED - PRE-CLASS CHECKS |
| R6.7 | Checkpoint and evidence dry run | ACCEPTED - PRE-CLASS CHECKS |
| R6.8 | Instructor contingency and provider fallback validation | DONE |
| R6.9 | Teaching baseline freeze | DONE |
