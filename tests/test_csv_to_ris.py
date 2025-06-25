import os
from converters import csv_to_ris


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


def test_csv_to_ris_conversion(tmp_path):
    input_file = os.path.join(os.path.dirname(__file__), 'data', 'SpringNature-SearchResults.csv')
    expected_file = os.path.join(os.path.dirname(__file__), 'data', 'SpringNature-SearchResults.ris')
    output_file = tmp_path / "output.ris"

    # Executa a conversão
    csv_to_ris.convert(input_file, str(output_file))

    # Lê os arquivos
    result = read_file(output_file)
    expected = read_file(expected_file)

    # Compara os arquivos normalizados (ordem de campos ignorada)
    assert normalize_ris(result) == normalize_ris(expected), "CSV to RIS conversion did not match expected output."
