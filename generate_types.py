from .quack_front import *
from .quack_constants import *

def eval_type(n: ASTNode) -> str|None:
    if isinstance(n, int):
        return INT
    return None

def update_type_table(n: ASTNode, type_table: dict[str, str]):
    if isinstance(n, AssignmentNode):
        evaluated_rhs = eval_type(n.rhs)
        # TODO: implement least common class
        if n.assign_type is not None and n.assign_type != evaluated_rhs:
            raise TypeError(f"Right hand side does not match declared type of {n.name}")
        else:
            type_table[n.name] = evaluated_rhs
    elif isinstance(n, VariableRefNode):
        if n.name not in type_table.keys():
            raise TypeError(f"Undeclared variable {n.name}")
    # elif isinstance(n, MethodCallNode):
        # TODO: Get return value of method call
    elif isinstance(n, BlockNode):
        for stmt in n.children:
            update_type_table(stmt, type_table)


def generate_method_type_table(m: MethodNode) -> dict[str, str]:
    type_table = {}
    for stmt in m.children:
        update_type_table(stmt, type_table)

    return type_table
