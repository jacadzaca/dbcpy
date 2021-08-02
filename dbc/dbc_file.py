from dataclasses import dataclass
import bytes_util
from dbc_header import DBCHeader
from records.record_reader import RecordReader
from records.record_iterator import RecordIterator
from loc import Loc

@dataclass
class DBCFile():
    """
    representation of a DBC file
    """
    header: DBCHeader
    records: RecordIterator

    def write_to_file(self, f):
        string_block = [b'\0']
        string_block_offset = 1
        # write header, reserving the first 20 bytes
        f.write(self.header.to_bytes())
        # count the records, so we can modify the header later
        record_count = 0
        for record in self.records:
            record_count += 1
            for field in record.__dict__.values():
                if isinstance(field, int):
                    f.write(bytes_util.to_bytes(field, 4))
                if isinstance(field, float):
                    f.write(bytes_util.float_to_bytes(field))
                elif isinstance(field, Loc):
                    # basicly all fields from 0 through 16
                    strings = [[0, value.encode('utf-8')] for value in field.__dict__.values() if isinstance(value, str)]
                    for i, string in enumerate(strings):
                        if string[1]:
                            string[1] += b'\0'
                            string_block.append(string[1])
                            strings[i][0] = string_block_offset
                            string_block_offset += len(string[1])
                        f.write(bytes_util.to_bytes(strings[i][0], 4))
                    # the last, 17th field
                    f.write(bytes_util.to_bytes(field.flag, 4))
        string_block = b''.join(string_block)
        f.write(string_block)
        # write the proper header
        f.seek(0)
        self.header.record_count = record_count
        self.header.string_block_size = len(string_block)
        f.write(self.header.to_bytes())

    @classmethod
    def from_file(cls, f, record_type):
        header = DBCHeader.from_file_handle(f)
        f.seek(header.size + header.record_size * header.record_count)
        string_block = f.read()
        records = RecordIterator(f, header, RecordReader(record_type), string_block)
        return cls(header, records)

