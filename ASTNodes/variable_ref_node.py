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
        util.MR['current_method_arity'] += 1;
        buffer.append(f"load {self.name}")

    def str(self):
        return self.name

    def __str__(self):
        return ZERO_SPACE_CHAR + self.name

    def infer_type(self, _master_record: dict = ...) -> dict:

        try:
            if self.name in _master_record['temp'].keys():
                return {self.name: _master_record['temp'][self.name]}
        except:
            current_class = util.MR['current_class']
            current_method = util.MR['current_method']
            if self.name in util.MR[current_class]['fields'].keys():
                return {self.name: util.MR[current_class]['fields'][self.name]}
            elif self.name in util.MR[current_class]['methods'][current_method]['params']:
                return {self.name: util.MR[current_class]['methods'][current_method]['params'][self.name]}
            elif self.name in util.MR[current_class]['methods'][current_method]['body'].keys():
                return {self.name: util.MR[current_class]['methods'][current_method]['body'][self.name]}
            else:
                raise ValueError(f"Cannot find variable {self.name}")

    def gen_code(self, code: list[str]):
        util.MR['current_method_arity'] -= 2
        code.append(f"store {self.name}")
