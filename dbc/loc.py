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
    ko_kr: str
    fr_fr: str
    de_de: str
    en_cn: str
    zh_cn: str
    en_tw: str
    zh_tw: str
    es_es: str
    es_mx: str
    ru_ru: str
    pt_pt: str
    pt_br: str
    it_it: str
    unknown: str
    flag: int

