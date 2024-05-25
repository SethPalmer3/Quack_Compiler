from ASTNodes import *
# from deepdiff import DeepDiff

def type_inference(n: ASTNode, _master_dict: dict = {}) -> dict:
    # n.infer_type(_master_dict)
    # util.MR = _master_dict
    n.infer_type(_master_dict)
    # while DeepDiff(_master_dict, util.MR) != {}:
    while _master_dict != util.MR:
        print("Hi")
        n.infer_type(_master_dict)
        util.MR = _master_dict

    
    return _master_dict
