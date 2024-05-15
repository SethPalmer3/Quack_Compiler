from . import *

class ExprNode(ASTNode):
    """Just identifiers in this stub"""
    def __init__(self, e: ASTNode):
        self.e = e
        self.children = [e]

    def __str__(self):
        return ZERO_SPACE_CHAR + str(self.e)

    def infer_type(self, _master_record: dict = ...) -> dict:
        inner_expr = list(self.e.infer_type(_master_record).values())[0]
        return {"expr": inner_expr}
    
    def gen_code(self, code: list[str]):
        self.e.gen_code(code)
