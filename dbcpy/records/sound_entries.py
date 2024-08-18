import dataclasses

_fields = {
    'id': int,
    'sound_type': int,
    'name': str,
    'file_1': str,
    'file_2': str,
    'file_3': str,
    'file_4': str,
    'file_5': str,
    'file_6': str,
    'file_7': str,
    'file_8': str,
    'file_9': str,
    'file_10': str,
    'frequency_1': int,
    'frequency_2': int,
    'frequency_3': int,
    'frequency_4': int,
    'frequency_5': int,
    'frequency_6': int,
    'frequency_7': int,
    'frequency_8': int,
    'frequency_9': int,
    'frequency_10': int,
    'directory_base': str,
    'volume': float,
    'flags': int,
    'min_distance': float,
    'max_distance': float,
    'distance_cutoff': float,
    'sound_entries_advanced_id': int,
}

SoundEntriesRecord = dataclasses.make_dataclass('SoundEntriesRecord', zip(_fields.keys(), _fields.values()))
SoundEntriesRecord .field_types = staticmethod(_fields.values())

