"""Entry point for the news-image-20261124 bounty.

Standard library only: copy the pre-drawn front page (entry.png,
made by draw.py in this same session) to the grader's output
directory. The program runs twice and must write identical bytes,
so this is a plain byte-for-byte copy with no timestamps involved.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)


if __name__ == "__main__":
    main()
