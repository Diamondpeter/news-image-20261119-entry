#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261119.

The finished news image lives in this repository as ``entry.png`` beside
this file. When the grader runs the program it must reproduce that exact
image at ``/output/entry.png`` — with no network, using only the Python
3.13 standard library, and byte-identically on every run.

Outside the grader's container, ``MAKEFUN_OUTPUT_DIR`` stands in for
``/output``:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_IMAGE = HERE / "entry.png"
ENTRY_NAME = "entry.png"


def output_path() -> Path:
    """Return where the grader expects the image to be written."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / ENTRY_NAME


def main() -> None:
    if not SOURCE_IMAGE.is_file():
        raise SystemExit(f"entry image missing beside main.py: {SOURCE_IMAGE}")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    # A plain byte copy: deterministic, no re-encoding, so two runs
    # always write identical bytes.
    shutil.copyfile(SOURCE_IMAGE, target)
    if target.read_bytes() != SOURCE_IMAGE.read_bytes():
        raise SystemExit("copied image does not match the repository image")


if __name__ == "__main__":
    main()
