from . import *


class ReturnNode(ASTNode):
    def __init__(self, e: ASTNode):
        self.return_expr = e
        self.children = [e]

    def str(self) -> str:
        return f"return {self.return_expr.str()}"
    
    def __str__(self) -> str:
        return f"{ZERO_SPACE_CHAR}return {self.return_expr.str()}"

    def infer_type(self, _master_record: dict = ...) -> dict:
        self.return_expr.infer_type(_master_record)
        return {}

    def gen_code(self, code: list[str]):
        self.return_expr.r_eval(code)
        current_class = util.MR[CURRENT_CLASS]
        current_method = util.MR[CURRENT_METHOD]
        num_args = util.MR[current_class][METHODS][current_method][PARAMS].__len__()
        code.append(f"return {num_args}")
