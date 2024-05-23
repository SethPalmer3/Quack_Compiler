from . import *

class VariableRefNode(ASTNode):
    """Reference to a variable in an expression.
    This will typically evaluate to a 'load' operation.
    """
    def __init__(self, name: str):
        assert isinstance(name, str)
        self.name = name
        self.children = []

    def r_eval(self, buffer: list[str]):
        util.MR[CURRENT_METHOD_ARITY] += 1;
        buffer.append(f"load {self.name}")

    def str(self):
        return self.name

    def __str__(self):
        return ZERO_SPACE_CHAR + self.name

    def infer_type(self, _master_record: dict = ...) -> dict:

        try:
            if self.name in _master_record[TEMP].keys():
                return {self.name: _master_record[TEMP][self.name]}
        except:
            current_class = util.MR[CURRENT_CLASS]
            current_method = util.MR[CURRENT_METHOD]
            if self.name in util.MR[current_class][FIELDS].keys():
                return {self.name: util.MR[current_class][FIELDS][self.name]}
            elif self.name in util.MR[current_class][METHODS][current_method][PARAMS].keys():
                return {self.name: util.MR[current_class][METHODS][current_method][PARAMS][self.name]}
            elif self.name in util.MR[current_class][METHODS][current_method][BODY].keys():
                return {self.name: util.MR[current_class][METHODS][current_method][BODY][self.name]}
            else:
                raise ValueError(f"Cannot find variable {self.name}")

    def gen_code(self, code: list[str]):
        util.MR[CURRENT_METHOD_ARITY] -= 1
        code.append(f"store {self.name}")
