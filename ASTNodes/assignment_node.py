from . import *
from type_inference import LCA

class AssignmentNode(ASTNode):
    """Placeholder ... not defined in grammar yet"""
    def __init__(self, name: str, assign_type: str, rhs:ASTNode):

        self.name = name
        self.assign_type = assign_type
        self.rhs = rhs
        self.children = [rhs]

    def __str__(self):
        if self.assign_type is None:
            return f"{ZERO_SPACE_CHAR}{self.name} = {remove_zero_size_char(self.rhs.__str__())}"
        return f"{ZERO_SPACE_CHAR}{self.name}: {self.assign_type} = {remove_zero_size_char(self.rhs.__str__())}"
    
    def infer_type(self, _master_record: dict = ...) -> dict:

        if self.assign_type:
            # TODO: Add check for declared type and given rhs
            return {self.name.__str__(): self.assign_type.__str__()}
        elif self.name in _master_record['temp'].keys():
            self.assign_type = _master_record["temp"][f"{self.name}"]
            calc_type = list(self.rhs.infer_type(_master_record).values())[0]
            new_type = LCA(self.assign_type, calc_type, _master_record)
            self.assign_type = new_type
            _master_record["temp"][f"{self.name}"] = new_type
            
            return {}
        else:
            assign_type = list(self.rhs.infer_type(_master_record).values())[0]
            self.assign_type = assign_type
            return {self.name.__str__(): assign_type}
    
    def gen_code(self, code: list[str]):
        self.rhs.gen_code(code)
        code.append(f"store {self.name}")
