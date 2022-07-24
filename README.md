## About
This repository contains code for a python3 library that is capable of editing various [DBC](https://wowdev.wiki/DBC) files.
The library was only tested with 3.3.5a DBCs and a [TrinityCore](https://www.trinitycore.org) server.
If this library dose not fit your use case, please consider using [pywowlib](https://github.com/wowdev/pywowlib/). Although
pywowlib's README states that reading/writing DBCs is not possible, [the features seem to be already implemented](https://github.com/wowdev/pywowlib/blob/master/wdbx/wdbc.py).

## Instalation
```bash
pip install dbcpy
```

## Records
dbcpy dose NOT use [WoWDBDefs](https://github.com/wowdev/WoWDBDefs) to parse the DBCs.
DBC representations must be added manually, for a list of supported DBCs see [records](https://github.com/jacadzaca/dbcpy/tree/master/dbcpy/records)

##### Adding records
Adding a record is easy. Just pick a copy-paste the definition from [here](https://wowdev.wiki/Category:DBC_WotLK)
into a python dictionary and define a new dataclass. See [this](https://github.com/jacadzaca/dbcpy/blob/master/dbcpy/records/item_record.py) for a
reference implementation.

## Examples
##### Modifying an existing items' display_ids (will take ~1 second)

```python
#!/usr/bin/env python3
from dbcpy.dbc_file import DBCFile
from dbcpy.records.item_record import ItemRecord

def change_display_ids(item_record):
    # entry: new_display_id
    new_display_ids = {
        1501: 37388,
        15534: 27083,
    }
    try:
        item_record.display_id = new_display_ids[item_record.entry]
        return item_record
    except KeyError:
        return item_record

if __name__ == '__main__':
    with open('Item.dbc', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, ItemRecord)
        some_item = dbc_file.records.find(873)
        some_item.entry = 56807
        some_item.display_id = 20300
        with open('Item.dbc.new', 'w+b') as ff:
            dbc_file.write_to_file(change_display_ids, ff)

    with open('Item.dbc.new', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, ItemRecord)
        print(dbc_file.records.find(1501).display_id)
        print(dbc_file.records.find(15534).display_id)

```

##### Adding a Spell.dbc entry (will take >1 second):

```python
#!/usr/bin/env python3
from dbcpy.dbc_file import DBCFile
from dbcpy.records.spell_record import SpellRecord

if __name__ == '__main__':
    with open('Spell.dbc', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, SpellRecord)
        some_spell = dbc_file.records.find(116)
        some_spell.name.en_us = 'New spell name'
        some_spell.entry = 80865
        dbc_file.records.append(some_spell)

    with open('Spell.dbc', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, SpellRecord)
        the_spell = dbc_file.records.find(80865)
        print(the_spell.name.en_us)

```

##### Modyfing an existing spells' names (will take ~30 seconds)

```python
#!/usr/bin/env python3
from dbcpy.dbc_file import DBCFile
from dbcpy.records.spell_record import SpellRecord

def rename_spell(spell_record):
    new_names = {
        8716: 'i love',
        37263: 'long',
        37290: 'discussions',
    }
    try:
        spell_record.name.en_us = new_names[spell_record.entry]
        return spell_record
    except KeyError:
        return spell_record

if __name__ == '__main__':
    with open('Spell.dbc', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, SpellRecord)
        with open('Spell.dbc.new', 'w+b') as ff:
            dbc_file.write_to_file(rename_spell, ff)

    with open('Spell.dbc.new', 'r+b') as f:
        dbc_file = DBCFile.from_file(f, SpellRecord)
        print(dbc_file.records.find(8716).name.en_us)
        print(dbc_file.records.find(37263).name.en_us)
        print(dbc_file.records.find(37290).name.en_us)

```

## Why dose modifying an existing record takes so long?
Well, not always. In order to modify an existing record, we must rewrite the whole DBC file, because of the string block.
The SpellRecord is especially *large* and the [RecordReader.read_record](https://github.com/jacadzaca/dbcpy/blob/master/dbcpy/records/record_reader.py)
method is not suited for reading *large* records like that. It handles smaller records (like ItemRecord) well enough (~1 second).
The simplest fix would be to implement a SpellRecord specific RecordReader.

## How to contribute?
1. Ensure that your commits have meaningful comments
2. If your contribution is small (e.g it fixes a minor bug) increment revision (the last digit of version) in [setup.py](https://github.com/jacadzaca/dbcpy/blob/master/setup.py)
3. Provide test-cases

## Legal Note
World of Warcraft is a registered trademark of Blizzard Entertainment and/or other respective owners.
This software is not created by Blizzard Entertainment or its affiliates, and is for purely educational and research purposes.
This software is not intended for the use and production of cheating (hacking) software or modifications that can disrupt World of Warcraft's gameplay.
It is your sole responsibility to follow copyright law, game's ToS and EULA.
The creators hold no responsibility for the consequences of use of this software.

The code is licensed under [LGPL 3.0](https://www.gnu.org/licenses/lgpl-3.0.txt).

