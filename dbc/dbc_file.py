import bytes_util
from dataclasses import dataclass
from dbc_header import DBCHeader
from records.record_iterator import RecordIterator
from loc import Loc

@dataclass
class DBCFile():
    header: DBCHeader
    records: RecordIterator

    def write_to_file(self, f):
        string_block = [b'\0']
        string_block_offset = 1
        f.write(self.header.to_bytes())
        for record in self.records:
            for field in record.__dict__.values():
                if isinstance(field, int):
                    f.write(bytes_util.to_bytes(field, 4))
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
        f.write(b''.join(string_block))

    @classmethod
    def from_file(cls, f, record_type):
        header = DBCHeader.from_file_handle(f)
        f.seek(header.size + header.record_size * header.record_count)
        string_block = f.read()
        records = RecordIterator(f, header, record_type.read_record, record_type.create_record, string_block)
        return cls(header, records)

