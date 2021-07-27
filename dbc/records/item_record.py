import bytes_util as bytes_util
from dataclasses import dataclass
from records.__init__ import NO_STRING


@dataclass
class ItemRecord():
    entry: int
    clazz: int
    sub_class: int
    sound: int
    material_id: int
    display_id: int
    slot_id: int
    sheat_id: int

    def to_bytes(self):
        return b''.join([bytes_util.to_bytes(value, 4)
                for value in self.__dict__.values()])

    def strings(self):
        return NO_STRING
