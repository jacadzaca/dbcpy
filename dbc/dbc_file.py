from dataclasses import dataclass
from dbc_header import DBCHeader
from records.record_iterator import RecordIterator

@dataclass
class DBCFile():
    header: DBCHeader
    records: RecordIterator

    @classmethod
    def from_file(cls, f, record_type):
        header = DBCHeader.from_file_handle(f)
        f.seek(header.size + header.record_size * header.record_count)
        string_block = f.read()
        records = RecordIterator(f, header, record_type.read_record, record_type.create_record, string_block)
        return cls(header, records)

