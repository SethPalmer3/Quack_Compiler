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
        # TODO: Add checks for lhs and rhs being boolean
        left_type = list(self.left.infer_type(_master_record).values())[0]
        right_type = list(self.right.infer_type(_master_record).values())[0]
        if left_type != "Bool" or right_type != "Bool":
            raise ValueError("Left or right `and` expressions do not evaluate to booleans")
        self.uuid += 1
        return {f"or_{self.uuid}": "Bool"}

