import argparse
from tqdm import tqdm
import os
from converters import csv_to_ris, bibtex_to_ris

def main():
    parser = argparse.ArgumentParser(description="Convert bibliographic files between formats.")
    parser.add_argument('--input-format', required=True, help='Input format (csv or bibtex)')
    parser.add_argument('--output-format', required=True, help='Output format (only ris supported now)')
    parser.add_argument('--input-file', required=True, help='Path to input file')

    args = parser.parse_args()

    input_format = args.input_format.lower()
    output_format = args.output_format.lower()
    input_file = args.input_file
    output_file = os.path.splitext(input_file)[0] + '.' + output_format

    if input_format == 'csv' and output_format == 'ris':
        csv_to_ris.convert(input_file, output_file)
    elif input_format == 'bibtex' and output_format == 'ris':
        bibtex_to_ris.convert(input_file, output_file)
    else:
        print("❌ Unsupported format conversion.")
        return

    print(f"\n✅ Conversion complete. Output file: {output_file}")

if __name__ == "__main__":
    main()
