def write_ris_entry(entry, file_handle):
    for key, value in entry.items():
        if key and value:
            if key == 'AU':
                for author in value.split(' and '):
                    file_handle.write(f"{key}  - {author.strip()}\n")
            else:
                file_handle.write(f"{key}  - {value.strip()}\n")
    file_handle.write("ER  -\n\n")
