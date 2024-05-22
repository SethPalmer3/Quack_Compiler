from . import *

class FieldRefNode(ASTNode):
    """Reference to a variable in an expression.
    This will typically evaluate to a 'load' operation.
    """
    def __init__(self, r_expr: ASTNode, name: str):
        assert isinstance(name, str)
        self.name = name
        self.r_expr = r_expr
        self.children = [r_expr]

    def r_eval(self, buffer: list[str]):
        self.r_expr.r_eval(buffer)
        current_class = util.MR['current_class']
        current_method = util.MR['current_method']
        try:
            receiver_type = util.MR[current_class]['methods'][current_method]['body'][self.r_expr.str()]
        except:
            receiver_type = util.MR[current_class]['methods'][current_method]['params'][self.r_expr.str()]

        util.MR['current_method_arity'] += 1;
        buffer.append(f"load_field {receiver_type}:{self.name}")

    def str(self):
        return f"{self.r_expr.str()}.{self.name}"

    def __str__(self):
        return ZERO_SPACE_CHAR + f"{self.r_expr.str()}.{self.name}"

    def infer_type(self, _master_record: dict = ...) -> dict:
        class_type = list(self.r_expr.infer_type(_master_record).values())[0]
        if self.name in _master_record[class_type]['fields'].keys():
            return {self.name: _master_record[class_type]['fields'][self.name]}
        else:
            _master_record[class_type]['fields'][self.name] = '' # Because we don't know what this is assigned to yet
            return {self.str(): class_type}

    def gen_code(self, code: list[str]):
        base_type = list(self.r_expr.infer_type(util.MR).values())[0]
        self.r_expr.r_eval(code)
        util.MR['current_method_arity'] -= 2
        if isinstance(self.r_expr, ThisNode):
            code.append(f"store_field $:{self.name}")
        else:
            code.append(f"store_field {base_type}:{self.name}")
