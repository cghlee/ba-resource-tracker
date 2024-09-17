import os, json

def data_import() -> dict:
    if os.path.exists('data.json'):
        print('"data.json" file found.')

        with open('data.json', 'r', encoding="UTF-8") as file:
            dict_init = json.load(file)

        print('Loaded "data.json" file.')
    else:
        print('"data.json" file not found.')

        with open('data.json', 'w') as file:
            file.write("{}")
            file.close
        dict_init = {}

        print('"data.json" file was created.')

    return dict_init

def data_export(dict_cur: dict):
    data_final = json.dumps(dict_cur)

    print('Saving updated data to "data.json"...')
    with open('data.json', 'w', encoding="UTF-8") as file:
        file.write(data_final)
        file.close

    print('Save successful.')
