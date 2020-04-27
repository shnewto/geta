from enum import Enum, auto
import names


class NameType(Enum):
    FIRST = auto()
    LAST = auto()
    FULL = auto()


def generateName(nameType: NameType):
    if nameType == nameType.FIRST:
        return names.get_first_name()
    elif nameType == nameType.LAST:
        return names.get_last_name()
    elif nameType == nameType.FULL:
        return names.get_full_name()
