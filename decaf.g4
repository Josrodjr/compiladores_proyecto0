grammar decaf;

// PARSER RULES

program : 'class' 'Program' '{' (declaration)* '}';

declaration : structDeclaration | varDeclaration | methoDeclaration;
varDeclaration : varType ID ';' | varType ID '[' NUM ']' ';';
structDeclaration : 'struct' ID '{' (varDeclaration)* '}';
varType : 'int' | 'char' | 'boolean' | 'struct' ID | structDeclaration | 'void';
methoDeclaration : methodType ID '(' (parameter)* ',' ')' block;
methodType : 'int' | 'char' | 'boolean'| 'void';
parameter : parametertype ID | parametertype ID '[' ']';
parametertype : 'int' | 'char' | 'boolean';
block: '{' (varDeclaration)* (statement)* '}';
statement : 'if' '(' expression ')' block ('else' block)?
| 'while' '(' expression ')' block
| 'return' (expression)? ';'
| methodCall ';'
| block
| location '=' expression
| (expression)? ';'
;
location : (ID | ID '[' expression ']') ('.' location)?;
expression : location
| methodCall
| literal
| expression op expression
| '-' expression
| '!' expression
| '(' expression ')'
;
methodCall : ID '(' (arg)* ',' ')';
arg : expression;
op : arith_op | rel_op | eq_op | cond_op;
arith_op : '+' | '-' | '*' | '/' | '%';
rel_op : '<' | '>' | '<=' | '>=';
eq_op : '==' | '!=';
cond_op : '&&' | '||';
literal : int_Literal | char_Literal | bool_Literal;
int_Literal : NUM;
char_Literal : '"' CHAR '"';
bool_Literal : 'true' | 'false';

// LEXER RULES

DIGIT: [0-9];
LETTER: [a-z] | [A-Z];

ID: LETTER (LETTER | DIGIT)*;
NUM: DIGIT (DIGIT)*;
CHAR: LETTER;