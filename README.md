# md-vault-scanner

A small Python CLI tool that scans a Markdown vault and reports:

- file path
- word count
- whether frontmatter appears at the start of the file

## Features

- Recursively finds all .md files in a directory
- Counts words from file text
- Detects frontmatter by checking whether content starts with ---
- Validates scan records with Pydantic
- Prints a clean summary table in the CLI

## Requirements

- Python 3.11+
- Dependencies listed in pyproject.toml

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.

Example:

python -m venv .venv
source .venv/bin/activate
pip install -e .

## Usage

Run the scanner by passing a directory path:

python main.py /path/to/your/vault

Example output includes:

- one row per Markdown file
- total files
- total words

## Project Structure

- main.py: Click command-line entry point
- scanner.py: Markdown model and scan logic
- test_scanner.py: tests for validation and scan behavior

## License

MIT License.
Use a LICENSE file in the repository root containing the standard MIT license text.