from ASTNodes import *

def type_inference(n: ASTNode, _master_dict: dict = {}) -> dict:
    n.infer_type(_master_dict)
    util.MR = _master_dict
    return _master_dict
