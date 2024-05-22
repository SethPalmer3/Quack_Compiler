from . import *
from type_inference import LCA

class AssignmentNode(ASTNode):
    """Placeholder ... not defined in grammar yet"""
    def __init__(self, l_expr: ASTNode, assign_type: str, rhs:ASTNode):

        self.l_expr = l_expr
        self.assign_type = assign_type
        self.rhs = rhs
        self.children = [rhs]

    def str(self):
        if self.assign_type is None:
            return f"{self.l_expr.__str__()} = {remove_zero_size_char(self.rhs.__str__())}"
        return f"{self.l_expr.__str__()}: {self.assign_type} = {remove_zero_size_char(self.rhs.__str__())}"

    def __str__(self):
        if self.assign_type is None:
            return f"{ZERO_SPACE_CHAR}{self.l_expr.__str__()} = {remove_zero_size_char(self.rhs.__str__())}"
        return f"{ZERO_SPACE_CHAR}{self.l_expr.__str__()}: {self.assign_type} = {remove_zero_size_char(self.rhs.__str__())}"
    
    def infer_type(self, _master_record: dict = ...) -> dict:

        if self.assign_type:
            # TODO: Add check for declared type and given rhs
            return {self.l_expr.str(): self.assign_type.__str__()}
        elif self.l_expr.str() in _master_record['temp'].keys():
            self.assign_type = _master_record["temp"][f"{self.l_expr.str()}"]
            calc_type = list(self.rhs.infer_type(_master_record).values())[0]
            new_type = LCA(self.assign_type, calc_type, _master_record)
            self.assign_type = new_type
            _master_record["temp"][f"{self.l_expr.str()}"] = new_type
            
            return {}
        elif isinstance(self.l_expr, FieldRefNode):
            class_type = list(self.l_expr.infer_type(_master_record).values())[0] # Get which class this field is referring to
            calc_type = list(self.rhs.infer_type(_master_record).values())[0] # Calculate the type from right hand side
            _master_record[class_type]['fields'][self.l_expr.name] = calc_type # update master record with new type
            self.assign_type = calc_type
            return {}
        else:
            assign_type = list(self.rhs.infer_type(_master_record).values())[0]
            self.assign_type = assign_type
            return {self.l_expr.str(): assign_type}
    
    def gen_code(self, code: list[str]):
        self.rhs.r_eval(code)
        self.l_expr.gen_code(code)
