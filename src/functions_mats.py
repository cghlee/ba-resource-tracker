mats_jfd = [
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

mats_non_jfd = [
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

def prompt_mats(toggle_primary_secondary) -> str:
    if toggle_primary_secondary == 1:
        variable_text = 'primary'
    else:
        variable_text = 'secondary'

    toggle_selected_mats = False
    while not toggle_selected_mats:
        response_jfd = input(f'Is the {variable_text} material JFD-farmable? (Y/N)\n')
        print()

        if response_jfd.lower() == 'y':
            sorted_mats = sorted(mats_jfd)
            print('JFD materials selected.\n')
        elif response_jfd.lower() == 'n':
            sorted_mats = sorted(mats_non_jfd)
            print('Non-JFD materials selected.\n')
        else:
            print('Invalid response, please try again.\n')
            continue
        
        range_mats = range(len(sorted_mats))

        print(f'Select the {variable_text} material from the following list:')
        print('\t0 - (BACK)')
        for i in range_mats:
            print(f'\t{i+1} - {sorted_mats[i].title()}')

        response_mats = input(f'{variable_text.title()} material selection: ')
        print()

        try:
            if response_mats == '0':
                pass
            elif (int(response_mats) - 1) in range_mats:
                selected_mats = sorted_mats[int(response_mats) - 1]
                print(f'{variable_text.title()} material selected:', selected_mats.title())
                toggle_selected_mats = True
            else:
                print('Invalid response, please try again.\n')
        except ValueError:
            print('Invalid response, please try again.\n')
    
    return selected_mats
