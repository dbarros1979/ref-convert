import bibtexparser
from tqdm import tqdm
from utils.ris_writer import write_ris_entry

def convert(input_file, output_file):
    with open(input_file, encoding='utf-8') as bibfile:
        bib_database = bibtexparser.load(bibfile)

    entries = bib_database.entries

    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in tqdm(entries, desc="Converting BibTeX to RIS"):
            ris_entry = {
                'TY': 'JOUR',
                'TI': entry.get('title', ''),
                'AU': entry.get('author', ''),
                'PY': entry.get('year', ''),
                'JO': entry.get('journal', ''),
                'VL': entry.get('volume', ''),
                'IS': entry.get('number', ''),
                'SP': entry.get('pages', ''),
                'DO': entry.get('doi', ''),
            }
            write_ris_entry(ris_entry, f)
