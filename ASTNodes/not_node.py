from . import *

class NotNode(ASTNode):
    def __init__(self, e: ASTNode):
        self.e = e
        self.children = [e]
        self.uuid = 0

    def __str__(self) -> str:
        return f"not {self.e.__str__()}"

    def infer_type(self, _master_record: dict = ...) -> dict:
        e_type = list(self.e.infer_type(_master_record).values())[0]
        if e_type != "Bool":
            raise ValueError("Left or right `and` expressions do not evaluate to booleans")
        self.uuid += 1
        return {f"not_{self.uuid}": "Bool"}

