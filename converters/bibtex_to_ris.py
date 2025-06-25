import bibtexparser
from tqdm import tqdm
from utils.ris_writer import write_ris_entry


def map_bibtex_type_to_ris(bib_type):
    mapping = {
        'article': 'JOUR',
        'book': 'BOOK',
        'inproceedings': 'CONF',
        'conference': 'CONF',
        'phdthesis': 'THES',
        'mastersthesis': 'THES',
        'techreport': 'RPRT',
        'misc': 'GEN',
        'unpublished': 'UNPB',
        'manual': 'MANU'
    }
    return mapping.get(bib_type.lower(), 'GEN')  # fallback para 'GEN'


def convert(input_file, output_file):
    with open(input_file, encoding='utf-8') as bibfile:
        bib_database = bibtexparser.load(bibfile)

    entries = bib_database.entries

    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in tqdm(entries, desc="Converting BibTeX to RIS"):
            ris_entry = {
                'TY': map_bibtex_type_to_ris(entry.get('ENTRYTYPE', 'misc')),
                'TI': entry.get('title', ''),
                'AU': entry.get('author', ''),
                'PY': entry.get('year', ''),
                'JO': entry.get('journal', ''),
                'VL': entry.get('volume', ''),
                'IS': entry.get('number', ''),
                'SP': entry.get('pages', ''),
                'DO': entry.get('doi', ''),
                'AB': entry.get('abstract', ''),
                'PB': entry.get('publisher', ''),
                'SN': entry.get('isbn', ''),
                'UR': entry.get('url', '')
            }
            write_ris_entry(ris_entry, f)
