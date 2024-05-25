from . import *
from .class_node import ClassNode

class MethodCallNode(ASTNode):
    """Node for calling a method"""
    def __init__(self, name: str, receiver: ASTNode, params: list[ ASTNode ]):
        self.name = name
        self.receiver = receiver
        self.params = params
        self.children = params

    def str(self) -> str:
        # return self.name
        return f"{self.receiver.str()}.{self.name}({ ','.join([p.str() for p in self.params]) })"

    def __str__(self) -> str:
        if isinstance(self.receiver, ClassNode):
            ret_str = f"{ZERO_SPACE_CHAR}{self.receiver.name}("
        else:
            ret_str = f"{ZERO_SPACE_CHAR}{self.receiver.__str__()}.{self.name}("
        for i in range(len(self.params)):
            ret_str += remove_zero_size_char(self.params[i].__str__())
            if i < len(self.params) - 1:
                ret_str += ", "
        return ret_str + ")"

    def infer_type(self, _master_record: dict = ...) -> dict:
        if isinstance(self.receiver, ClassNode):
            reciever_type = self.receiver.name
        else:
            reciever_type = retrieve_type(self.receiver, _master_record)
        self.receiver_type = reciever_type
        if self.name == _master_record[CURRENT_METHOD] and reciever_type == _master_record[CURRENT_CLASS]:
            _master_record[reciever_type][METHODS][self.name][RECURSIVE] = True
        if self.name not in _master_record[reciever_type][METHODS].keys() and self.name != _master_record[CURRENT_METHOD]:
            raise ValueError(f"Cannot find {self.str()} in {reciever_type} class")
        return {f"{self.str()}": _master_record[f"{reciever_type}"][METHODS][f"{self.name.__str__()}"][RET]}
    
    def gen_code(self, code: list[str]):
        method_class = retrieve_type(self.receiver, util.MR)
        method_params = util.MR[method_class][METHODS][self.name][PARAMS]
        for method_param, given_param in zip(method_params, self.params): # Load all parameters before call
            given_param_type = retrieve_type(given_param, util.MR) 
            if method_param == given_param_type:
                given_param.r_eval(code)
            else:
                raise TypeError(f"Method {self.name} excpected parameter type {method_param} but got {given_param_type}")
        if isinstance(self.receiver, ClassNode):  # Instantiate a class
            util.MR[CURRENT_METHOD_ARITY] += 1
            code.append(f"new {self.receiver.name}")
            code.append(f"call {self.receiver.name}:$constructor")
        elif isinstance(self.receiver, ThisNode):  # inner class call
            self.receiver.r_eval(code)
            code.append(f"call $:{self.name}")
        else:  # Everything else
            self.receiver.r_eval(code)
            reciever_type = retrieve_type(self.receiver, util.MR)
            util.MR[CURRENT_METHOD_ARITY] -= self.params.__len__() - 1
            code.append(f"call {reciever_type}:{self.name}")
            if util.MR[reciever_type][METHODS][self.name][RET] == 'Nothing':
                code.append("pop")


