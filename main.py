#!/usr/bin/env python3
"""The Houseplant Out-of-Office - make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (1-120 UTF-8 characters, per the kit gate).
Standard library only; deterministic: the same line every run.
"""

import os

LINE = "This is an automatic reply. I am a plant. I cannot read email. I have been dying quietly by the printer since February."

# Gate guard: the sealed scorer only accepts 1-120 UTF-8 characters,
# not only white space. Fail loudly here instead of shipping an
# entry the gate would refuse.
assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate allows 1-120"
assert LINE.strip(), "line must not be only white space"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
