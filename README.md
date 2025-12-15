# Combine Images as a PDF
> Basic Python CLI tool to combine image files as a PDF file

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/image-to-pdf-py?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/image-to-pdf-py/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Python version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMichaelCurrin%2Fimage-to-pdf-py%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=project.requires-python&label=python&logo=python&logoColor=white)](https://python.org)
[![dependency - poetry](https://img.shields.io/badge/poetry-2.x-blue)](https://pypi.org/project/poetry)


## Sample

```sh
# Convert all images in a directory:
img2pdf --dir my_images out.pdf

# Convert specific image paths:
img2pdf --path abc.png def.jpg out.pdf
```

## Usage

Install directly from GitHub with pip, then invoke the script:

```sh
pip install git+https://github.com/MichaelCurrin/image-to-pdf-py

img2pdf -h
```

Alternatively, run using [pipx](https://pypa.github.io/pipx/) without installing globally:

```sh
pipx install git+https://github.com/MichaelCurrin/image-to-pdf-py

img2pdf -h
```

Remove:

```sh
pipx uninstall img2pdf
```

## Development

### System dependencies

- Install Python - see `requires-python` in [pyproject.toml](/pyproject.toml).
- Install Poetry - follow Installation on the [Poetry docs](https://python-poetry.org/docs/).

### Installation

1. Clone the project.
1. Navigate to it.
1. Install dependencies:
   ```sh
   poetry install
   ```

### Usage

Run the script:
```sh
poetry run img2pdf -h
```

Format:

```sh
poetry run black .
poetry run isort .
```

## License

Licenses under [MIT](/LICENSE).
