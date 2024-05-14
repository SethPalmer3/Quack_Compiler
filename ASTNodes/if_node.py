from . import *

class IfStmtNode(ASTNode):
    def __init__(self,
                 cond: ASTNode,
                 thenpart: ASTNode,
                 elsepart: ASTNode):
        self.cond = cond
        self.thenpart = thenpart
        self.elsepart = elsepart
        self.children = [cond, thenpart, elsepart]

    def __str__(self):
        return f"""
{ZERO_SPACE_CHAR}if {remove_zero_size_char(self.cond.__str__())} {LB}
{append_zero_size_char(self.thenpart.__str__())}
{ZERO_SPACE_CHAR}{RB} else {LB}
{append_zero_size_char(self.elsepart.__str__())}
{ZERO_SPACE_CHAR}{RB}"""
    
    def infer_type(self, _master_record: dict = ...) -> dict:
        # cond = list(self.cond.infer_type(_master_record).values())[0]
        # TODO: Add check for condition
        # TODO: Possibly update thenpart and elsepart
        return {}
