grammar decaf;

// PARSER RULES

PROGRAM : 'class' 'Program' '{' (DECLARATION)* '}';
DECLARATION : STRUCTDECLARATION | VARDECLARATION | METHODECLARATION;
VARDECLARATION : VARTYPE ID ';' | VARTYPE ID '[' NUM ']' ';';
STRUCTDECLARATION : 'struct' ID '{' (VARDECLARATION)* '}';
VARTYPE : 'int' | 'char' | 'boolean' | 'struct' ID | STRUCTDECLARATION | 'void';
METHODECLARATION : METHODTYPE ID '(' (PARAMETER)* ',' ')' BLOCK;
METHODTYPE : 'int' | 'char' | 'boolean'| 'void';
PARAMETER : PARAMETERTYPE ID | PARAMETERTYPE ID '[' ']';
PARAMETERTYPE : 'int' | 'char' | 'boolean';
BLOCK : '{' (VARDECLARATION)* (STATEMENT)* '}';
STATEMENT : 'if' '(' EXPRESSION ')' BLOCK ['else' BLOCK]
| 'while' '(' EXPRESSION ')' BLOCK
| 'return' [EXPRESSION] ';'
| METHODCALL ';'
| BLOCK
| LOCATION '=' EXPRESSION
| [EXPRESSION] ';'
;
LOCATION : (ID | ID '[' EXPRESSION ']') [ '.' LOCATION ];
EXPRESSION : LOCATION
| METHODCALL
| LITERAL
| EXPRESSION OP EXPRESSION
| '-' EXPRESSION
| '!' EXPRESSION
| '(' EXPRESSION ')'
;
METHODCALL : ID '(' (ARG)* ',' ')';
ARG : EXPRESSION;
OP : ARITH_OP | REL_OP | EQ_OP | COND_OP;
ARITH_OP : '+' | '-' | '*' | '/' | '%';
REL_OP : '<' | '>' | '<=' | '>=';
EQ_OP : '==' | '!=';
COND_OP : '&&' | '||';
LITERAL : INT_LITERAL | CHAR_LITERAL | BOOL_LITERAL;
INT_LITERAL : NUM;
CHAR_LITERAL : ''' char ''';
BOOL_LITERAL : 'true' | 'false';

// LEXER RULES

fragment DIGIT: [0-9];
fragment LETTER: [a..z] | [A..Z];

ID: LETTER (LETTER | DIGIT)*;
NUM: DIGIT (DIGIT)*;
CHAR: LETTER;