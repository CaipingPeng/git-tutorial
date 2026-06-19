from __future__ import annotations

import argparse
from pathlib import Path

import fitz


DEFAULT_PDF = Path(
    "referencesBook"
    "/Git Apprentice Getting Started with Git Commands  Concepts "
    "(Chris Belanger) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
)

# Page numbers are 1-based. Image indexes count only real image blocks on the page,
# not text blocks. The tiny raywenderlich footer icon is intentionally skipped.
CANDIDATES = {
    "git-apprentice-staging-area-files": (65, 0),
    "git-apprentice-staging-area-selection": (65, 1),
    "git-apprentice-branch-history": (111, 0),
    "git-apprentice-three-way-merge": (114, 0),
    "git-apprentice-fast-forward-merge": (118, 0),
}


def image_blocks(page: fitz.Page) -> list[dict]:
    return [block for block in page.get_text("dict")["blocks"] if block.get("type") == 1]


def extract_assets(pdf_path: Path, out_dir: Path) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    out_dir.mkdir(parents=True, exist_ok=True)

    with fitz.open(pdf_path) as doc:
        for name, (page_number, image_index) in CANDIDATES.items():
            page = doc[page_number - 1]
            blocks = image_blocks(page)
            if image_index >= len(blocks):
                raise IndexError(
                    f"Page {page_number} has {len(blocks)} image blocks; "
                    f"cannot read index {image_index}"
                )

            block = blocks[image_index]
            ext = block.get("ext", "png")
            target = out_dir / f"{name}.{ext}"
            target.write_bytes(block["image"])
            print(f"wrote {target}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract selected Git Apprentice images for the Git tutorial."
    )
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--out", type=Path, default=Path("assets"))
    args = parser.parse_args()

    extract_assets(args.pdf, args.out)


if __name__ == "__main__":
    main()
