from funcs_artifs import prompt_artifs_confirm
from funcs_br import prompt_br_confirm

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

                print(f'\nAffilication selected: {selected_affil.title()}')
                response_affils_confirm = input('Is this correct? (Y/N)\n')

                if response_affils_confirm.lower() == 'y':
                    vars_char['affiliation'] = selected_affil
                    toggle_selected_affils = True
                elif response_affils_confirm.lower() == 'n':
                    print('\nSelection was incorrect - please try again.\n')
                else:
                    print('\nInvalid response, please try again.\n')
            else:
                print('\nInvalid response, please try again.\n')
        except ValueError:
            print('\nInvalid response, please try again.\n')
        
    print('\nAffiliation successfully assigned.\n')
    return vars_char

def add_character(dict_curr: dict, name: str) -> dict:
    if name.lower() not in dict_curr:
        vars_char = {}

        vars_char_affil = prompt_affil_confirm(vars_char, name)

        vars_char_artifs = prompt_artifs_confirm(vars_char_affil)
        
        vars_char_br = prompt_br_confirm(vars_char_artifs)

        # vars_char_tn = (...)

        ## Create prompt interface to define number of materials needed per level
            ## Tech Note requirements for levels 4, 5, 6, 7, 8, 9

        ## Tech Notes
        # 3 -> 4 = primary T1
        # 4 -> 5 = primary T2, secondary T1
        # 5 -> 6 = primary T2, secondary T1
        # 6 -> 7 = primary T3, secondary T2
        # 7 -> 8 = primary T4, secondary T3
        # 8 -> 9 = primary T4, secondary T3

        print(vars_char_br)
    else:
        print(f'{name.title()} is already being tracked.')

test_dict = {
    'yuuka': {
        'affiliation': 'gehenna',
        'artifs_primary': 'nimrud lens',
        'artifs_secondary': 'antikythera mechanism',
        'br_primary_reqs': [1,  # 1 -> 2
                            2,  # 2 -> 3
                            3,  # 3 -> 4
                            4   # 4 -> 5
                            ],
        'br_secondary_reqs': [1,  # 2 -> 3
                              2,  # 3 -> 4
                              3   # 4 -> 5
                              ],
        'tn_primary_reqs': [1,  # 3 -> 4
                            2,  # 4 -> 5
                            2,  # 5 -> 6
                            3,  # 6 -> 7
                            4,  # 7 -> 8
                            4   # 8 -> 9
                            ],
        'tn_secondary_reqs': [1,  # 4 -> 5
                              1,  # 5 -> 6
                              2,  # 6 -> 7
                              3,  # 7 -> 8
                              3   # 8 -> 9
                              ],
    },
}

add_character(test_dict, 'aru')
