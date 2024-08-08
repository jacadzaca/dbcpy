import dataclasses

_fields = {
    'id': int,
    'flags': int,
    'model_path': str,
    'size_class': int,
    'model_scale': float,
    'blood_level': int,
    'footprint': int,
    'footprint_texture_length': float,
    'footprint_texture_width': float,
    'footprint_particle_scale': float,
    'foley_material_id': int,
    'footstep_shake_size':  int,
    'deaththud_shake_size': int,
    'sound_data': int,
    'collision_width': float,
    'collision_height': float,
    'mount_height': float,
    'geo_box_min_1': float,
    'geo_box_min_2': float,
    'geo_box_min_3': float,
    'geo_box_max_1': float,
    'geo_box_max_2': float,
    'geo_box_max_3': float,
    'world_effect_scale': float,
    'attached_effect_scale': float,
    'missile_collision_radius': float,    
    'missile_collision_push': float,    
    'missile_collision_raise': float,
}

CreatureModelDataRecord = dataclasses.make_dataclass('CreatureModelDataRecord ', zip(_fields.keys(), _fields.values()))
CreatureModelDataRecord.field_types = staticmethod(_fields.values())

