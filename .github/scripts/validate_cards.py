#!/usr/bin/env python3
"""Checks the student cards changed in a pull request.

Runs in GitHub Actions on every pull request (see .github/workflows/check-cards.yml).
You can also run it on your own laptop:  python3 .github/scripts/validate_cards.py
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

FOLDER = "students"
LIMITS = {"name": 40, "github": 39, "city": 30, "emoji": 12, "tagline": 80, "funFact": 140}
USERNAME = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}$")
IN_ACTIONS = os.environ.get("GITHUB_ACTIONS") == "true"


def git(*args):
    result = subprocess.run(["git", *args], capture_output=True, text=True)
    return result.returncode, result.stdout.strip()


def changed_files():
    """Files this pull request adds or modifies (or every card when run locally)."""
    is_merge, _ = git("rev-parse", "--verify", "--quiet", "HEAD^2")
    if is_merge == 0:
        _, out = git("diff", "--name-only", "--diff-filter=AMR", "HEAD^1", "HEAD")
        return [line for line in out.splitlines() if line]
    return [str(p) for p in sorted(Path(FOLDER).glob("*.json"))]


def report(path, message, line=None):
    if IN_ACTIONS:
        where = f"file={path}" + (f",line={line}" if line else "")
        print(f"::error {where}::{message}")
    print(f"  ✗ {path}: {message}")


def check_card(path, author, owner):
    problems = 0
    name = Path(path).name
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        report(path, "Save the file as UTF-8 (in VS Code: bottom-right corner → UTF-8).")
        return 1
    try:
        card = json.loads(text)
    except json.JSONDecodeError as err:
        hint = ""
        if "trailing comma" in err.msg or "Expecting property name" in err.msg or "Expecting value" in err.msg:
            hint = " Look for an extra comma after the LAST line, or a missing quote."
        elif "Expecting ',' delimiter" in err.msg:
            hint = " A comma is missing at the end of the line before this one."
        report(path, f"This is not valid JSON yet: {err.msg} (line {err.lineno}, column {err.colno}).{hint}", err.lineno)
        return 1
    if not isinstance(card, dict):
        report(path, "The file must contain one { ... } object.")
        return 1

    for field, limit in LIMITS.items():
        value = card.get(field)
        if not isinstance(value, str) or not value.strip():
            report(path, f'"{field}" is missing or empty. Copy it from students/_template.json.')
            problems += 1
        elif len(value) > limit:
            report(path, f'"{field}" is {len(value)} characters long. Keep it under {limit}.')
            problems += 1

    for field in card:
        if field not in LIMITS:
            report(path, f'Unknown field "{field}". Allowed fields: {", ".join(LIMITS)}.')
            problems += 1

    name_ok = True
    github = card.get("github", "")
    if isinstance(github, str) and github.strip():
        if not USERNAME.match(github):
            report(path, f'"{github}" is not a valid GitHub username (letters, numbers and single hyphens only).')
            problems += 1
        if name.lower() != f"{github.lower()}.json":
            report(path, f'The file name must match your username: rename it to "{FOLDER}/{github}.json".')
            problems += 1
            name_ok = False

    if name_ok and author and owner and author.lower() != owner.lower():
        if name.lower() != f"{author.lower()}.json":
            report(path, f"You can only add or edit your own card: {FOLDER}/{author}.json")
            problems += 1
    return problems


def main():
    author = os.environ.get("PR_AUTHOR", "")
    owner = os.environ.get("REPO_OWNER", "")
    files = changed_files()
    cards = [f for f in files if f.startswith(f"{FOLDER}/") and f.endswith(".json")
             and not Path(f).name.startswith("_") and Path(f).exists()]
    others = [f for f in files if f not in cards]

    print(f"Cards to check: {len(cards)}")
    for f in others:
        print(f"  • note: this pull request also changes {f}")
        if IN_ACTIONS:
            print(f"::notice file={f}::Student pull requests should only add a file inside {FOLDER}/.")

    problems = sum(check_card(f, author, owner) for f in cards)
    if problems:
        print(f"\n{problems} thing(s) to fix. Fix them, commit, and push again: this check re-runs by itself.")
        sys.exit(1)
    for f in cards:
        print(f"  ✓ {f} looks great")
    print("\nAll good. A human reviewer will take it from here. 🚀")


if __name__ == "__main__":
    main()
