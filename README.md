# Ref-Convert 📚

A CLI tool to convert bibliographic references between formats such as CSV, BibTeX, and RIS.

## Usage

```bash
python main.py --input-format bibtex --output-format ris --input-file references.bib
````

## Supported Formats

| From   | To  |
| ------ | --- |
| CSV    | RIS |
| BibTeX | RIS |

## CSV Input Example

| title | author | year | journal | volume | issue | pages | doi |
| ----- | ------ | ---- | ------- | ------ | ----- | ----- | --- |
| ...   | ...    | ...  | ...     | ...    | ...   | ...   | ... |

## Requirements

```bash
pip install -r requirements.txt
```

## License

MIT
