# Characters last updated on 2024-09-18
# Most recent releases: Marina (Qipao), Tomoe (Qipao)
chars_total = [
        'airi', 'airi_band', 'akane', 'akane (bunny)', 'akari',
        'akari (new year)', 'ako', 'ako (dress)', 'aris', 'aris (maid)',
        'aru', 'aru (dress)', 'aru (new year)', 'asuna', 'asuna (bunny)',
        'atsuko', 'atsuko (swimsuit)', 'ayane', 'ayane (swimsuit)', 'azusa',
        'azusa (swimsuit)', 'cherino', 'cherino (onsen)', 'chihiro',
        'chinatsu', 'chinatsu (onsen)', 'chise', 'chise (swimsuit)', 'eimi',
        'eimi (swimsuit)', 'fubuki', 'fubuki (swimsuit)', 'fuuka',
        'fuuka (new year)', 'hanae', 'hanae (christmas)', 'hanako',
        'hanako (swimsuit)', 'hare', 'hare (camp)', 'haruka',
        'haruka (new year)', 'haruna', 'haruna (new year)', 'haruna (track)',
        'hasumi', 'hasumi (track)', 'hatsune miku', 'hibiki',
        'hibiki (cheer squad)', 'hifumi', 'hifumi (swimsuit)', 'himari',
        'hina', 'hina (dress)', 'hina (swimsuit)', 'hinata',
        'hinata (swimsuit)', 'hiyori', 'hiyori (swimsuit)', 'hoshino',
        'hoshino (battle)', 'hoshino (swimsuit)', 'ibuki', 'ichika', 'iori',
        'iori (swimsuit)', 'iroha', 'izumi', 'izumi (swimsuit)', 'izuna',
        'izuna (swimsuit)', 'junko', 'junko (new year)', 'juri', 'kaede',
        'kaho', 'kanna', 'kanna (swimsuit)', 'karin', 'karin (bunny)',
        'kasumi', 'kayoko', 'kayoko (dress)', 'kayoko (new year)', 'kazusa',
        'kazusa (band)', 'kikyou', 'kirara', 'kirino', 'kirino (swimsuit)',
        'koharu', 'koharu (swimsuit)', 'kokona', 'kotama', 'kotama (camp)',
        'kotori', 'kotori (cheer squad)', 'koyuki', 'maki', 'makoto', 'mari',
        'mari (track)', 'marina', 'marina (qipao)', 'mashiro',
        'mashiro (swimsuit)', 'megu', 'meru', 'michiru', 'midori',
        'midori (maid)', 'mika', 'mimori', 'mimori (swimsuit)', 'mina',
        'mine', 'minori', 'misaka mikoto', 'misaki', 'miyako',
        'miyako (swimsuit)', 'miyu', 'miyu (swimsuit)', 'moe',
        'moe (swimsuit)', 'momiji', 'momoi', 'momoi (maid)', 'mutsuki',
        'mutsuki (new year)', 'nagisa', 'natsu', 'neru', 'neru (bunny)',
        'noa', 'nodoka', 'nodoka (onsen)', 'nonomi', 'nonomi (swimsuit)',
        'pina', 'reisa', 'renge', 'rumi', 'saki', 'saki (swimsuit)',
        'sakurako', 'saori', 'saori (swimsuit)', 'saten ruiko', 'saya',
        'saya (casual)', 'sena', 'serika', 'serika (new year)',
        'serika (swimsuit)', 'serina', 'serina (christmas)', 'shigure',
        'shigure (onsen)', 'shimiko', 'shiroko', 'shiroko (cycling)',
        'shiroko (swimsuit)', 'shiroko terror', 'shizuko',
        'shizuko (swimsuit)', 'shokuhou misaki', 'shun', 'shun (small)',
        'sumire', 'suzumi', 'toki', 'toki (bunny)', 'tomoe',
        'tomoe (qipao)', 'tsubaki', 'tsubaki (guide)', 'tsukuyo', 'tsurugi',
        'tsurugi (swimsuit)', 'ui', 'ui (swimsuit)', 'umika', 'utaha',
        'utaha (cheer squad)', 'wakamo', 'wakamo (swimsuit)', 'yoshimi',
        'yoshimi (band)', 'yukari', 'yuuka', 'yuuka (track)', 'yuzu',
        'yuzu (maid)',
    ]

def prompt_init(dict_curr: dict):
    print(f'\nX characters currently tracked ({len(dict_curr)} in database)\n'
          'Please select an option:\n'
          '\t1 - Add character to database\n'
          '\t2 - Edit character in database\n'
          '\t3 - Save and exit\n'
          '\t4 - Exit without saving')

def prompt_name_db_add_confirm(dict_curr: dict) -> str:
    # TODO: Use alternative to "while True"?
    while True:
        print('Input name of character to be added to the database: (input "x" to cancel)')
        response_name_add = input().lower()

        if response_name_add == 'x':
            print('\nCancelling addition of character to database.')
            return None
        elif response_name_add in dict_curr:
            print(f'\n{response_name_add.title()} is already in the database.')
            return None
        elif response_name_add in chars_total:
            return response_name_add
        else:
            print('\nCharacter not recognised, please try again.\n')

def prompt_name_db_edit_confirm(dict_curr: dict) -> str:
    # TODO: Use alternative to "while True"?
    toggle_name_db_edit_selected = False
    while not toggle_name_db_edit_selected:
        print('Input name of character in the database to be edited: (input "x" to cancel)')
        response_name_edit = input().lower()

        if response_name_edit == 'x':
            print('\nCancelling editing of character in database.')
            return None
        elif response_name_edit in dict_curr:
            print(f'\n{response_name_edit.title()} selected. Is this correct? (Y/N)')
            response_name_edit_confirmation = input().lower()
            
            if response_name_edit_confirmation == 'y':
                print()
                return response_name_edit
            if response_name_edit_confirmation == 'n':
                print()
            else:
                print('\nInvalid response, please try again.\n')
        else:
            print('\nCharacter not recognised, please try again.\n')
