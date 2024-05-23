from . import *

class ClassNode(ASTNode):
    def __init__(self, name: str, formals: list[ASTNode],
                 super_class: str,
                 methods: list[ASTNode],
                 block: ASTNode):
        from .method_node import MethodNode
        self.name = name
        self.super_class = super_class
        self.methods = methods
        self.constructor = MethodNode("$constructor", formals, name, block)
        self.children = methods +  [self.constructor]

    def __str__(self):
        formals_str = ", ".join([str(fm) for fm in self.constructor.formals])
        methods_str = "\n".join([f"{method.__str__()}" for method in self.methods])
        full_ret = f"""class {self.name}({formals_str}){LB}
{append_zero_size_char(methods_str)}
{ZERO_SPACE_CHAR}/* statements as a constructor */
{append_zero_size_char(self.constructor.__str__())}
{RB} /* end class {self.name} */"""
        return full_ret

    # Example walk to gather method signatures
    def method_table_visit(self, visit_state: dict):
        """Create class entry in symbol table (as a preorder visit)"""
        if self.name in visit_state:
            raise Exception(f"Shadowing class {self.name} is not permitted")
        visit_state[CURRENT_CLASS] = self.name
        visit_state[self.name] = {
            "super": self.super_class,
            FIELDS: [],
            METHODS: {}
        }

    def infer_type(self, _master_record: dict = ...) -> dict:
        _master_record[f"{self.name.__str__()}"] = {}
        _master_record[f"{self.name.__str__()}"]['super'] = self.super_class.__str__()
        _master_record[f"{self.name.__str__()}"][METHODS] = {}
        _master_record[f"{self.name.__str__()}"][FIELDS] = {}
        _master_record[CURRENT_CLASS] = self.name.__str__()
        for m in self.children:
            m.infer_type(_master_record)
        return {self.name: self.name}
    
    def gen_code(self, code: list[str]):
        util.MR[CURRENT_CLASS] = self.name
        code.append(f".class {self.name}:{self.super_class}")
        for f in util.MR[self.name][FIELDS].keys():
            code.append(f".field {f}")
        for child in self.children:
            child.gen_code(code)
        code.append(f"{ZERO_SPACE_CHAR}")
