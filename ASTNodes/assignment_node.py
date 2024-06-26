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
        cc = util.MR[CURRENT_CLASS]
        cm = util.MR[CURRENT_METHOD]
        try:
            assignment_type = util.MR[cc][METHODS][cm][BODY][self.l_expr.str()]
        except:
            assignment_type = util.MR[cc][METHODS][cm][PARAMS][self.l_expr.str()]

        return f"{ZERO_SPACE_CHAR}{self.l_expr.__str__()}: {assignment_type} = {remove_zero_size_char(self.rhs.__str__())}"
    
    def infer_type(self, _master_record: dict = ...) -> dict:

        if self.assign_type:
            return {self.l_expr.str(): self.assign_type.__str__()}
        elif self.l_expr.str() in _master_record[TEMP].keys():
            self.assign_type = _master_record[TEMP][f"{self.l_expr.str()}"]
            calc_type = retrieve_type(self.rhs, _master_record)
            new_type = LCA(self.assign_type, calc_type, _master_record)
            self.assign_type = new_type
            _master_record[TEMP][f"{self.l_expr.str()}"] = new_type
            
            return {}
        elif isinstance(self.l_expr, FieldRefNode):
            class_type = retrieve_type(self.l_expr, _master_record) # Get which class this field is referring to
            calc_type = retrieve_type(self.rhs, _master_record) # Calculate the type from right hand side
            _master_record[class_type][FIELDS][self.l_expr.name] = calc_type # update master record with new type
            self.assign_type = calc_type
            return {}
        else:
            assign_type = retrieve_type(self.rhs, _master_record)
            self.assign_type = assign_type
            return {self.l_expr.str(): assign_type}
    
    def gen_code(self, code: list[str]):
        self.rhs.r_eval(code)
        self.l_expr.gen_code(code)
