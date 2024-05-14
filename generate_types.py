import quack_front
import json

def type_inference(n: quack_front.ASTNode, _master_dict: dict = {}) -> dict:
    if isinstance(n, quack_front.ProgramNode):
        for c in n.children:
            _master_dict[c.name] = type_inference(c, _master_dict)
    elif isinstance(n, quack_front.QuackClass):
        for m in n.children:
            _master_dict[f"{n.name}"].append(type_inference(m))
    elif isinstance(n, quack_front.MethodNode):
        signature = (n.returns, [])
        for f in n.formals:
            signature[1].append(f.var_type)
            _master_dict[f"{f.var_name}"] = f.var_type
        for stmt in n.body.children:
            type_inference(stmt, _master_dict)
        return _master_dict
    elif isinstance(n, quack_front.AssignmentNode):
        if n.assign_type:
            return {n.name: n.assign_type}
        elif n.name in _master_dict.keys():
            return {}
        else:
            return {n.name: type_inference(n.rhs)}
        
    return {}

