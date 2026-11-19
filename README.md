# DATA2010 Final Project Group 3

## Installation

Please install `uv` (follow instructions at <https://docs.astral.sh/uv/getting-started/installation>).

To create the virtual environment and install the libraries (i.e. when first cloning this repo), run `uv sync`.
Use the virtual environment (located in `.venv`, available after `uv sync`) in this library when developing/running the notebook.

## Committing

`ruff` and `nbdev` are installed to clean and format the Jupyter notebook before committing.

Stage changed files before committing.
The commit may fail; this is because the pre-commit hooks modified the notebook. You should stage the modifications made by the hooks and then commit again.

## Dataset

In order to ensure consistency and reproducibility, **PLEASE INSTALL AND USE THE TOOLING IN [Installation](#installation)**.

## Libraries

You may install additional libraries using `uv` (i.e. `uv add <library name>`) and import them as normal in the notebook.

Further information about `uv` may be found at <https://docs.astral.sh/uv>.

## Notes

A GPU (I used a RTX 5060 Laptop (8GB VRAM)) is required to run the BERTopic training.

Embeddings and tokenization are cached in `/cache`. Remember to clear this folder if you change the embedding/tokenization logic.
