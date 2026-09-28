"""Build the printable PDF books into dist/pdf (needs: uv sync --group pdf)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from atlas.pdf import main

if __name__ == "__main__":
    raise SystemExit(main())
