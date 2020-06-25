from typing import BinaryIO
from typing import Optional
from dbc.dbc_header import DBCHeader
from dbc.records.__init__ import Record
from dbc.records.record_iterator import RecordIterator


def append_record(record: Record, header: DBCHeader, file: BinaryIO):
    """
    file MUST have write permissions
    this method changes the file's cursor
    """
    # increment record_count
    header.record_count += 1
    file.seek(0)
    for field in header.to_bytes():
        file.write(field)

    file.seek(header.size + (header.record_count - 1) * header.record_size)
    for field in record.to_bytes():
        file.write(field)
    # write strings...
    file.write('\0'.join(record.strings()).encode())


"""
this method requires the record instance in @records to have an entry field
"""


def find(entry: int, records: RecordIterator) -> Optional[Record]:
    return next(filter(lambda item: item.entry == entry, records))
