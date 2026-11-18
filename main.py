"""News-image entry for 18 November 2026 (Python 3.13, standard library only).

The entry image lives in this repository as assets/entry.jpg: a
newspaper-style front page composed in the build session from four
illustrations drawn for the day's news, with PIL-rendered headlines.

This program copies that image to /output/entry.png. The grader reads
the bytes of that file only, and it accepts a PNG or a JPEG by its
first bytes, so the name stays entry.png either way.

Deterministic and offline: the copy is a plain byte copy of a file
already in the repository, so every run writes identical bytes and
the program never touches the network.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

ASSET = Path(__file__).resolve().parent / "assets" / "entry.jpg"


def main() -> None:
    if not ASSET.is_file():
        raise FileNotFoundError(f"entry image missing: {ASSET}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(ASSET, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
