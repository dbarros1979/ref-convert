def write_ris_entry(entry, file_handle):
    for key, value in entry.items():
        if key and value and str(value).strip() != 'nan':
            if key == 'AU':
                for author in str(value).split(';'):
                    file_handle.write(f"{key}  - {author.strip()}\n")
            else:
                file_handle.write(f"{key}  - {str(value).strip()}\n")
    file_handle.write("ER  -\n\n")
