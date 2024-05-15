"""Front end for Quack"""

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

def cli():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("source", type=argparse.FileType("r"),
                            nargs="?", default=sys.stdin)
    # cli_parser.add_argument("-d", "--debug", action=argparse.BooleanOptionalAction, 
    #                         default=False)
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
        return ClassNode(name.__str__(), formals, super.__str__(), methods, constructor)

    def methods(self, e):
        return e

    def method(self, e):
        log.debug("->method")
        name, formals, returns, body, return_stmt = e
        return MethodNode(name.__str__(), formals, returns[0].__str__(), body, return_stmt)

    def call(self, e):
        log.debug("->method call")
        name = e[0]
        receiver = e[1]
        params = e[2:]
        return MethodCallNode(name.__str__(), receiver, params)

    def returns(self, e):
        if not e:
            return "Nothing"
        return e

    def formals(self, e):
        if e[0] is None:
            return []
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
        return e[0]

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

def method_table_walk(node: ASTNode, visit_state: dict):
        node.method_table_visit(visit_state)

def generate_ast(
    input_text: str,
    grammar: str = open(pathlib.Path(__file__).parent.resolve() / 'qklib' / 'quack_grammar.txt' ).read(),
    ast_builder: Transformer = ASTBuilder()
    ) -> tuple[ ASTNode, ParseTree ]:
    quack_parser = Lark(grammar)  # Create parser
    tree = quack_parser.parse(input_text) # Generate the parse tree from input_text and given grammar
    return ast_builder.transform(tree), tree  # Transform tree to the AST

DEBUG = False
def main():
    args = cli()
    if DEBUG:
        text = "".join(open("./samples/simple.qk").readlines())
    else:
        text = "".join(args.source.readlines())
    ( ast, tree ) = generate_ast(text)
    if DEBUG:
        print(tree.pretty("   "))
    ast: ASTNode = ASTBuilder().transform(tree)
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
    for i, line in enumerate(code): # Find and replace $Main with the file name
        main_split = line.split("$Main")
        if main_split.__len__() > 1:
            code[i] = main_split[0] + filename + "".join(main_split[1:])
            break


    print("\n".join(code))
    # Build symbol table, starting with the hard-coded json table
    # provided by Pranav.  We'll follow that structure for the rest
    # builtins = open(pathlib.Path(__file__).parent.resolve() / 'qklib' / 'builtin_methods.json')
    # symtab = json.load(builtins)
    # ast.walk(symtab, method_table_walk)
    # print(json.dumps(symtab,indent=4))


if __name__ == "__main__":
    main()
