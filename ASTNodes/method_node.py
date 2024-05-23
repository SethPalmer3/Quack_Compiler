from . import *
import uuid

class MethodNode(ASTNode):
    def __init__(self, name: str, formals: list[ASTNode],
                 returns: str, body: ASTNode):
        self.name = name
        self.formals = formals
        self.returns = returns
        self.body = body
        self.children = [formals, body]

    def str(self):
        return self.name

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
        clazz = visit_state[CURRENT_CLASS]
        if self.name in visit_state[clazz][METHODS]:
            raise Exception(f"Redeclaration of method {self.name} not permitted")
        params = [formal.var_type for formal in self.formals]
        visit_state[clazz][METHODS][self.name] = { PARAMS: params, RET: self.returns }

    def infer_type(self, _master_record: dict = ...) -> dict:

        _master_record[TEMP] = {}
        _master_record[CURRENT_METHOD] = self.name
        current_class = _master_record[CURRENT_CLASS]

        _master_record[current_class][METHODS][self.name] = {PARAMS: {}, RET: self.returns.__str__(), BODY: {}, RECURSIVE: False}
        for f in self.formals:  # Construct parameters and their types
            _master_record[TEMP][f'{f.var_name}'] = f.var_type.__str__()
            _master_record[current_class][METHODS][self.name][PARAMS][f'{f.var_name}'] = f.var_type.__str__()
        for stmt in self.body.children:
            if isinstance(stmt, MethodCallNode) and stmt.name == self.name:
                _master_record[current_class][METHODS][self.name][RECURSIVE] = True
            else:
                loc_types = stmt.infer_type(_master_record) 
                if isinstance(stmt, AssignmentNode):
                    _master_record[current_class][METHODS][self.name][BODY].update(loc_types)
                    _master_record[TEMP].update(loc_types)
        return _master_record[current_class][METHODS][self.name]
    
    def gen_code(self, code: list[str]):
        util.MR[CURRENT_METHOD] = self.name
        util.MR[CURRENT_METHOD_ARITY] = 0
        current_class = util.MR[CURRENT_CLASS]
        if util.MR[current_class][METHODS][self.name][RECURSIVE]:
            code.append(f".method {self.name} forward")
        else:
            code.append(f".method {self.name}")

        local_scope = util.MR[current_class][METHODS][self.name]
        if self.formals.__len__() > 0:
            code_str = ".args "
            for i, p in enumerate(self.formals):
                if i < self.formals.__len__() - 1:
                    code_str += f"{p.var_name},"
                else:
                    code_str += f"{p.var_name}"
            code.append(code_str)

        if local_scope[BODY].keys().__len__() > 0: # Get local variables
            local_var_str =".local "
            for i, k in enumerate(local_scope[BODY].keys()):
                local_var_str += k.__str__()
                if i < local_scope[BODY].keys().__len__() - 1:
                    local_var_str += ","

            code.append(local_var_str)

        code.append(f"enter")
        self.body.gen_code(code)
        if self.returns == "Nothing":
            code.append("const nothing")
            code.append(f"return {self.formals.__len__()}")


