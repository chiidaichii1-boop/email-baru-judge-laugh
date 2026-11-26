"""Make the Judge Laugh in One Line.

Writes exactly one funny line to <MAKEFUN_OUTPUT_DIR>/entry.txt
(fallback /output). The line is a self-contained one-liner: a dating
profile setup that the reader expects to end in romance, broken at
the last word by a very 2026 misunderstanding.

The line is 89 characters, well under the 200-character gate, and is
written with no trailing newline so the file holds exactly the line.
"""

import os

LINE = "My dating profile says I'm mysterious; my only match asked if I was a bot selling crypto."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
