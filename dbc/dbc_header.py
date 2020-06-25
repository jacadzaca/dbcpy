from typing import List
from typing import BinaryIO
import dbc.bytes_util as bytes_util
from dataclasses import dataclass


@dataclass()
class DBCHeader():
    magic: str
    record_count: int
    field_count: int
    record_size: int
    string_block_size: int
    size: int

    def to_bytes(self) -> List[bytes]:
        return [self.magic,
                bytes_util.to_bytes(self.record_count, 4),
                bytes_util.to_bytes(self.field_count, 4),
                bytes_util.to_bytes(self.record_size, 4),
                bytes_util.to_bytes(self.string_block_size, 4)]

    '''
    method changes the @file_handle's position
    @see https://wowdev.wiki/DBC
    '''
    @classmethod
    def from_file_handle(cls, file_handle: BinaryIO):
        file_handle.seek(0)
        size = 4 * 5
        header_bytes = file_handle.read(size)
        magic = header_bytes[0:4]
        record_count = bytes_util.to_int(header_bytes[4:8])
        field_count = bytes_util.to_int(header_bytes[8:12])
        record_size = bytes_util.to_int(header_bytes[12:16])
        string_block_size = bytes_util.to_int(header_bytes[16:20])
        return cls(magic, record_count, field_count,
                   record_size, string_block_size, size)
