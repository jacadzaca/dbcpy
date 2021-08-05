import dbcpy.loc as loc
import dbcpy.bytes_util as bytes_util
from dbcpy.loc import Loc

class RecordReader():
    def __init__(self, record_type):
        self._record_type = record_type

    def read_record(self, strings, f):
        int32_size = 4
        float_size = 4
        record_fields = []
        for field_type in self._record_type.field_types:
            if field_type is int:
                record_fields.append(bytes_util.to_int(f.read(int32_size)))
            if field_type is float:
                record_fields.append(bytes_util.to_float(f.read(float_size)))
            elif field_type is Loc:
                raw_loc = [bytes_util.to_int(f.read(int32_size)) for _ in range(17)]
                strs = (loc.read_dbc_string(offset, strings) for offset in raw_loc[0:16])
                record_fields.append(Loc(*strs, raw_loc[16]))
        return self._record_type(*record_fields)

