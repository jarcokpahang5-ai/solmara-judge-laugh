"""One-line entry for make.fun: Make the Judge Laugh in One Line.

Writes a single original funny line to /output/entry.txt.
Pure standard library, deterministic, no network, no randomness.
"""

import os


def build_line() -> str:
    subject = "My smart fridge"
    twist = "just emailed me a rent notice"
    payoff = "apparently my leftovers have been subletting the bottom shelf for three months and never paid a cent"
    return f"{subject} {twist} — {payoff}."


def main() -> None:
    line = build_line()
    assert 1 <= len(line) <= 200, f"line length {len(line)} out of range"
    assert "\n" not in line, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
