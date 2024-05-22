from . import *

class OrNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right
        self.children = [left, right]
        self.true_label = f"or_{uuid_gen.gen_uuid()}"
        self.end_label = f"or_end_{uuid_gen.gen_uuid()}"


    def str(self) -> str:
        return f"{self.left.str()} or {self.right.str()}"

    def __str__(self) -> str:
        return f"{ZERO_SPACE_CHAR}{self.left.__str__()} or {self.right.__str__()}"
    
    def infer_type(self, _master_record: dict = ...) -> dict:
        # TODO: Add checks for lhs and rhs being boolean
        left_type = list(self.left.infer_type(_master_record).values())[0]
        right_type = list(self.right.infer_type(_master_record).values())[0]
        if left_type != "Bool" or right_type != "Bool":
            raise ValueError("Left or right `or` expressions do not evaluate to booleans")
        return {self.true_label: "Bool"}
    
    def gen_code(self, code: list[str]):
        short_or = uuid_gen.gen_label("short_or")
        code.append("const true")
        self.left.gen_code(code)
        code.append(f"jump_if {short_or}")
        code.append(f"pop")
        self.right.gen_code(code)
        code.append(f"{short_or}:")

