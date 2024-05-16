"""Front end for Quack"""

from logging import DEBUG
import pathlib
from lark import Lark, Transformer

import argparse
import json
import sys
import pprint
# from ASTNodes.util import *

from lark.tree import ParseTree

from ASTNodes import *

from type_inference import *

sys.path.insert(1, './tiny_vm/')

def cli():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("source", type=argparse.FileType("r"),
                            nargs="?", default=sys.stdin)
    cli_parser.add_argument("-r", "--run", action=argparse.BooleanOptionalAction, 
                            default=False)
    # cli_parser.add_argument("-o", "--object", type=argparse.FileType("w"), nargs="?",
    #                         default="../tiny_vm/OBJ/$Main.json")
    args = cli_parser.parse_args()
    return args


class ASTBuilder(Transformer):
    """Translate Lark tree into my AST structure"""

    def program(self, e):
        log.debug("->program")
        classes, main_block = e
        return ProgramNode(classes, main_block)

    def classes(self, e):
        return e

    def clazz(self, e):
        log.debug("->clazz")
        name, formals, super, methods, constructor = e
        if not formals[0]:
            formals = []
        clss = ClassNode(name.__str__(), formals, super.__str__(), methods, constructor)
        util.class_table[name.__str__()] = clss
        return clss

    def methods(self, e):
        return e

    def method(self, e):
        log.debug("->method")
        name, formals, returns, body = e
        return MethodNode(name.__str__(), formals, returns[0].__str__(), body)

    def call(self, e):
        log.debug("->method call")
        receiver = e[0]
        name = e[1]
        params = e[2]
        return MethodCallNode(name.__str__(), receiver, params)

    def returns(self, e):
        return e

    def formals(self, e):
        return e

    def formal(self, e):
        log.debug("->formal")
        var_name, var_type = e
        return FormalNode(var_name.__str__(), var_type.__str__())

    def expr(self, e):
        log.debug("->expr")
        return ExprNode(e[0])

    def lessthan(self, e):
        receiver = e[0]
        params = e[1:]
        return MethodCallNode("less", receiver, params)

    def greaterthan(self, e):
        receiver = e[0]
        params = e[1:]
        return MethodCallNode("greater", receiver, params)

    def and_op(self, e):
        left, right = e
        return AndNode(left, right)
    
    def or_op(self, e):
        left, right = e
        return OrNode(left, right)

    def add(self, e):
        receiver, params = e
        return MethodCallNode("plus", receiver, [params])

    def sub(self, e):
        receiver, params = e
        return MethodCallNode("minus", receiver, [params])

    def mul(self, e):
        receiver, params = e
        return MethodCallNode("times", receiver, [params])

    def div(self, e):
        receiver, params = e
        return MethodCallNode("divide", receiver, [params])

    def ident(self, e):
        """A terminal symbol """
        log.debug("->ident")
        return e[0].__str__()

    def variable_ref(self, e):
        """A reference to a variable"""
        log.debug("->variable_ref")
        return VariableRefNode(e[0].__str__())

    def block(self, e) -> ASTNode:
        log.debug("->block")
        stmts = e
        return BlockNode(stmts)

    def assignment(self, e) -> ASTNode:
        log.debug("->assignment")

        name, assign_type, rhs = e
        return AssignmentNode(name.__str__(), assign_type, rhs)

    def ifstmt(self, e) -> ASTNode:
        log.debug("->ifstmt")
        cond, thenpart, elsepart = e
        return IfStmtNode(cond, thenpart, elsepart)

    def otherwise(self, e) -> ASTNode:
        log.debug("->otherwise")
        return e

    def elseblock(self, e) -> ASTNode:
        log.debug("->elseblock")
        return e[0]  # Unwrap one level of block

    def cond(self, e) -> ASTNode:
        log.debug("->cond")
        return e
    
    def constant(self, e) -> ASTNode:
        log.debug("->constant")
        return ConstantNode(e[0])

    def class_init(self, e) -> ASTNode:
        if e.__len__() > 1:
            params = e[1]
        else:
            params = []
        return MethodCallNode('$constructor', receiver=util.class_table[e[0]], params=params)
    
    def actuals(self, e):
        if e[0]:
            return e
        return []




def method_table_walk(node: ASTNode, visit_state: dict):
        node.method_table_visit(visit_state)

def generate_ast(
    input_text: str,
    grammar: str = open(pathlib.Path(__file__).parent.resolve() / 'qklib' / 'quack_grammar.txt' ).read(),
    ast_builder: Transformer = ASTBuilder()
    ) -> tuple[ ASTNode, ParseTree ]:
    quack_parser = Lark(grammar, parser="lalr", debug=True)  # Create parser
    tree = quack_parser.parse(input_text) # Generate the parse tree from input_text and given grammar
    return ast_builder.transform(tree), tree  # Transform tree to the AST

def replace_main_class(filename: str, code: list[str]):
    for i, line in enumerate(code): # Find and replace $Main with the file name
        main_split = line.split("$Main")
        if main_split.__len__() > 1:
            code[i] = main_split[0] + filename + "".join(main_split[1:])
            break

def split_classes(split_phrase: str, code: list[str]) -> list[list[str]]:
    ret_list = []
    tmp_list = []
    for line in code:
        if line == split_phrase:
            ret_list.append(tmp_list)
            tmp_list = []
        else:
            tmp_list.append(line)
    if tmp_list.__len__() > 0:
        ret_list.append(tmp_list)
    return ret_list

def write_tmp_files(tmp_dir: pathlib.Path, codes: list[list[str]]):
    for code in codes:
        tmp_file = tmp_dir / f"{code[0].split(' ')[1].split(':')[0]}.asm"
        tmp_file.write_text("\n".join(code))

def main():
    DEBUG = True
    # DEBUG = False
    args = cli()
    if args.run:
        DEBUG = False
    if DEBUG:
        text = "".join(open("./samples/simple.qk").readlines())
    else:
        text = "".join(args.source.readlines())
    ( ast, tree ) = generate_ast(text)
    if DEBUG:
        print(tree.pretty("   "))
    builtins = open(pathlib.Path(__file__).parent.resolve() / 'qklib' / 'builtin_methods.json')
    symtab = json.load(builtins)
    ast.walk(symtab, method_table_walk)
    typing_stuff = type_inference(ast, symtab) 
    # args.object.write(typing_stuff.__str__())
    if DEBUG:
        print(pprint.pp(typing_stuff))
        print(ast)
    code = []
    ast.gen_code(code)
    filename = pathlib.Path(args.source.__str__()).stem
    replace_main_class(filename, code)
    class_codes = split_classes(ZERO_SPACE_CHAR, code)
    write_tmp_files(pathlib.Path('./tmp/'), class_codes)


    print("\n".join(code))
    # Build symbol table, starting with the hard-coded json table
    # provided by Pranav.  We'll follow that structure for the rest
    # builtins = open(pathlib.Path(__file__).parent.resolve() / 'qklib' / 'builtin_methods.json')
    # symtab = json.load(builtins)
    # ast.walk(symtab, method_table_walk)
    # print(json.dumps(symtab,indent=4))


if __name__ == "__main__":
    main()
