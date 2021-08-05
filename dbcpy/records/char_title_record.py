import dataclasses
from dbcpy.loc import Loc

_fields = {
    'entry': int,
    'unknown': int,
    'male_title': Loc,
    'female_title': Loc,
    'title_mask_id': int
}

CharTitleRecord = dataclasses.make_dataclass('CharTitleRecord', zip(_fields.keys(), _fields.values()))
CharTitleRecord.field_types = staticmethod(_fields.values())

