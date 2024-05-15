from . import *
import uuid

class MethodNode(ASTNode):
    def __init__(self, name: str, formals: list[ASTNode],
                 returns: str, body: ASTNode, return_stmt: ASTNode|None=None):
        self.name = name
        self.formals = formals
        self.returns = returns
        self.body = body
        self.return_stmt = return_stmt
        if not self.return_stmt:
            self.return_stmt = ConstantNode(None)
        self.children = [formals, body, self.return_stmt]

    def __str__(self):
        formals_str = ", ".join([str(fm) for fm in self.formals])
        full_ret =  f"""
{ZERO_SPACE_CHAR}/* method */ 
{ZERO_SPACE_CHAR}def {self.name}({formals_str}): {self.returns} {LB}
{append_zero_size_char(self.body.__str__())}
{ZERO_SPACE_CHAR}{RB} /* End of method {self.name} */"""
        return full_ret

    # Add this method to the symbol table
    def method_table_visit(self, visit_state: dict):
        clazz = visit_state["current_class"]
        if self.name in visit_state[clazz]["methods"]:
            raise Exception(f"Redeclaration of method {self.name} not permitted")
        params = [formal.var_type for formal in self.formals]
        visit_state[clazz]["methods"][self.name] = { "params": params, "ret": self.returns }

    def infer_type(self, _master_record: dict = ...) -> dict:

        _master_record["temp"] = {}
        local_scope = {'params': [  ], 'ret': self.returns.__str__(), 'body': {}}
        for f in self.formals:
            _master_record['temp'][f'{f.var_name}'] = f.var_type.__str__()
            local_scope['params'].append(f.var_type.__str__())
        for stmt in self.body.children:
            loc_types = stmt.infer_type(_master_record) 
            local_scope['body'].update(loc_types)
            _master_record["temp"].update(loc_types)
        return local_scope
    
    def gen_code(self, code: list[str]):
        code.append(f".method {self.name}")
        code.append(f"enter")
        for formal in self.formals:
            formal.gen_code(code)
        self.body.gen_code(code)
        # self.return_stmt.gen_code(code)
        code.append(f"return 0")


