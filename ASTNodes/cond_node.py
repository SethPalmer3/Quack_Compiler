from . import *

class CondNode(ASTNode):
    """Boolean condition. It can evaluate to jumps,
    but in this grammar it's just a placeholder.
    """
    def __init__(self, cond: str):
        self.cond = cond

    def __str__(self):
        return f"{self.cond}"
    
