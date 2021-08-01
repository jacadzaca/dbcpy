import dataclasses

_fields = {
    'entry': int,
    'clazz': int,
    'sub_class': int,
    'sound': int,
    'material_id': int,
    'display_id': int,
    'slot_id': int,
    'sheat_id': int
}

ItemRecord = dataclasses.make_dataclass('ItemRecord', zip(_fields.keys(), _fields.values()))
ItemRecord.field_types = staticmethod(_fields.values())

