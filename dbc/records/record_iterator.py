class RecordIterator():
    def __init__(self, f, dbc_header, read_record, create_record, string_block):
        self._f = f
        self._header = dbc_header
        self._read_record = read_record
        self._create_record = create_record
        self._string_block = string_block
        self._size = dbc_header.record_count * dbc_header.record_size

    def __iter__(self):
        self._f.seek(self._header.size)
        return self

    def __next__(self):
        if self._f.tell() < self._size:
            return self._create_record(self._string_block, *self._read_record(self._f))
        else:
            raise StopIteration

