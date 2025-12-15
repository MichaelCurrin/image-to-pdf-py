"""
Tests for the img2pdf CLI module.
"""

from pathlib import Path
from typing import Iterable

import pytest
from PIL import Image

# Note using the package name otherwise mypy complains about two __main__ paths.
from __main__ import load_images, resolve_paths, save_pdf


def _create_image(path: Path, color: str = "red") -> None:
    """
    Create a simple RGB image file for testing.

    :param path: Destination image path.
    :param color: Fill color name for the image.
    """

    image = Image.new("RGB", (10, 10), color=color)
    image.save(path)


def _assert_paths_equal(paths: Iterable[Path], expected: Iterable[Path]) -> None:
    """
    Assert that two path sequences are equal as lists.

    :param paths: Actual paths.
    :param expected: Expected paths.
    """

    assert list(paths) == list(expected)


def test_resolve_paths_from_directory_sorted(tmp_path: Path) -> None:
    """
    Resolve image paths from a directory and ensure they are sorted.
    """

    first = tmp_path / "b.png"
    second = tmp_path / "a.jpg"
    _create_image(first)
    _create_image(second)

    resolved = resolve_paths(dir_path=tmp_path, image_paths=None)

    # Directory listing is sorted lexicographically by file name.
    _assert_paths_equal(resolved, [second, first])


def test_resolve_paths_from_explicit_list(tmp_path: Path) -> None:
    """
    Resolve paths from explicit image list.
    """

    first = tmp_path / "one.png"
    second = tmp_path / "two.jpg"
    _create_image(first)
    _create_image(second)

    resolved = resolve_paths(dir_path=None, image_paths=[first, second])

    _assert_paths_equal(resolved, [first, second])


def test_resolve_paths_raises_for_missing_directory(tmp_path: Path) -> None:
    """
    Raise ValueError when directory does not exist.
    """

    missing_dir = tmp_path / "missing"

    with pytest.raises(ValueError) as captured:
        resolve_paths(dir_path=missing_dir, image_paths=None)

    assert "Directory does not exist" in str(captured.value)


def test_resolve_paths_raises_for_no_images_in_directory(tmp_path: Path) -> None:
    """
    Raise ValueError when directory has no supported image files.
    """

    empty_dir = tmp_path / "images"
    empty_dir.mkdir()

    with pytest.raises(ValueError) as captured:
        resolve_paths(dir_path=empty_dir, image_paths=None)

    assert "No supported images found" in str(captured.value)


def test_resolve_paths_raises_for_missing_image_path(tmp_path: Path) -> None:
    """
    Raise ValueError when an explicit image path does not exist.
    """

    missing_image = tmp_path / "missing.png"

    with pytest.raises(ValueError) as captured:
        resolve_paths(dir_path=None, image_paths=[missing_image])

    assert "Image path does not exist" in str(captured.value)


def test_resolve_paths_raises_when_no_sources() -> None:
    """
    Raise ValueError when neither directory nor image_paths are supplied.
    """

    with pytest.raises(ValueError) as captured:
        resolve_paths(dir_path=None, image_paths=None)

    assert "At least one image path must be provided" in str(captured.value)


def test_load_images_converts_to_rgb(tmp_path: Path) -> None:
    """
    Load images and convert non-RGB modes to RGB.
    """

    path = tmp_path / "img.png"
    # Create an image in a non-RGB mode to exercise conversion.
    image = Image.new("L", (5, 5))
    image.save(path)

    loaded = load_images([path])

    assert len(loaded) == 1
    assert loaded[0].mode == "RGB"


def test_save_pdf_creates_file(tmp_path: Path) -> None:
    """
    Save images into a single PDF file.
    """

    image_path = tmp_path / "img.png"
    _create_image(image_path)

    images = load_images([image_path])
    output_path = tmp_path / "output" / "combined.pdf"

    save_pdf(images, output_path)

    assert output_path.is_file()
