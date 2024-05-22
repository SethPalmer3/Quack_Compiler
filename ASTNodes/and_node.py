from . import *

class AndNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right
        self.children = [left, right]
        self.true_label = uuid_gen.gen_label("and_")
        self.end_label = uuid_gen.gen_label("and_end_")

    def str(self) -> str:
        return f"{self.left.str()} and {self.right.str()}"

    def __str__(self) -> str:
        return f"{ZERO_SPACE_CHAR}{self.left.__str__()} and {self.right.__str__()}"

    def c_eval(self, true_branch: str, false_branch: str, buffer: list[str]):
        continue_and = uuid_gen.gen_label("continue_and")
        self.left.c_eval(continue_and, false_branch, buffer)
        buffer.append(f"{continue_and}:")
        self.right.c_eval(true_branch, false_branch, buffer)
    
    def infer_type(self, _master_record: dict = ...) -> dict:
        # TODO: add checks for left and right hand sides
        left_type = list(self.left.infer_type(_master_record).values())[0]
        right_type = list(self.right.infer_type(_master_record).values())[0]
        if left_type != "Bool" or right_type != "Bool":
            raise ValueError("Left or right `and` expressions do not evaluate to booleans")
        return {self.true_label: "Bool"}
    
    def gen_code(self, code: list[str]):
        short_and = uuid_gen.gen_label("short_and")
        code.append("const false")
        self.left.gen_code(code)
        code.append(f"jump_ifnot {short_and}")
        code.append(f"pop")
        self.right.gen_code(code)
        code.append(f"{short_and}:")
        
