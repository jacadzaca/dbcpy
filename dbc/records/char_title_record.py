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

    def to_bytes(self):
        return b''.join([bytes_util.to_bytes(value, 4)
                for value in self.__dict__.values()])

    @classmethod
    def create_from_bytes(cls, strings, entry, unknown, *args):
        male_title = tuple(loc.read_dbc_string(offset, strings) for offset in args[0:15])
        title_male = Loc(*(male_title + args[15:17]))
        female_title = tuple(loc.read_dbc_string(offset, strings) for offset in args[17:32])
        title_female = Loc(*(female_title + args[32:34]))
        title_mask_id = args[34]
        return cls(entry, unknown, title_male, title_female, title_mask_id)

