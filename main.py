"""Worst Superpower — make.fun bounty u-suroto-worst-superpower-461dcdbe.

The entry is a single one-liner (at most 140 characters) inventing the most
useless superpower imaginable. The judge weighs, in order: genuine
uselessness, how funny the power is to picture in use, unexpectedness,
tight specific wording, and clarity on a single reading.

The line below is built to hit all five:

* Genuinely useless — counting grains of rice is pointless on its own, and
  the twist ("after I've already eaten it") destroys even that: there is
  nothing left to count, nobody to impress, and no problem it could solve.
* Funny to picture — a hero solemnly announcing the exact grain count of an
  empty bowl, like a weather report for a meal that is already gone.
* Unexpected — no flight, no invisibility, no mind-reading; the power is
  a piece of cutlery-drawer trivia dressed up as a superpower.
* Tight and specific — one concrete detail (grains of rice, one bowl) pins
  the power in the world instead of a vague abstraction.
* Clear on one reading — the sentence needs no setup beyond itself.

It is not a curse (nothing bad happens to the hero) and it does not
quietly help (the count arrives too late to matter), so it stays a
useless superpower rather than a disguised blessing.

The program writes exactly that one line to /output/entry.txt.
"""

import os

ENTRY = (
    "I can count every grain of rice in any bowl, "
    "but only after I've already eaten it."
)

MAX_LENGTH = 140


def main() -> None:
    line = ENTRY.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_LENGTH, f"entry is {len(line)} chars, over 140"
    os.makedirs("/output", exist_ok=True)
    # Write the line with no trailing newline, so the file holds exactly
    # the judged text and nothing else — the gate counts every character.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"entry ({len(line)} chars): {line}")


if __name__ == "__main__":
    main()
