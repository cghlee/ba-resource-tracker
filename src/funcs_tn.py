## Tech Notes
# 3 -> 4 = primary T1
# 4 -> 5 = primary T2, secondary T1
# 5 -> 6 = primary T2, secondary T1
# 6 -> 7 = primary T3, secondary T2
# 7 -> 8 = primary T4, secondary T3
# 8 -> 9 = primary T4, secondary T3

tn_artifs_tiers = [
        {'skill_init': 3,
         'skill_final': 4,
         'tier_primary': 1,
         'tier_secondary': 0},
        {'skill_init': 4,
         'skill_final': 5,
         'tier_primary': 2,
         'tier_secondary': 1},
        {'skill_init': 5,
         'skill_final': 6,
         'tier_primary': 2,
         'tier_secondary': 1},
        {'skill_init': 6,
         'skill_final': 7,
         'tier_primary': 3,
         'tier_secondary': 2},
        {'skill_init': 7,
         'skill_final': 8,
         'tier_primary': 4,
         'tier_secondary': 3},
        {'skill_init': 8,
         'skill_final': 9,
         'tier_primary': 4,
         'tier_secondary': 3}
    ]

def prompt_tn_quants(artif_primary: str, artif_secondary: str) -> list:
    # No artifacts are needed for skill levels 1 -> 2 and 2 -> 3
    tn_artifs_quants = [(0, 0), (0, 0)]

    print()
    for i in tn_artifs_tiers:
        skill_init = i['skill_init']
        skill_final = i['skill_final']
        tier_primary = i['tier_primary']
        tier_secondary = i['tier_secondary']

        print(f'For skill level {skill_init} -> {skill_final}, how many tier {tier_primary} '
            f'primary artifacts ({artif_primary.title()}) are needed?')
        tn_artifs_primary = int(input())

        if (tier_secondary):
            print(f'For skill level {skill_init} -> {skill_final}, how many tier {tier_secondary} '
                f'secondary artifacts ({artif_secondary.title()}) are needed?')
            tn_artifs_secondary = int(input())
        else:
            tn_artifs_secondary = 0

        tn_artifs_quants.append((tn_artifs_primary, tn_artifs_secondary))
        print()

    return tn_artifs_quants

def prompt_tn_confirm(vars_char: dict) -> dict:
    artif_primary = vars_char['artifs_primary']
    artif_secondary = vars_char['artifs_secondary']

    toggle_tn_artifs_quants_confirmed = False
    while not toggle_tn_artifs_quants_confirmed:
        try:
            tn_artifs_quants = prompt_tn_quants(artif_primary, artif_secondary)
        except ValueError:
            print('\nInvalid response, please try again.')
            continue
        
        for i in range(len(tn_artifs_quants)):
            tier_primary = tn_artifs_tiers[i]['tier_primary']
            tier_secondary = tn_artifs_tiers[i]['tier_secondary']

            print(f'Skill level {i+3} -> {i+4}:')
            print(f'\t{tn_artifs_quants[i][0]}x (tier {tier_primary}) '
                  f'primary artifacts ({artif_primary.title()})')
            if (tn_artifs_quants[i][1]):
                print(f'\t{tn_artifs_quants[i][1]}x (tier {tier_secondary}) '
                      f'secondary artifacts ({artif_secondary.title()})')

        confirmation_tn_artifs_quants = input('\nAre the above artifact requirements correct? (Y/N)\n').lower()
        print()
        
        if confirmation_tn_artifs_quants == 'y':
            vars_char['tn_artifs_quants'] = tn_artifs_quants

            toggle_tn_artifs_quants_confirmed = True
        elif confirmation_tn_artifs_quants == 'n':
            print('Selection was incorrect - please try again.')
        else:
            print('Invalid response, please try again.')
    
    print('TN-related artifact quantities successfully assigned.\n')
    return vars_char
