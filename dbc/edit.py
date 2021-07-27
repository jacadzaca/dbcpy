from typing import BinaryIO
from typing import Optional
from dbc_header import DBCHeader
from records.__init__ import Record
from records.record_iterator import RecordIterator


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

def write_records(records, header, f):
    header.record_count += len(records)

    record_count_field_offset = 4 * 1
    f.seek(record_count_field_offset)
    f.write(header.to_bytes()[1])

    f.seek(header.size + (header.record_count - len(records)) * header.record_size)
    for record in records:
        f.write(record.to_bytes())



def find(entry: int, records: RecordIterator) -> Optional[Record]:
    """
    this method requires the record instance in @records to have an entry field
    """
    if entry is None:
        return None
    return next(filter(lambda item: item.entry == entry, records))
