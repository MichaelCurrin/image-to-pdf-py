# Combine Images as a PDF
> Combine one or more image files and convert to a single PDF - a light Python package

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
pipx run --spec git+https://github.com/MichaelCurrin/image-to-pdf-py \
    img2pdf -h
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
