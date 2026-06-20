from __future__ import annotations

import argparse
from pathlib import Path

import fitz


DEFAULT_PDF = Path(
    "referencesBook"
    "/Git for Humans (David Demaree) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
)

# Page numbers are 1-based. Rectangles are PDF points and crop only figures that
# are actually referenced by the tutorial text.
ASSETS = {
    "git-for-humans-version-copies.png": {
        "page": 16,
        "rect": (74, 84, 538, 484),
    },
    "git-for-humans-hub-model.png": {
        "page": 81,
        "rect": (74, 274, 538, 640),
    },
}


def extract_assets(pdf_path: Path, out_dir: Path, scale: float) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    out_dir.mkdir(parents=True, exist_ok=True)

    with fitz.open(pdf_path) as doc:
        for filename, spec in ASSETS.items():
            page = doc[spec["page"] - 1]
            rect = fitz.Rect(*spec["rect"])
            pix = page.get_pixmap(
                matrix=fitz.Matrix(scale, scale),
                clip=rect,
                alpha=False,
            )
            target = out_dir / filename
            pix.save(target)
            print(f"wrote {target}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract selected Git for Humans figures used by the Git tutorial."
    )
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--out", type=Path, default=Path("assets"))
    parser.add_argument("--scale", type=float, default=2.2)
    args = parser.parse_args()

    extract_assets(args.pdf, args.out, args.scale)


if __name__ == "__main__":
    main()
