from . import *
from .class_node import ClassNode

class MethodCallNode(ASTNode):
    """Node for calling a method"""
    def __init__(self, name: str, receiver: ASTNode, params: list[ ASTNode ]):
        self.name = name
        self.receiver = receiver
        self.params = params
        self.children = params
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
        reciever_type = list(self.receiver.infer_type(_master_record).values())[0]
        self.receiver_type = reciever_type
        if self.name not in _master_record[f"{reciever_type}"]["methods"].keys():
            raise ValueError(f"Cannot find {self.name} in {reciever_type} class")
        return {f"{self.name.__str__()}": _master_record[f"{reciever_type}"]["methods"][f"{self.name.__str__()}"]['ret']}
    
    def gen_code(self, code: list[str]):
        for p in self.params: # Load all parameters before call
            p.gen_code(code)
        if isinstance(self.receiver, ClassNode):
            code.append(f"new {self.receiver.name}")
        else:
            self.receiver.gen_code(code)
            reciever_type = list(self.receiver.infer_type(util.MR).values())[0]
            code.append(f"call {reciever_type}:{self.name}")


