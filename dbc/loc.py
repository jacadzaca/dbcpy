from dataclasses import dataclass

def read_dbc_string(offset, strings):
    string = []
    while strings[offset] != 0:
        string.append(chr(strings[offset]))
        offset += 1
    return ''.join(string)

@dataclass
class Loc():
    en_us: str
    en_gb: str
    ko_KR: str
    fr_FR: str
    de_DE: str
    en_CN: str
    zh_CN: str
    en_TW: str
    zh_TW: str
    es_ES: str
    es_MX: str
    ru_RU: str
    pt_PT: str
    pt_BR: str
    it_IT: str
    unknown: int
    flag: int

