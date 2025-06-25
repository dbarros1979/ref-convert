import pandas as pd
from tqdm import tqdm
from utils.ris_writer import write_ris_entry

def convert(input_file, output_file):
    df = pd.read_csv(input_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Converting CSV to RIS"):
            entry = {
                'TY': 'JOUR',
                'TI': row.get('title', ''),
                'AU': row.get('author', ''),
                'PY': str(row.get('year', '')),
                'JO': row.get('journal', ''),
                'VL': str(row.get('volume', '')),
                'IS': str(row.get('issue', '')),
                'SP': str(row.get('pages', '')),
                'DO': row.get('doi', ''),
            }
            write_ris_entry(entry, f)
