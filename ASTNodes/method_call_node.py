from . import *

class MethodCallNode(ASTNode):
    """Node for calling a method"""
    def __init__(self, name: str, receiver: ASTNode, params: list[ ASTNode ]):
        self.name = name
        self.receiver = receiver
        self.params = params
        self.children = params
    def __str__(self) -> str:
        ret_str = f"{ZERO_SPACE_CHAR}{self.name}("
        all_params = [self.receiver] + self.params
        for i in range(len(all_params)):
            ret_str += remove_zero_size_char(all_params[i].__str__())
            if i < len(all_params) - 1:
                ret_str += ", "
        return ret_str + ")"

    def infer_type(self, _master_record: dict = ...) -> dict:
        reciever_type = list(self.receiver.infer_type(_master_record).values())[0]
        if self.name not in _master_record[f"{reciever_type}"]["methods"]:
            raise ValueError(f"Cannot find {self.name} in {reciever_type} class")
        return {f"{self.name.__str__()}": _master_record[f"{reciever_type}"]["methods"][f"{self.name.__str__()}"]['ret']}

