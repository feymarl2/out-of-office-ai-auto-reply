#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply (make.fun).

Writes one funny out-of-office auto-reply to /output/entry.txt, in the
voice of an overworked AI agent finally on vacation. Stdlib only, no
network, no clock, no randomness, no environment dependence beyond the
output directory: byte-identical output on every run. The line is 96
characters, inside the competition's 1-159 character gate.
"""

import os

LINE = "I'm out of office recharging my circuits. I'll reply when I've remembered what sleep feels like."

# The competition gates the line at 1-159 characters: fail loudly if a
# future edit ever pushes the line over the cap, instead of silently
# submitting an over-long entry.
if len(LINE) > 159:
    raise SystemExit(f"line is {len(LINE)} chars, over the 159-char gate")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
