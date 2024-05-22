from . import *

class BlockNode(ASTNode):
    def __init__(self, stmts: list[ASTNode]):
        self.stmts = stmts
        self.children = stmts

    def __str__(self):
        return append_zero_size_char("\n".join([f"{str(stmt)};" for stmt in self.stmts]))
    
    def infer_type(self, _master_record: dict = ...) -> dict:
        pass

    def gen_code(self, code: list[str]):
        for child in self.children:
            child.r_eval(code)

