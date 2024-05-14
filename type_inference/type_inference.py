from ASTNodes import *

# def type_inference(n: ASTNode, _master_dict: dict = {}) -> dict:
#     if isinstance(n, ProgramNode):
#         for c in n.children:
#             type_inference(c, _master_dict)
#         return _master_dict
#     elif isinstance(n, ClassNode):
#         _master_dict[f"{n.name.__str__()}"] = {}
#         _master_dict[f"{n.name.__str__()}"]['super'] = n.super_class.__str__()
#         _master_dict[f"{n.name.__str__()}"]['methods'] = {}
#         for m in n.children:
#             _master_dict[f"{n.name}"]['methods'][f"{m.name}"] = type_inference(m, _master_dict)
#     elif isinstance(n, MethodNode):
#         _master_dict["temp"] = {'params': []}
#         local_scope = {'params': [], 'ret': n.returns.__str__(), 'body': {}}
#         for f in n.formals:
#             _master_dict['temp']['params'].append(f.var_type.__str__())
#             local_scope['params'].append(f.var_type.__str__())
#         for stmt in n.body.children:
#             local_scope['body'].update(type_inference(stmt, _master_dict))
#         return local_scope
#     elif isinstance(n, AssignmentNode):
#         if n.assign_type:
#             return {n.name.__str__(): n.assign_type.__str__()}
#         elif n.name in _master_dict.keys():
#             return {}
#         else:
#             assign_type = list(type_inference(n.rhs, _master_dict).values())[0]
#             return {n.name.__str__(): assign_type}
#     elif isinstance(n, MethodCallNode):
#         reciever_type = list(type_inference(n.receiver, _master_dict).values())
#         return {f"{n.name.__str__()}": _master_dict[f"{reciever_type[0]}"]["methods"][f"{n.name.__str__()}"]['ret']}
#     elif isinstance(n, ConstantNode):
#         return {f"{n.value.__str__()}": n.const_type}
#         
#     return {}

def type_inference(n: ASTNode, _master_dict: dict = {}) -> dict:
    return n.infer_type(_master_dict)
