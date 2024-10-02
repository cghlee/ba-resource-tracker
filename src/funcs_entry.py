# Characters last updated on 2024-10-02
# Most recent releases: Kisaki, Reijo
chars_total = [
        'airi', 'airi (band)', 'akane', 'akane (bunny)', 'akari',
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
        'kisaki', 'koharu', 'koharu (swimsuit)', 'kokona', 'kotama',
        'kotama (camp)', 'kotori', 'kotori (cheer squad)', 'koyuki', 'maki',
        'makoto', 'mari', 'mari (track)', 'marina', 'marina (qipao)', 'mashiro',
        'mashiro (swimsuit)', 'megu', 'meru', 'michiru', 'midori',
        'midori (maid)', 'mika', 'mimori', 'mimori (swimsuit)', 'mina',
        'mine', 'minori', 'misaka mikoto', 'misaki', 'miyako',
        'miyako (swimsuit)', 'miyu', 'miyu (swimsuit)', 'moe',
        'moe (swimsuit)', 'momiji', 'momoi', 'momoi (maid)', 'mutsuki',
        'mutsuki (new year)', 'nagisa', 'natsu', 'neru', 'neru (bunny)',
        'noa', 'nodoka', 'nodoka (onsen)', 'nonomi', 'nonomi (swimsuit)',
        'pina', 'reijo', 'reisa', 'renge', 'rumi', 'saki', 'saki (swimsuit)',
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

def prompt_init(dict_db_curr: dict, dict_tracked_curr: dict):
    print(f'\n{len(dict_tracked_curr)} characters currently tracked ({len(dict_db_curr)} in database)\n'
          'Please select an option:\n'
          '\t1 - Begin tracking a character\n'
          '\t2 - Add character to database\n'
          '\t3 - Edit character in database\n'
          '\t4 - Save and exit\n'
          '\t5 - Exit without saving')

def prompt_name_db_add_confirm(dict_db_curr: dict) -> str:
    # TODO: Use alternative to "while True"?
    while True:
        response_name_db_add = input('Input name of character to be added to the database: (input "x" to cancel)\n').lower()

        if response_name_db_add == 'x':
            print('\nCancelling addition of character to database.')
            return None
        elif response_name_db_add in dict_db_curr:
            print(f'\n{response_name_db_add.title()} is already in the database.')
            return None
        elif response_name_db_add in chars_total:
            return response_name_db_add
        else:
            print('\nCharacter not recognised, please try again.\n')

def prompt_name_db_edit_confirm(dict_db_curr: dict) -> str:
    # TODO: Use alternative to "while True"?
    toggle_name_db_edit_selected = False
    while not toggle_name_db_edit_selected:
        response_name_db_edit = input('Input name of character in the database to be edited: (input "x" to cancel)\n').lower()

        if response_name_db_edit == 'x':
            print('\nCancelling editing of character in database.')
            return None
        elif response_name_db_edit in dict_db_curr:
            confirmation_name_db_edit = input(f'\n{response_name_db_edit.title()} selected. Is this correct? (Y/N)\n').lower()
            
            if confirmation_name_db_edit == 'y':
                print()
                return response_name_db_edit
            if confirmation_name_db_edit == 'n':
                print()
            else:
                print('\nInvalid response, please try again.\n')
        else:
            print('\nCharacter not recognised, please try again.\n')

def prompt_name_tracked_add_confirm(dict_db_curr: dict, dict_tracked_curr: dict) -> str:
    # TODO: Use alternative to "while True"?
    toggle_name_tracked_add_selected = False
    while not toggle_name_tracked_add_selected:
        response_name_tracked_add = input('Input name of character to be tracked: (input "x" to cancel)\n').lower()

        if response_name_tracked_add == 'x':
            print('\nCancelling addition of character to be tracked.')
            return None
        elif response_name_tracked_add in dict_tracked_curr:
            print(f'\n{response_name_tracked_add.title()} is already being tracked.')
            return None
        elif response_name_tracked_add in dict_db_curr:
            confirmation_name_tracked_add = input(f'\n{response_name_tracked_add.title()} selected. Is this correct? (Y/N)\n').lower()
            
            if confirmation_name_tracked_add == 'y':
                return response_name_tracked_add
            if confirmation_name_tracked_add == 'n':
                print()
            else:
                print('\nInvalid response, please try again.\n')
        else:
            print('\nCharacter not recognised, please try again.\n')
