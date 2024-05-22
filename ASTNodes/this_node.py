from . import *


class ThisNode(ASTNode):
    def __init__(self):
        self.children = []

    def str(str):
        return '$'

    def __str__(self) -> str:
        return f'{ZERO_SPACE_CHAR}this'

    def r_eval(self, buffer: list[str]):
        util.MR['current_method_arity'] += 1
        buffer.append("load $")

    def gen_code(self, code: list[str]):
        util.MR['current_method_arity'] += 1
        code.append("load $")

    def infer_type(self, _master_record: dict = ...) -> dict:
        return {'$': _master_record['current_class']}

