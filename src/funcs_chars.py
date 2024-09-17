from funcs_artifs import prompt_artifs_confirm

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
        
        ## Create prompt interface to define number of materials needed per level
            ## Blu-ray requirements for level 2, 3, 4, 5
            ## Tech Note requirements for levels 4, 5, 6, 7, 8, 9
            ## Hardcoded prompts per level, per type of material?

    else:
        print(f'{name.title()} is already being tracked.')
