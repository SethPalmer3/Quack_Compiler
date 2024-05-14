from . import *

class VariableRefNode(ASTNode):
    """Reference to a variable in an expression.
    This will typically evaluate to a 'load' operation.
    """
    def __init__(self, name: str):
        assert isinstance(name, str)
        self.name = name
        self.children = []

    def __str__(self):
        return ZERO_SPACE_CHAR + self.name

    def infer_type(self, _master_record: dict = ...) -> dict:
        return {}
