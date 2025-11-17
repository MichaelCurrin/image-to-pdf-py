# Combine Images as a PDF
> Basic Python CLI tool to combine image files as a PDF file

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/image-to-pdf-py?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/image-to-pdf-py/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python-blue?logo=python&logoColor=white)](https://python.org "Go to Python website")
[![dependency - poetry](https://img.shields.io/badge/poetry-2.x-blue)](https://pypi.org/project/poetry)


## Sample

```sh
# From a directory.
img2pdf --dir my_images out.pdf

# From specific image paths.
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
pipx install git+https://github.com/MichaelCurrin/image-to-pdf-py \
img2pdf -h
```

Remove:

```sh
pipx uninstall img2pdf
```

## Development

### Installation

1. Install Poetry - follow Installation on the [Poetry docs](https://python-poetry.org/docs/).
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
