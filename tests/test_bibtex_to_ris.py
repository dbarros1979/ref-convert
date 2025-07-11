import os
from converters import bibtex_to_ris


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()


def normalize_ris(text):
    entries = text.strip().split("ER  -")
    entries = [e.strip().splitlines() for e in entries if e.strip()]
    normalized = []

    for entry in entries:
        lines = sorted([line.strip() for line in entry if line.strip()])
        normalized.append("\n".join(lines) + "\nER  -")

    return normalized


def test_bibtex_to_ris_conversion(tmp_path):
    input_file = os.path.join(os.path.dirname(__file__), 'data', 'acm.bib')
    expected_file = os.path.join(os.path.dirname(__file__), 'data', 'acm.ris')
    output_file = tmp_path / "output.ris"

    bibtex_to_ris.convert(input_file, str(output_file))

    result = read_file(output_file)
    expected = read_file(expected_file)

    assert normalize_ris(result) == normalize_ris(expected), "RIS output doesn't match expected content (normalized)."
