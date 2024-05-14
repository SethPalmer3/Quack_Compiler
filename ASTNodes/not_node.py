from . import *

class NotNode(ASTNode):
    def __init__(self, e: ASTNode):
        self.e = e
        self.children = [e]
        self.uuid = 0

    def __str__(self) -> str:
        return f"not {self.e.__str__()}"

    def infer_type(self, _master_record: dict = ...) -> dict:
        self.uuid += 1
        return {f"not_{self.uuid}": "Bool"}

