'''
contains helper functions for conversions to/from byte representations
'''
from typing import List


def to_int(byttes: List[bytes]) -> int:
    return int.from_bytes(byttes, byteorder='little', signed=True)


def to_bytes(intt: int, field_size: int) -> List[bytes]:
    return intt.to_bytes(field_size, byteorder='little', signed=True)
