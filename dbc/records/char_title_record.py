import bytes_util as bytes_util
from dataclasses import dataclass
import loc
from loc import Loc


@dataclass
class CharTitleRecord():
    entry: int
    unknown: int
    male_title: Loc
    female_title: Loc
    title_mask_id: int

    @classmethod
    def read_record(_, f):
        field_count = 37
        int32_size = 4
        return (bytes_util.to_int(f.read(int32_size)) for _ in range(field_count))

    @classmethod
    def create_record(cls, strings, entry, unknown, *args):
        male_title = (loc.read_dbc_string(offset, strings) for offset in args[0:16])
        title_male = Loc(*male_title, args[16])
        female_title = (loc.read_dbc_string(offset, strings) for offset in args[17:33])
        title_female = Loc(*female_title, args[33])
        title_mask_id = args[34]
        return cls(entry, unknown, title_male, title_female, title_mask_id)

