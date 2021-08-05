import itertools
from dataclasses import dataclass

import dbcpy.bytes_util as bytes_util
from dbcpy.dbc_header import DBCHeader
from dbcpy.records.record_reader import RecordReader
from dbcpy.records.record_iterator import RecordIterator
from dbcpy.loc import Loc

@dataclass
class DBCFile():
    """
    representation of a DBC file
    """
    header: DBCHeader
    records: RecordIterator

    def write_to_file(self, transform, f):
        string_block_offset = self.header.size + self.header.record_count * self.header.record_size
        f.seek(string_block_offset)
        f.write(b'\0')
        string_block_size = 1

        # reserve the first 20 bytes for the header
        f.seek(self.header.size)

        for record in map(transform, self.records):
            for field in record.__dict__.values():
                if isinstance(field, Loc):
                    for string in itertools.islice(field.__dict__.values(), 16):
                        if string:
                            f.write(bytes_util.to_bytes(string_block_size))
                            pos = f.tell()
                            f.seek(string_block_offset + string_block_size)
                            f.write((string + '\0').encode('utf-8'))
                            string_block_size += len(string + '\0')
                            f.seek(pos)
                        else:
                            f.write(bytes_util.to_bytes(0))
                    f.write(bytes_util.to_bytes(field.flag))
                else:
                    f.write(bytes_util.to_bytes(field))

        f.seek(0)
        self.header.string_block_size = string_block_size
        f.write(self.header.to_bytes())

    @classmethod
    def from_file(cls, f, record_type):
        header = DBCHeader.from_file_handle(f)
        f.seek(header.size + header.record_size * header.record_count)
        string_block = f.read()
        records = RecordIterator(f, header, RecordReader(record_type), string_block)
        return cls(header, records)

