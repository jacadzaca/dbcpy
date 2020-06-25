"""
stores different representations of dbc file structures
ALL representations MUST specify a strings() method
that returns string to be put in string_block section,
if no strings are to be put, the implementation should return NO_STRING.
ALL representations MUST specify a to_bytes() method
for different types of records @see https://wowdev.wiki/Category:DBC_WotLK
"""
from typing import TypeVar

NO_STRING = ['\0']
Record = TypeVar('Record')
