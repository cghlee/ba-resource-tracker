from functions_mats import prompt_mats

def add_character(dict_curr: dict, name: str) -> dict:
    if name.lower() not in dict_curr:
        variables_char = {}

        ## Ask for character's affiliation

        ## Compartmentalise code to functions file?
            ## variables_char as input argument, also as output
        toggle_confirmed_mats = False
        while not toggle_confirmed_mats:
            mats_primary = prompt_mats(1)
            print()
            mats_secondary = prompt_mats(2)

            print('\nPrimary material:', mats_primary.title())
            print(f'Secondary material: {mats_secondary.title()}\n')
            
            response_mats_confirm = input('Are the above selections correct? (Y/N)\n')
            if response_mats_confirm.lower() == 'y':
                variables_char['mats_primary'] = mats_primary
                variables_char['mats_secondary'] = mats_secondary

                toggle_confirmed_mats = True
            elif response_mats_confirm.lower() == 'n':
                print()
            else:
                print('\nInvalid response, please try again.\n')
        
        ## Create prompt interface to define number of materials needed per level
            ## Blu-ray requirements for level 2, 3, 4, 5
            ## Tech Note requirements for levels 4, 5, 6, 7, 8, 9
            ## Hardcoded prompts per level, per type of material?

    else:
        print(f'{name.title()} is already being tracked.')
