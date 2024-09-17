artifs_jfd = [
    'totem pole',
    'ancient battery',
    'golden dress',
    'okiku doll',
    'disco colgante',
    'atlantis medal',
    'roman dodecahedron',
    'quimbaya relic',
    'istanbul rocket',
    'winnipesaukee stone'
]

artifs_non_jfd = [
    'nebra sky disk',
    'phaistos disc',
    'wolfsegg steel',
    'nimrud lens',
    'mandrake essence',
    'rohonc codex',
    'aether essence',
    'antikythera mechanism',
    'voynich manuscript',
    'crystal haniwa'
]

def prompt_artifs_select(toggle_primary_secondary) -> str:
    if toggle_primary_secondary == 1:
        variable_text = 'primary'
    else:
        variable_text = 'secondary'

    toggle_selected_artifs = False
    while not toggle_selected_artifs:
        response_jfd = input(f'Is the {variable_text} artifact JFD-farmable? (Y/N)\n')
        print()

        if response_jfd.lower() == 'y':
            sorted_artifs = sorted(artifs_jfd)
            print('JFD artifacts selected.\n')
        elif response_jfd.lower() == 'n':
            sorted_artifs = sorted(artifs_non_jfd)
            print('Non-JFD artifacts selected.\n')
        else:
            print('Invalid response, please try again.\n')
            continue
        
        range_artifs = range(len(sorted_artifs))

        print(f'Select the {variable_text} artifact from the following list:')
        print('\t0 - (BACK)')
        for i in range_artifs:
            print(f'\t{i+1} - {sorted_artifs[i].title()}')

        response_artifs = input(f'{variable_text.title()} artifact selection: ')
        print()

        try:
            if response_artifs == '0':
                pass
            elif (int(response_artifs) - 1) in range_artifs:
                selected_artifs = sorted_artifs[int(response_artifs) - 1]
                print(f'{variable_text.title()} artifact selected:', selected_artifs.title())
                toggle_selected_artifs = True
            else:
                print('Invalid response, please try again.\n')
        except ValueError:
            print('Invalid response, please try again.\n')
    
    return selected_artifs

def prompt_artifs_confirm(vars_char: dict) -> dict:
    toggle_confirmed_artifs = False
    while not toggle_confirmed_artifs:
        artifs_primary = prompt_artifs_select(1)
        print()
        artifs_secondary = prompt_artifs_select(2)

        print('\nPrimary artifact:', artifs_primary.title())
        print(f'Secondary artifact: {artifs_secondary.title()}')
        
        response_artifs_confirm = input('\nAre the above selections correct? (Y/N)\n')
        if response_artifs_confirm.lower() == 'y':
            vars_char['artifs_primary'] = artifs_primary
            vars_char['artifs_secondary'] = artifs_secondary

            toggle_confirmed_artifs = True
        elif response_artifs_confirm.lower() == 'n':
            print('\nSelection was incorrect - please try again.\n')
        else:
            print('\nInvalid response, please try again.\n')

    print('\nArtifacts successfully assigned.')
    return vars_char
