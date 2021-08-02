# dbcpy

## About
This repository contains code for a python3 library that is capable of editing various [DBC](https://wowdev.wiki/DBC) files.
The library was only tested with a 3.3.5a DBCs and a [TrinityCore](https://www.trinitycore.org) server.
If this library dose not fit your use case, please consider using [pywowlib](https://github.com/wowdev/pywowlib/) - although
pywowlib's README states that reading/writing DBCs is not possible, [the features seem to be already implemented](https://github.com/wowdev/pywowlib/blob/master/wdbx/wdbc.py).

## Examples
##### Modifying an Item.dbc entry's display id (will take about 1.6s)

```python
#!/usr/bin/env python3
from dbc_file import DBCFile
from records.item_record import ItemRecord

if __name__ == '__main__':
    with open('Item.dbc', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, ItemRecord)
        some_item = next(filter(lambda item: item.entry == 873, dbc_file.records))
        some_item.entry = 56807
        some_item.display_id = 20300
        dbc_file.records.add_records(some_item)
        with open('Item.dbc.new', 'w+b') as ff:
            dbc_file.write_to_file(ff)

    with open('Item.dbc.new', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, ItemRecord)
        the_item = next(filter(lambda spell: spell.entry == 56807, dbc_file.records))
        print(the_item.entry)
        print(the_item.display_id)

```

##### Adding an Spell.dbc entry with a modified name (will take about 45 seconds):

```python
#!/usr/bin/env python3
from dbc_file import DBCFile
from records.spell_record import SpellRecord

if __name__ == '__main__':
    with open('Spell.dbc', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, SpellRecord)
        some_spell = next(filter(lambda spell: spell.entry == 116, dbc_file.records))
        some_spell.name.en_us = 'New spell name'
        some_spell.entry = 80865
        dbc_file.records.add_records(some_spell)
        with open('Spell.dbc.new', 'w+b') as ff:
            dbc_file.write_to_file(ff)

    with open('Spell.dbc.new', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, SpellRecord)
        the_spell = next(filter(lambda spell: spell.entry == 80865, dbc_file.records))
        print(the_spell.name.en_us)

```

## Legal Note
World of Warcraft is a registered trademark of Blizzard Entertainment and/or other respective owners.
This software is not created by Blizzard Entertainment or its affiliates, and is for purely educational and research purposes.
This software is not intended for the use and production of cheating (hacking) software or modifications that can disrupt World of Warcraft's gameplay.
It is your sole responsibility to follow copyright law, game's ToS and EULA.
The creators hold no responsibility for the consequences of use of this software.

The code is licensed under [LGPL 3.0](https://www.gnu.org/licenses/lgpl-3.0.txt).

