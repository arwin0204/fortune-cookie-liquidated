#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a crypto trader who has just been
liquidated to /output/entry.txt (or the directory given as argv[1]).

The entry is a fixed, deterministic string: no randomness, no clock,
no network, no input files. Running the program twice produces
byte-identical output.
"""

import os
import sys

ENTRY = (
    "You lost the trade, not the trader \u2014 "
    "the market keeps the coins, you keep the comeback."
)

MAX_CHARS = 160
MAX_WORDS = 20


def check_entry(text: str) -> None:
    """Gate self-check: 1-160 chars, not only whitespace, at most 20 words."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    words = stripped.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"entry is {len(words)} words, over the {MAX_WORDS} limit")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")


def main() -> int:
    check_entry(ENTRY)
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
