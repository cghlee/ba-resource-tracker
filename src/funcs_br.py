## Blu-rays
# 1 -> 2 = primary T1
# 2 -> 3 = primary T2, secondary T1
# 3 -> 4 = primary T3, secondary T2
# 4 -> 5 = primary T5, secondary T3

br_artifs_tiers = [
        {'ex_init': 1,
         'ex_final': 2,
         'tier_primary': 1,
         'tier_secondary': 0},
        {'ex_init': 2,
         'ex_final': 3,
         'tier_primary': 2,
         'tier_secondary': 1},
        {'ex_init': 3,
         'ex_final': 4,
         'tier_primary': 3,
         'tier_secondary': 2},
        {'ex_init': 4,
         'ex_final': 5,
         'tier_primary': 4,
         'tier_secondary': 3}
    ]

def prompt_br_confirm(vars_char: dict) -> dict:
    artif_primary = vars_char['artifs_primary']
    artif_secondary = vars_char['artifs_secondary']

    toggle_artifs_quants_confirmed = False
    while not toggle_artifs_quants_confirmed:
        ## Below block into separate function, output br_artifs_quants?
        try:
            br_artifs_quants = []
            print()

            for i in br_artifs_tiers:
                ex_init = i['ex_init']
                ex_final = i['ex_final']
                tier_primary = i['tier_primary']
                tier_secondary = i['tier_secondary']

                print(f'For EX level {ex_init} -> {ex_final}, how many tier {tier_primary} '
                    f'primary artifacts ({artif_primary.title()}) are needed?')
                br_artifs_primary = int(input())

                if (tier_secondary) and (not artif_primary == artif_secondary):
                    print(f'For EX level {ex_init} -> {ex_final}, how many tier {tier_secondary} '
                        f'secondary artifacts ({artif_secondary.title()}) are needed?')
                    br_artifs_secondary = int(input())
                else:
                    br_artifs_secondary = 0
                print()

                br_artifs_quants.append((br_artifs_primary, br_artifs_secondary))
        except ValueError:
            print('\nInvalid response, please try again.')
            continue
        ## Above block into separate function, output br_artifs_quants?
        
        for i in range(len(br_artifs_quants)):
            tier_primary = br_artifs_tiers[i]['tier_primary']
            tier_secondary = br_artifs_tiers[i]['tier_secondary']

            print(f'EX level {i+1} -> {i+2}:')
            print(f'\t{br_artifs_quants[i][0]}x (tier {tier_primary}) '
                  f'primary artifacts ({artif_primary.title()})')
            if (br_artifs_quants[i][1]) and (not artif_primary == artif_secondary):
                print(f'\t{br_artifs_quants[i][1]}x (tier {tier_secondary}) '
                      f'secondary artifacts ({artif_secondary.title()})')

        print('\nAre the above artifact requirements correct? (Y/N)')
        response_artifs_quants_confirmed = input()
        if response_artifs_quants_confirmed.lower() == 'y':
            vars_char['br_artifs_quants'] = br_artifs_quants

            toggle_artifs_quants_confirmed = True
        elif response_artifs_quants_confirmed.lower() == 'n':
            print('\nSelection was incorrect - please try again.')
        else:
            print('\nInvalid response, please try again.')
    
    print('Artifact quantities successfully assigned.')
    return vars_char
