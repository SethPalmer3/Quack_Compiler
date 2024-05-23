from . import *

class TypecaseNode(ASTNode):
    def __init__(self, e: ASTNode, cases: ASTNode):
        self.e = e
        self.cases = cases
        self.children = [e, cases]

    def __str__(self):
        return f"""{ZERO_SPACE_CHAR}typecase {self.e.str()} {LB}
{self.cases.__str__()}
{RB}"""
    
    def infer_type(self, _master_record: dict = ...) -> dict:
        self.e.infer_type(_master_record)
        self.cases.infer_type(_master_record)
        return {}
