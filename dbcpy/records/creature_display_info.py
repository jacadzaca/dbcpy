import dataclasses

_fields = {
    'id': int,
    'model': int,
    'sound': int,
    'extra_display_information': int,
    'scale': float,
    'opacity': int,
    'texture1': str,
    'texture2': str,
    'texture3': str,
    'portrait_texturename': str,
    'blood_level': int,
    'blood': int,
    'npc_sounds': int,
    'particles': int,
    'creature_geoset_data': int,
    'object_effect_package_id': int,
}

CreatureDisplayInfoRecord = dataclasses.make_dataclass('CreatureDisplayInfoRecord', zip(_fields.keys(), _fields.values()))
CreatureDisplayInfoRecord.field_types = staticmethod(_fields.values())

