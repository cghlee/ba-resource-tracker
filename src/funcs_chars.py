from .funcs_artifs import prompt_artifs_confirm
from .funcs_br import prompt_br_confirm
from .funcs_tn import prompt_tn_confirm

def prompt_affil_confirm(vars_char: dict, name: str) -> dict:
    affils_total = [
        'hyakkiyako',
        'red winter',
        'trinity',
        'gehenna',
        'abydos',
        'millennium',
        'arius',
        'shanhaijing',
        'valkyrie'
    ]

    toggle_selected_affils = False
    while not toggle_selected_affils:
        sorted_affils = sorted(affils_total)
        range_affils = range(len(sorted_affils))

        print(f"Select the affiliation of {name.title()}:")
        for i in range_affils:
            print(f'\t{i+1} - {sorted_affils[i].title()}')
        response_affils = input(f'Affiliation selection: ')

        try:
            if (int(response_affils) - 1) in range_affils:
                selected_affil = sorted_affils[int(response_affils) - 1]

                print(f'\nAffiliation selected: {selected_affil.title()}')
                confirmation_affils = input('Is this correct? (Y/N)\n').lower()

                if confirmation_affils == 'y':
                    vars_char['affiliation'] = selected_affil
                    toggle_selected_affils = True
                elif confirmation_affils == 'n':
                    print('\nSelection was incorrect - please try again.\n')
                else:
                    print('\nInvalid response, please try again.\n')
            else:
                print('\nInvalid response, please try again.\n')
        except ValueError:
            print('\nInvalid response, please try again.\n')
        
    print('\nAffiliation successfully assigned.\n')
    return vars_char

def add_db_character(dict_db_curr: dict, name: str) -> dict:
    vars_char = {}

    vars_char_affil = prompt_affil_confirm(vars_char, name)

    vars_char_artifs = prompt_artifs_confirm(vars_char_affil)
    
    vars_char_br = prompt_br_confirm(vars_char_artifs)

    vars_char_tn = prompt_tn_confirm(vars_char_br)

    dict_db_curr[name] = vars_char_tn
    return dict_db_curr
