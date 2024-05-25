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
        self.if_label = f"if_{uuid_gen.gen_uuid()}"
        self.else_label = f"else_{uuid_gen.gen_uuid()}"
        self.exit_label = f"fi_{uuid_gen.gen_uuid()}"

    def __str__(self):
        return f"""
{ZERO_SPACE_CHAR}if {remove_zero_size_char(self.cond.__str__())} {LB}
{append_zero_size_char(self.thenpart.__str__())}
{ZERO_SPACE_CHAR}{RB} else {LB}
{append_zero_size_char(self.elsepart.__str__())}
{ZERO_SPACE_CHAR}{RB}"""
    
    def infer_type(self, _master_record: dict = ...) -> dict:
        self.cond.infer_type(_master_record)
        self.thenpart.infer_type(_master_record)
        self.elsepart.infer_type(_master_record)
        return {}
    
    def gen_code(self, code: list[str]):
        if retrieve_type(self.cond, util.MR) != "Bool":
            raise TypeError(f"If statement excpected a boolean expression")
        self.cond.r_eval(code) # Evaluate condition
        code.append(f"jump_ifnot {self.else_label}") # Go to else if false
        self.thenpart.gen_code(code) # continue with if part if true
        code.append(f"jump {self.exit_label}") # Jump to end of statement when done
        code.append(f"{self.else_label}:") # Else label
        self.elsepart.gen_code(code) # Else code
        code.append(f"{self.exit_label}:") # Exit label



