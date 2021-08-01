import bytes_util
from dbc_header import DBCHeader

def _record_to_bytes(record):
    int32_size = 4
    return b''.join((bytes_util.to_bytes(value, int32_size)
            for value in record.__dict__.values()))

def write_records(records, header, f):
    """
    this function only changes the dbc's fields, if you edit the strings,
    use DBCFile.write_to_file
    """
    header.record_count += len(records)

    record_count_field_offset = 4 * 1
    f.seek(record_count_field_offset)
    f.write(header.to_bytes()[1])

    f.seek(header.size + (header.record_count - len(records)) * header.record_size)
    for record in records:
        f.write(_record_to_bytes(record))

def find(entry, records):
    return next(filter(lambda item: item.entry == entry, records))
