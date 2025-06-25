import pandas as pd
import csv
from tqdm import tqdm
from utils.ris_writer import write_ris_entry


def detect_delimiter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        sample = f.read(2048)
        sniffer = csv.Sniffer()
        try:
            return sniffer.sniff(sample).delimiter
        except csv.Error:
            # fallback: assume que é ponto e vírgula
            return ';'


def convert(input_file, output_file):
    delimiter = detect_delimiter(input_file)
    df = pd.read_csv(input_file, sep=delimiter)

    with open(output_file, 'w', encoding='utf-8') as f:
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Converting CSV to RIS"):
            content_type = str(row.get('Content Type', '')).strip().lower()
            if 'article' in content_type:
                ty = 'JOUR'
            elif 'book' in content_type:
                ty = 'BOOK'
            else:
                ty = 'GEN'

            entry = {
                'TY': ty,
                'TI': row.get('Item Title', ''),
                'JO': row.get('Publication Title', ''),
                'T2': row.get('Book Series Title', ''),
                'VL': str(row.get('Journal Volume', '')),
                'IS': str(row.get('Journal Issue', '')),
                'DO': row.get('Item DOI', ''),
                'AU': row.get('Authors', ''),
                'PY': str(row.get('Publication Year', '')),
                'UR': row.get('URL', ''),
            }

            write_ris_entry(entry, f)
