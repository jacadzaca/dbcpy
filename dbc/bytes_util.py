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

def to_bytes(intt, field_size):
    return intt.to_bytes(field_size, byteorder='little', signed=True)
