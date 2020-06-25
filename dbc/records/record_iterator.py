import dbc.bytes_util as bytes_util
from typing import BinaryIO
from dbc.dbc_header import DBCHeader


class RecordIterator():
    def __init__(self, file: BinaryIO, dbc_header: DBCHeader,
                 record_creator, field_size: int):
        self._f = file
        self._header = dbc_header
        self._record_creator = record_creator
        self._field_size = field_size

    def __iter__(self):
        self._f.seek(self._header.size)
        return self

    def __next__(self):
        if self._f.tell() > self._calculate_size():
            raise StopIteration
        return self._record_creator(*self._read_record())

    # we need to calculate size every time,
    # becouse the number of records can change
    def _calculate_size(self):
        return self._header.record_count * self._header.record_size

    def _read_record(self):
        return [bytes_util.to_int(self._f.read(self._field_size))
                for _ in range(self._header.field_count)]

    """
    when using, keep in mind that @file_handler's
    cursor is being manged by this class
    @record_cretor is a function returing an instance
    of the record that should be returned during the iteration
    """
    @classmethod
    def create(cls, file_handler: BinaryIO,
               dbc_header: DBCHeader, record_creator):
        field_size = dbc_header.record_size // dbc_header.field_count
        return cls(file_handler, dbc_header, record_creator, field_size)
