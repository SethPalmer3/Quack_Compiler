from ASTNodes import *

def LCA(t1: str, t2: str, _master_record: dict = {}) -> str:
    if t1 == t2: # Both the same type
        return t1
    else:
        heirarchy = construct_class_heirarchy(_master_record)
        t1_node = heirarchy.get_node(t1)
        t2_node = heirarchy.get_node(t2)
        if t1_node is None or t2_node is None:
            raise ValueError("LCA given non existant type")
        while t1_node != t2_node:
            t1_node = t1_node.parent_class
            t2_node = t2_node.parent_class
        return t1_node.class_name


class QC:
    def __init__(self, class_name: str) -> None:
        self.class_name = class_name
        self.parent_class = None
        self.child_classes: list[QC] =[]

    def add_child_class(self, c: "QC"):
        self.child_classes.append(c)
        c.parent_class = self

    def shift_down(self, c: "QC", p_name: str) -> bool:
        if self.class_name == p_name:
            self.add_child_class(c)
            return True
        else:
            for cc in self.child_classes:
                if cc.shift_down(c, p_name):
                    return True
        return False
    
    def get_node(self, name: str):
        if self.class_name == name:
            return self
        for c in self.child_classes:
            tmp_node = c.get_node(name)
            if tmp_node is not None:
                return tmp_node
        return None
    def __repr__(self) -> str:
        return self.class_name

def construct_class_heirarchy(record: dict[str,dict]) -> QC:
    classes: list[QC] = []
    for (k, _) in record.items():
        classes.append(QC(k))

    head = None
    for i, n in enumerate(classes):
        if n.class_name == "Obj":
            head = n
            classes.pop(i)
            break

    if head is None:
        raise ValueError("Could not find root `Obj` in record")

    while(classes.__len__() > 0):
        for i, n in enumerate(classes):
            if 'super' not in record[n.class_name] or head.shift_down(n, record[n.class_name]['super']):
                classes.pop(i)
    return head
