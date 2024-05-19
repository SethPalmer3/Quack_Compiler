from . import *

class WhileNode(ASTNode):
    """Abstract while loop"""
    def __init__(self, cond: ASTNode, stmts: ASTNode):
        self.cond = cond
        self.stmts = stmts
        self.loop_label = f"while_{uuid_gen.gen_uuid()}"
        self.cond_label = f"cond_{uuid_gen.gen_uuid()}"
        self.children = [cond, stmts]

    def __str__(self) -> str:
        return f"""{ZERO_SPACE_CHAR}while {remove_zero_size_char(self.cond.__str__())} {LB}
{append_zero_size_char(self.stmts.__str__())}
{ZERO_SPACE_CHAR}{RB}"""

    def infer_type(self, _master_record: dict ={}) -> dict:
        return {}

    def gen_code(self, code: list[str]):
        code.append(f"jump {self.cond_label}")
        code.append(f"{ self.loop_label }:")
        self.stmts.gen_code(code)
        code.append(f"{ self.cond_label }:")
        self.cond.gen_code(code)
        code.append(f"jump_if {self.loop_label}")


