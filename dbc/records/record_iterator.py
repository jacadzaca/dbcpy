import itertools

class RecordIterator():
    """
    iterator for... iterating over records stored in a DBC file
    """
    def __init__(self, f, dbc_header, record_reader, string_block, new_records=iter([])):
        self._f = f
        self._header = dbc_header
        self._record_reader = record_reader
        self._string_block = string_block
        self._size = dbc_header.record_count * dbc_header.record_size
        self._new_records = new_records

    def add_records(self, *records):
        self._header.record_count += len(records)

        self._new_records = itertools.chain(self._new_records, iter(records))

    def __iter__(self):
        self._f.seek(self._header.size)
        return self

    def __next__(self):
        if self._f.tell() < self._size:
            return self._record_reader.read_record(self._string_block, self._f)
        return next(self._new_records)

