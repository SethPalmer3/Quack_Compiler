from .ast_node import ASTNode
from .util import *

class ConstantNode(ASTNode):
    def __init__(self, e):
        self.value = e
        self.const_type = self.determine_type(e)
        self.children = []

    def determine_type(self, e):
        if e is None:
            self.const_type = "Nothing"
        try:
            self.value = int(e.__str__())
            return "Int"
        except ValueError as E:
            self.value = e.__str__()
            return "String"

    def __str__(self) -> str:
        return self.value.__str__()
    
    def infer_type(self, _master_record: dict = ...) -> dict:
        return {self.value.__str__(): self.const_type}
    
    def gen_code(self, code: list[str]):
        if self.value is None:
            return
        code.append(f"const {self.value}")
