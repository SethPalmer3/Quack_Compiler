from . import *

class OrNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right
        self.children = [left, right]
        self.uuid = 0

    def __str__(self) -> str:
        return f"{self.left.__str__()} or {self.right.__str__()}"
    
    def infer_type(self, _master_record: dict = ...) -> dict:
        # lhs = list(self.left.infer_type(_master_record).values())[0]
        # rhs = list(self.right.infer_type(_master_record).values())[0]
        # TODO: Add checks for lhs and rhs being boolean
        self.uuid += 1
        return {f"or_{self.uuid}": "Bool"}

