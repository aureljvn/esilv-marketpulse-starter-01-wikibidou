# TD03 - Git Local Workflow - Aurelien Juvin

## What I did
- Checked my Git identity (`git config user.name` / `user.email`).
- Inspected my TD02 changes with `git status` and `git diff`.
- Staged only `src/main.py` with `git add`, checked `git diff --staged`.
- Created the commit and inspected it with `git log --oneline` and `git show HEAD`.

## My commit
- `1d69bb0` feat: add reusable market summary display
- Author: Aurelien JUVIN
- 1 file changed (`src/main.py`), 29 insertions, 18 deletions

## What the diff represents
- New helpers `get_first_close()` and `get_last_close()`.
- New `display_market_summary()` reused for the instrument and the benchmark.
- New "Market configuration" block (period and interval).

## Key concepts
- Working tree: files as they are on disk.
- Staging area: changes selected for the next commit (`git add`).
- Commit: recorded snapshot with author, date, message and identifier.
