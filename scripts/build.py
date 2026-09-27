"""Regenerate README and docs pages from src/content, or verify them with --check."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from atlas.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
