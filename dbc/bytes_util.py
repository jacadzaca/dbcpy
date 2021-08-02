"""
contains helper functions for conversions to/from byte representations
"""
import struct

def to_int(byttes):
    return int.from_bytes(byttes, byteorder='little', signed=True)

def to_float(byttes):
    return struct.unpack('f', byttes)[0]

def float_to_bytes(floatt):
    return struct.pack('f', floatt)

def to_bytes(x):
    if isinstance(x, int):
        int32_size = 4
        return x.to_bytes(int32_size, byteorder='little', signed=True)
    elif isinstance(x, float):
        return struct.pack('f', x)
    else:
        raise ValueError('to_bytes only converts ints and floats')

