from . import log, flatten
from typing import Callable

def ignore(node: "ASTNode", visit_state):
    log.debug(f"No visitor action at {node.__class__.__name__} node")
    return

def retrieve_type(n: "ASTNode", _master_record: dict):
    inf_type = n.infer_type(_master_record)
    try:
        if n.__getattribute__("name") and n.__getattribute__("name") in inf_type.keys():
            return inf_type[n.__getattribute__("name")]

    except:
        if n.str() in inf_type.keys():
            return inf_type[n.str()]
        else:
            return list(inf_type.values())[0]

class ASTNode:
    """Abstract base class"""
    def __init__(self):
        self.children = []    # Internal nodes should set this to list of child nodes

    # Visitor-like functionality for walking over the AST. Define default methods in ASTNode
    # and specific overrides in node types in which the visitor should do something
    def walk(self, visit_state, pre_visit: Callable =ignore, post_visit: Callable=ignore):
        pre_visit(self, visit_state)
        for child in flatten(self.children):
            log.debug(f"Visiting ASTNode of class {child.__class__.__name__}")
            child.walk(visit_state, pre_visit, post_visit)
        post_visit(self, visit_state)


    # a slightly modified version of the string used for code generation
    def str(self) -> str:
        return self.__str__()

    # Example walk to gather method signatures
    def method_table_visit(self, visit_state: dict):
        ignore(self, visit_state)

    def r_eval(self, buffer: list[str]):
        self.gen_code(buffer)

    def c_eval(self, true_branch: str, false_branch: str, buffer: list[str]):
        raise NotImplementedError(f"c_eval not implemented for node type {self.__class__.__name__}")

    def infer_type(self, _master_record: dict ={}) -> dict:
        pass

    def gen_code(self, code: list[str]):
        raise NotImplementedError(f"Gen code was not implemented for {self.__class__.__name__}")

