import dataclasses

_fields = {
    'entry': int,
    'file_name': str
}

SpellIconRecord = dataclasses.make_dataclass('SpellIconRecord', zip(_fields.keys(), _fields.values()))
SpellIconRecord .field_types = staticmethod(_fields.values())

