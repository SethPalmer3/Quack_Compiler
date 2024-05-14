from . import *

class ProgramNode(ASTNode):

    def __init__(self, classes: list[ASTNode], main_block: ASTNode):
        self.classes = classes
        main_class = ClassNode("$Main", [], "Obj", [], main_block)
        self.classes.append(main_class)
        self.children = self.classes

    def __str__(self) -> str:
        return "\n".join([str(c).replace(ZERO_SPACE_CHAR, TAB_CHAR) for c in self.classes]) + "\n"

    def infer_type(self, _master_record: dict = ...) -> dict:
        for c in self.children:
            c.infer_type(_master_record)
        if 'temp' in _master_record.keys():
            del _master_record['temp']
        MR = _master_record
        return _master_record
    
    def gen_code(self, code: list[str]):
        for child in self.children:
            child.gen_code(code)
