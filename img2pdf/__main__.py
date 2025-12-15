"""
Combine image files into a single PDF.

Based on https://stackoverflow.com/a/47283224 and extended with Cursor AI.
"""

import argparse
import sys
from pathlib import Path
from typing import Sequence

from PIL import Image
from PIL import ImageFile

IMG_SUFFIXES = (".bmp", ".gif", ".jpeg", ".jpg", ".png", ".tif", ".tiff")


def resolve_paths(
    dir_path: Path | None, image_paths: Sequence[Path] | None
) -> list[Path]:
    """
    Return a list of image paths sourced from a directory or explicit list.

    :param dir_path: Directory containing images or None.
    :param image_paths: Explicit image paths or None.

    :return: Ordered image paths ready to load.
    """

    if dir_path is not None:
        if not dir_path.is_dir():
            raise ValueError(f"Directory does not exist: {dir_path}")

        paths = sorted(
            path
            for path in dir_path.iterdir()
            if path.is_file() and path.suffix.lower() in IMG_SUFFIXES
        )

        if not paths:
            raise ValueError(f"No supported images found in directory: {dir_path}")

        return paths

    if not image_paths:
        raise ValueError("At least one image path must be provided.")

    paths = []
    for path in image_paths:
        if not path.is_file():
            raise ValueError(f"Image path does not exist: {path}")
        paths.append(path)

    return paths


def load_images(paths: Sequence[Path]) -> list[ImageFile.ImageFile | Image.Image]:
    """
    Return opened image objects converted to RGB mode.

    :param paths: Paths to the images to load.

    :returns: Loaded image objects.
    """
    image: ImageFile.ImageFile | Image.Image

    loaded = []
    for path in paths:
        image = Image.open(path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        loaded.append(image)

    return loaded


def save_pdf(images: Sequence[ImageFile.ImageFile | Image.Image], output: Path) -> None:
    """
    Save images into a single PDF file.

    :param images: Image objects to combine.
    :param output: Destination PDF path.
    """

    output.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(
        output,
        format="PDF",
        resolution=100.0,
        save_all=True,
        append_images=list(images[1:]),
    )


def parse_args() -> argparse.Namespace:
    """
    Return parsed command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Combine image files from a directory or explicit paths into a PDF."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-d",
        "--dir",
        metavar="INPUT_DIR",
        type=Path,
        help="Directory containing the images to combine.",
    )
    group.add_argument(
        "-p",
        "--path",
        dest="paths",
        metavar="IMAGE_PATH",
        nargs="+",
        type=Path,
        help="Explicit image file paths to combine.",
    )
    parser.add_argument(
        "output_path",
        metavar="OUTPUT_PATH",
        type=Path,
        help="Destination PDF file path.",
    )
    return parser.parse_args()


def main() -> None:
    """
    Entry point for converting images to a PDF.
    """

    args = parse_args()

    try:
        paths = resolve_paths(args.dir, args.paths)
        images = load_images(paths)
        save_pdf(images, args.output_path)
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        raise SystemExit(1) from err


if __name__ == "__main__":
    main()
