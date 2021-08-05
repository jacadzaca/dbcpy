import dataclasses
from dbcpy.loc import Loc

_fields = {
    'entry': int,
    'tip': Loc
}

GameTipRecord = dataclasses.make_dataclass('GameTipRecord', zip(_fields.keys(), _fields.values()))
GameTipRecord.field_types = staticmethod(_fields.values())

