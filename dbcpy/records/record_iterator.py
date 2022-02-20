import itertools
import dbcpy.bytes_util as bytes_util
from dbcpy.loc import Loc

class RecordIterator():
    """
    iterator for... iterating over records stored in a DBC file
    """
    def __init__(self, f, dbc_header, record_reader, string_block):
        self._f = f
        self._header = dbc_header
        self._record_reader = record_reader
        self._string_block = string_block

    def append(self, *records):
        self._f.seek(self._header.size + self._size())
        self._header.record_count += len(records)

        new_strings = []
        for record in records:
            for field in record.__dict__.values():
                if isinstance(field, Loc):
                    for string in itertools.islice(field.__dict__.values(), 16):
                        if string:
                            self._f.write(bytes_util.to_bytes(self._header.string_block_size))
                            string = (string + '\0').encode('utf-8')
                            new_strings.append(string)
                            self._header.string_block_size += len(string)
                        else:
                            self._f.write(bytes_util.to_bytes(0))
                    self._f.write(bytes_util.to_bytes(field.flag))
                else:
                    self._f.write(bytes_util.to_bytes(field))

        self._f.write(self._string_block)
        self._f.write(b''.join(new_strings))

        self._f.seek(0)
        self._f.write(self._header.to_bytes())

    def find(self, entry):
        int32_size = 4

        low = 0
        high = self._header.record_count - 1
        while low <= high:
            i = low + ((high - low) // 2)
            self._f.seek(self._header.size + self._header.record_size * i)
            found_entry = bytes_util.to_int(self._f.read(int32_size))
            if found_entry == entry:
                self._f.seek(-int32_size, 1)
                return self._record_reader.read_record(self._string_block, self._f)
            elif found_entry < entry:
                low = i + 1
            else:
                high = i - 1
        raise ValueError(f'{entry} is not in this dbc file')

    def _size(self):
        return self._header.record_count * self._header.record_size

    def __iter__(self):
        self._f.seek(self._header.size)
        return self

    def __next__(self):
        if self._f.tell() < self._size():
            return self._record_reader.read_record(self._string_block, self._f)
        raise StopIteration()

