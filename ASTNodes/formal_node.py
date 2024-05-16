from . import *

class FormalNode(ASTNode):
    def __init__(self, var_name: str, var_type: str):
        self.var_name = var_name
        self.var_type = var_type
        self.children = []

    def __str__(self):
        return f"{self.var_name}: {self.var_type}"

    def infer_type(self, _master_record: dict = ...) -> dict:
        return {self.var_name: self.var_type}
    
    def gen_code(self, code: list[str]):
        return self.var_name
