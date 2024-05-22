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
        return self.name

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
            reciever_type = list(self.receiver.infer_type(_master_record).values())[0]
        self.receiver_type = reciever_type
        if self.name not in _master_record[f"{reciever_type}"]["methods"].keys():
            raise ValueError(f"Cannot find {self.str()} in {reciever_type} class")
        return {f"{self.str()}": _master_record[f"{reciever_type}"]["methods"][f"{self.name.__str__()}"]['ret']}
    
    def gen_code(self, code: list[str]):
        for p in self.params: # Load all parameters before call
            p.r_eval(code)
        if isinstance(self.receiver, ClassNode):
            util.MR['current_method_arity'] += 1
            code.append(f"new {self.receiver.name}")
            code.append(f"call {self.receiver.name}:$constructor")
        else:
            self.receiver.r_eval(code)
            reciever_type = list(self.receiver.infer_type(util.MR).values())[0]
            util.MR['current_method_arity'] -= self.params.__len__() - 1
            code.append(f"call {reciever_type}:{self.name}")
            if util.MR[reciever_type]["methods"][self.name]['ret'] == 'Nothing':
                code.append("pop")


