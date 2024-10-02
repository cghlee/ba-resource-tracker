import os, json

from .data_shared import filename_db, filename_tracked

def data_import(filename: str) -> dict:
    if os.path.exists(filename):
        print(f'"{filename}" file found.')

        with open(filename, 'r', encoding="UTF-8") as file:
            dict_init = json.load(file)

        print(f'Loaded "{filename}" file.')
    else:
        print(f'"{filename}" file not found.')

        with open(filename, 'w') as file:
            file.write("{}")
            file.close
        dict_init = {}

        print(f'"{filename}" file was created.')

    return dict_init

def data_export(dict_db_curr: dict, dict_tracked_curr: dict):
    data_db_final = json.dumps(dict_db_curr)
    data_tracked_final = json.dumps(dict_tracked_curr)

    print(f'Saving updated database information to "{filename_db}"...')
    with open(filename_db, 'w', encoding="UTF-8") as file_db:
        file_db.write(data_db_final)
        file_db.close
    
    print(f'Saving updated character tracking information to "{filename_tracked}"...')
    with open(filename_tracked, 'w', encoding="UTF-8") as file_tracked:
        file_tracked.write(data_tracked_final)
        file_tracked.close

    print('\nSave successful.')
