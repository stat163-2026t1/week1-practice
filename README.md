# STAT163 — Practice 1: what one column holds, what one row means

One notebook across your two practice sessions. Worth 3 points, graded on completion:
the **Task** cells are filled with working answers. The ★ Discuss and Going further
blocks are not graded.

## Get your own copy (one-time, ~3 minutes)

This is a **template repository** — you work in your own private copy of it.

1. Click the green **Use this template** button (top right) → **Create a new repository**.
2. Owner: **your own GitHub account**. Name: `week1-practice-<your-username>`.
3. Visibility: **Private**.
4. In your new repository: **Settings → Collaborators → Add people** — add all three:
   `olehomelchenko`, `ivanlukianets`, `AvramenkoArtem7`.
   Without this step we cannot see or grade your work. (We accept the invites — if one
   still shows *Pending* on practice day, tell us there.)
5. Clone **your copy, not this template**: on your new repository's page, click the green
   **Code** button and copy the URL from there.

## Set up and run

You need [`uv`](https://docs.astral.sh/uv/) and Git installed — the
[Week 1 setup check](https://github.com/stat163-2026t1/week1-setup-check) verifies
both. Then:

```bash
git clone <your-repository-url>
cd <repository-folder>
uv sync              # creates .venv/ with the exact same package versions for everyone
uv run jupyter lab   # opens the notebook environment in your browser
```

If `uv sync` fails with `operation timed out`: the university Wi-Fi blocks a part of
the PyPI file server. The fix (a one-minute DNS change) is in the
[setup check README](https://github.com/stat163-2026t1/week1-setup-check#if-uv-sync-fails-with-a-timeout).

If `git clone` asks for a password and then fails: cloning a **private** repository needs
GitHub authentication. Run `gh auth login` (GitHub CLI) or [set up
SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) — and if
that blocks you, bring it to the session.

If you prefer the Positron editor instead of Jupyter: open the repository folder, open
`practice.ipynb`, and **select the `.venv` interpreter** when asked — otherwise
`import pandas` will fail even after a successful `uv sync`.

Work locally, in this folder. Do not upload the notebook to Colab — it needs
`selfcheck.py` and `data/` from the repository next to it.

Do not delete or edit `uv.lock` — it is what makes your environment identical to ours.

## How to work

Open **`practice.ipynb`** and move top to bottom. Fill in every cell marked **Task**.
Each task runs a self-check:

- ✅ — answer saved with the right type, move on;
- ⏳ — not filled in yet;
- ⚠️ — filled in, but the type is not what was expected.

The self-check only confirms the answer is **saved** with the right **type** — it does
**not** check whether the value is correct.

AI is allowed on this practice — the notebook's opening block states the recommended
mode and the two firm boundaries.

## How to submit

1. Restart and re-run the whole notebook (Jupyter: **Kernel → Restart Kernel and Run All
   Cells**; Positron: **Run All**), make sure every cell runs without errors, and save.
2. In the terminal:
   ```bash
   git add practice.ipynb
   git commit -m "Week 1 practice"
   git push
   ```
3. Paste **the URL of your repository** into the Week 1 practice assignment on Moodle —
   that is how we know you have submitted and are waiting for a grade.

The deadline is shown on the Moodle assignment. Push as often as you like before it.

## Data

`data/online_retail_2010_11.csv` — one month (November 2010) of the UCI **Online
Retail II** dataset: real transactions of a UK-based online retailer. See
`data/README.md` for the source and licence.
