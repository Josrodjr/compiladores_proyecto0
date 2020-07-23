# Generated from decaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafParser import decafParser
else:
    from decafParser import decafParser

# This class defines a complete listener for a parse tree produced by decafParser.
class decafListener(ParseTreeListener):

    # Enter a parse tree produced by decafParser#prog.
    def enterProg(self, ctx:decafParser.ProgContext):
        pass

    # Exit a parse tree produced by decafParser#prog.
    def exitProg(self, ctx:decafParser.ProgContext):
        pass



del decafParser