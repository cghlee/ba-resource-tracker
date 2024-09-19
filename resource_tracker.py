import copy

from src.funcs_json import data_import, data_export
from src.funcs_entry import prompt_init, prompt_name_db_add_confirm, prompt_name_db_edit_confirm
from src.funcs_chars import add_db_character

dict_init = data_import()
print(dict_init)

dict_curr = copy.deepcopy(dict_init)
print(dict_curr)

toggle_quit = False
while not toggle_quit:
    prompt_init(dict_curr)
    response_main = input()
    print()

    if response_main == '1':
        name_db_add_confirmed = prompt_name_db_add_confirm(dict_curr)
        
        if name_db_add_confirmed:
            add_db_character(dict_curr, name_db_add_confirmed)
            print(f'{name_db_add_confirmed.title()} successfully added to database.')

    elif response_main == '2':
        name_db_edit_confirmed = prompt_name_db_edit_confirm(dict_curr)

        if name_db_edit_confirmed:
            del dict_curr[name_db_edit_confirmed]
            
            add_db_character(dict_curr, name_db_edit_confirmed)
            print(f'{name_db_edit_confirmed.title()} successfully edited in database.')

    elif response_main == '3':
        data_export(dict_curr)
        toggle_quit = True

    elif response_main == '4':
        print('Are you sure you want to exit WITHOUT saving? (Y/N)')
        response_force_quit = input()

        if response_force_quit.lower() == 'y':
            toggle_quit = True
        
    else:
        print('Invalid response, please try again.')
