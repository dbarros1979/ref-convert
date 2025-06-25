import os
from converters import bibtex_to_ris

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def test_bibtex_to_ris_conversion(tmp_path):
    input_file = os.path.join(os.path.dirname(__file__), 'data', 'acm.bib')
    expected_file = os.path.join(os.path.dirname(__file__), 'data', 'acm.ris')
    output_file = tmp_path / "output.ris"

    # execute the conversion
    bibtex_to_ris.convert(input_file, str(output_file))

    # read files
    result = read_file(output_file)
    expected = read_file(expected_file)

    # compare ignoring small differences
    assert result.strip() == expected.strip(), "RIS output doesn't match expected content."
