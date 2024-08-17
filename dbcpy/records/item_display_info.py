import dataclasses

_fields = {
    'id': int,
    'left_model': str,
    'right_model': str,
    'left_model_texture': str,
    'right_model_texture': str,
    'icon_1': str,
    'icon_2': str,
    'geosetGroup_1': int,
    'geosetGroup_2': int,
    'geosetGroup_3': int,
    'flags': int,
    'spell_visual_id': int,
    'group_sound_index': int,
    'helmet_geoset_vis': int,
    'helmetGeosetVis': int,
    'UpperArmTexture': str,
    'LowerArmTexture': str,
    'HandsTexture': str,
    'UpperTorsoTexture': str,
    'LowerTorsoTexture': str,
    'UpperLegTexture': str,
    'LowerLegTexture': str,
    'FootTexture': str,
    'itemVisual': int,
    'particleColorID': int,
}

ItemDisplayInfoRecord = dataclasses.make_dataclass('ItemDisplayRecord', zip(_fields.keys(), _fields.values()))
ItemDisplayInfoRecord.field_types = staticmethod(_fields.values())

