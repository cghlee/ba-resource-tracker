import copy

from src import funcs_json as fj

def prompt_main(dict_cur):
    print(f'\n{len(dict_cur)} characters currently tracked (X in database)\n'
          'Please select an option:\n'
          '\t1 - Track a new character\n'
          '\t2 - Save and exit\n'
          '\t3 - Exit without saving')

dict_init = fj.data_import()
dict_cur = copy.deepcopy(dict_init)

toggle_quit = False
while not toggle_quit:
    prompt_main(dict_cur)
    response_main = input()
    print()

    if response_main == '1':
        print('Response 1')
        ## Eventually link to funcs_chars.py
    
    elif response_main == '2':
        fj.data_export(dict_cur)
        toggle_quit = True

    elif response_main == '3':
        print('Are you sure you want to exit WITHOUT saving? (Y/N)')
        response_force_quit = input()

        if response_force_quit.lower() == 'y':
            toggle_quit = True
        
    else:
        print('Invalid response, please try again.')
