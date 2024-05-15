from . import *

class MemberNode(ASTNode):
    def __init__(self, member_name: str):
        self.member_name = member_name

    def __str__(self) -> str:
        return f"{self.member_name}"
    
    


