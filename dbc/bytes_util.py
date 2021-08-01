"""
contains helper functions for conversions to/from byte representations
"""

def to_int(byttes):
    return int.from_bytes(byttes, byteorder='little', signed=True)


def to_bytes(intt, field_size):
    return intt.to_bytes(field_size, byteorder='little', signed=True)
