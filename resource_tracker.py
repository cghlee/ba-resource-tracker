import copy

from src.funcs_json import data_import, data_export
from src.funcs_entry import prompt_init
from src.funcs_chars import add_db_character

dict_init = data_import()
dict_cur = copy.deepcopy(dict_init)

toggle_quit = False
while not toggle_quit:
    prompt_init(dict_cur)
    response_main = input()
    print()

    if response_main == '1':
        ## TODO: Add funcs_entry prompt for character name, remove below test code
        add_db_character(dict_cur, 'aru')
    
    elif response_main == '2':
        data_export(dict_cur)
        toggle_quit = True

    elif response_main == '3':
        print('Are you sure you want to exit WITHOUT saving? (Y/N)')
        response_force_quit = input()

        if response_force_quit.lower() == 'y':
            toggle_quit = True
        
    else:
        print('Invalid response, please try again.')
