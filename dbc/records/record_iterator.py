class RecordIterator():
    """
    iterator for... iterating over records stored in a DBC file
    """
    def __init__(self, f, dbc_header, record_reader, string_block):
        self._f = f
        self._header = dbc_header
        self._record_reader = record_reader
        self._string_block = string_block
        self._size = dbc_header.record_count * dbc_header.record_size

    def __iter__(self):
        self._f.seek(self._header.size)
        return self

    def __next__(self):
        if self._f.tell() < self._size:
            return self._record_reader.read_record(self._string_block, self._f)
        raise StopIteration

