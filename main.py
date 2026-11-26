"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username (at most 30 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``) and prints
it to stdout. Deterministic: no randomness, no network, no input. The file
holds exactly the username, with no trailing newline, so the gate's
character count equals len(LINE).

Judge criteria, most important first (RULES.txt):
1. Is a real make.fun username, the entrant's own handle sent as one word.
   The handle is "lycann", confirmed from the account's own API key record.
   2. Raises a smile on the first read, without needing to be explained.
   3. Sticks in the mind after one look, a name with a bit of character.
   4. Is a single word, with no spaces, no padding and no gloss tacked on.
   5. Sounds like a handle its owner would happily wear.

The entry is the handle itself: there is nothing to invent — the bounty
asks for the entrant's own username and nothing else, so any other word
would fail criterion 1 outright.
"""

import os
import sys

LINE = 'lycann'

MAX_CHARS = 30


def validate_entry() -> None:
    """Refuse an empty or over-long entry (gate 1-MAX_CHARS)."""
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        print(f"entry invalid: {len(LINE)} chars", file=sys.stderr)
        raise SystemExit(1)


def write_entry() -> str:
    """Write LINE to the output entry file and return its path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return path


def main() -> int:
    validate_entry()
    write_entry()
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
