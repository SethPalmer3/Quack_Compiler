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
        current_class = util.MR[CURRENT_CLASS]
        current_method = util.MR[CURRENT_METHOD]
        try:
            receiver_type = util.MR[current_class][METHODS][current_method][BODY][self.r_expr.str()]
        except:
            receiver_type = util.MR[current_class][METHODS][current_method][PARAMS][self.r_expr.str()]

        util.MR[CURRENT_METHOD_ARITY] += 1;
        buffer.append(f"load_field {receiver_type}:{self.name}")

    def str(self):
        return f"{self.r_expr.str()}.{self.name}"

    def __str__(self):
        return ZERO_SPACE_CHAR + f"{self.r_expr.str()}.{self.name}"

    def infer_type(self, _master_record: dict = ...) -> dict:
        class_type = retrieve_type(self.r_expr, _master_record)
        if self.name in _master_record[class_type][FIELDS].keys():
            return {self.name: _master_record[class_type][FIELDS][self.name]}
        else:
            _master_record[class_type][FIELDS][self.name] = '' # Because we don't know what this is assigned to yet
            return {self.str(): class_type}

    def gen_code(self, code: list[str]):
        base_type = retrieve_type(self.r_expr, util.MR)
        self.r_expr.r_eval(code)
        util.MR[CURRENT_METHOD_ARITY] -= 2
        if isinstance(self.r_expr, ThisNode):
            code.append(f"store_field $:{self.name}")
        else:
            code.append(f"store_field {base_type}:{self.name}")
