STRING = "String"
INT = "Int"
BOOL = "Bool"
NOTHING = "Nothing"

class QuackType:
    def __init__(self, str_type: str) -> None:
        self.str_type = str_type

    def __eq__(self, value: object, /) -> bool:
        return self.str_type == value.__str__()

    def __str__(self) -> str:
        raise NotImplemented("Implement the string magic method")


class QString(QuackType):
    def __str__(self) -> str:
        return STRING
class QInt(QuackType):
    def __str__(self) -> str:
        return INT
class QBool(QuackType):
    def __str__(self) -> str:
        return BOOL
class QNothing(QuackType):
    def __str__(self) -> str:
        return NOTHING
