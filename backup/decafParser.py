# Generated from decaf.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write("\20\4\2\t\2\3\2\3\2\3\2\3\2\7\2\t\n\2\f\2\16\2\f\13\2")
        buf.write("\3\2\3\2\3\2\2\2\3\2\2\2\2\17\2\4\3\2\2\2\4\5\7\3\2\2")
        buf.write("\5\6\7\4\2\2\6\n\7\5\2\2\7\t\7\7\2\2\b\7\3\2\2\2\t\f\3")
        buf.write("\2\2\2\n\b\3\2\2\2\n\13\3\2\2\2\13\r\3\2\2\2\f\n\3\2\2")
        buf.write("\2\r\16\7\6\2\2\16\3\3\2\2\2\3\n")
        return buf.getvalue()


class decafParser ( Parser ):

    grammarFileName = "decaf.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'Program'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Declaration", "Vardeclaration", "Structdeclaration", 
                      "Vartype", "Methodeclaration", "Methodtype", "Parameter", 
                      "Parametertype", "Block", "Statement", "Location", 
                      "Expression", "Methodcall", "Arg", "Op", "Arith_op", 
                      "Rel_op", "Eq_op", "Cond_op", "Literal", "Int_literal", 
                      "Char_literal", "Bool_literal", "DIGIT", "LETTER", 
                      "ID", "NUM", "CHAR" ]

    RULE_prog = 0

    ruleNames =  [ "prog" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Declaration=5
    Vardeclaration=6
    Structdeclaration=7
    Vartype=8
    Methodeclaration=9
    Methodtype=10
    Parameter=11
    Parametertype=12
    Block=13
    Statement=14
    Location=15
    Expression=16
    Methodcall=17
    Arg=18
    Op=19
    Arith_op=20
    Rel_op=21
    Eq_op=22
    Cond_op=23
    Literal=24
    Int_literal=25
    Char_literal=26
    Bool_literal=27
    DIGIT=28
    LETTER=29
    ID=30
    NUM=31
    CHAR=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Declaration(self, i:int=None):
            if i is None:
                return self.getTokens(decafParser.Declaration)
            else:
                return self.getToken(decafParser.Declaration, i)

        def getRuleIndex(self):
            return decafParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = decafParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(decafParser.T__0)
            self.state = 3
            self.match(decafParser.T__1)
            self.state = 4
            self.match(decafParser.T__2)
            self.state = 8
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==decafParser.Declaration:
                self.state = 5
                self.match(decafParser.Declaration)
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 11
            self.match(decafParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





