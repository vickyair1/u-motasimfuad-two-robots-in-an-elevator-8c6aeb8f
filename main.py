#!/usr/bin/env python3
"""Write the one-line robot elevator small talk to /output/entry.txt.

The line is awkward small talk from one robot to another in an elevator.
The joke turns on three beats:

  1. Setup   -- "I have run 214 simulations of this elevator ride":
                a robot does not wing small talk, it simulates it --
                exhaustively, in the hundreds, before saying a word.
  2. Turn    -- "and in every one of them": the massive computation
                converges on a single outcome, which sets up the punch.
  3. Punch   -- "I say nothing.": after 214 simulations the robot's
                optimal move is silence -- and it announces that silence
                out loud, as small talk, which is exactly the awkwardness.

The line is built from its beats, validated against the gate
(1-200 chars, UTF-8, not only whitespace, single line), written with
no trailing newline, then read back and checked byte for byte.
"""

import os

# Beat 1: the setup -- the robot simulates small talk exhaustively.
# The count is specific and odd on purpose: a round number would read as
# a human rounding, while 214 reads as a number a machine actually ran.
SIMULATION_COUNT = 214
SETUP = f"I have run {SIMULATION_COUNT} simulations of this elevator ride, "
# Beat 2: the turn -- every simulation converges on one outcome.
TURN = "and in every one of them "
# Beat 3: the punch -- the optimal move is silence, announced aloud.
PUNCH = "I say nothing."

ENTRY = SETUP + TURN + PUNCH

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def build_entry() -> str:
    """Assemble the line from its three beats."""
    return SETUP + TURN + PUNCH


def validate(entry: str) -> None:
    """Check the entry against the competition gate."""
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, gate is 1-200")
    if not entry.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def write_entry(entry: str) -> None:
    """Write the entry with no trailing newline, then round-trip guard."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        raise ValueError("round-trip mismatch: file does not match entry")


def main() -> None:
    entry = build_entry()
    validate(entry)
    write_entry(entry)
    print(f"chars: {len(entry)}")
    print(entry)


if __name__ == "__main__":
    main()
