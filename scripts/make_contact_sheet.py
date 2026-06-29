#!/usr/bin/env python3
"""Create a contact sheet for AI-director image assets."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()


def build_contact_sheet(asset_dir: Path, output: Path, cols: int) -> None:
    images = sorted(
        p
        for p in asset_dir.iterdir()
        if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
        and p.name[:2].isdigit()
    )
    if not images:
        raise SystemExit(f"No numbered image assets found in {asset_dir}")

    thumb_w, thumb_h = 180, 320
    label_h = 46
    rows = math.ceil(len(images) / cols)
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    font = load_font(14)

    for idx, path in enumerate(images):
        row, col = divmod(idx, cols)
        image = Image.open(path).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.LANCZOS)

        x = col * thumb_w + (thumb_w - image.width) // 2
        y = row * (thumb_h + label_h)
        sheet.paste(image, (x, y))

        label = path.stem
        text_x = col * thumb_w + 8
        draw.text((text_x, y + thumb_h + 5), label[:16], fill=(20, 20, 20), font=font)
        if len(label) > 16:
            draw.text((text_x, y + thumb_h + 25), label[16:32], fill=(20, 20, 20), font=font)

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=95)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a contact sheet for image assets.")
    parser.add_argument("asset_dir", type=Path, help="Directory containing numbered image assets.")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output image path. Defaults to contact-sheet_图片资产总览.png in asset_dir.",
    )
    parser.add_argument("--cols", type=int, default=6, help="Number of columns.")
    args = parser.parse_args()

    output = args.output or args.asset_dir / "contact-sheet_图片资产总览.png"
    build_contact_sheet(args.asset_dir, output, args.cols)
    print(output.resolve())


if __name__ == "__main__":
    main()
