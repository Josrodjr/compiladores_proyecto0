import antlr4 as antlr4
from decafLexer import decafLexer
from decafListener import decafListener
from decafParser import decafParser
import sys

def main():
    lexer = decafLexer(antlr4.StdinStream())
    stream = antlr4.CommonTokenStream(lexer)
    parser = decafParser(stream)
    tree = parser.program()

    print(tree)

if __name__ == '__main__':
    main()