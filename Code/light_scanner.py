import ply.lex as lex

tokens = (
    'PROGRAM', 'VAR_IDENTIFIER' , 'SEP_LCBRACKET' , 'SEP_RCBRACKET',
    'FUNCTION', 'LIGHT_TOKEN', 'VAR_BOOLEAN', 'VAR_INT', 'VAR_DECIMAL',
    'VAR_STRING', 'VAR_FRACTION', 'POINT', 'LINE', 'TRIANGLE', 'SQUARE',
    'BOOLEAN', 'INT', 'DECIMAL', 'STRING', 'FRACTION',
    'RECTANGLE', 'POLYGON', 'STAR', 'CIRCLE', 'SEP_LPAR', 'SEP_RPAR', 'RETURNS',
    'SEP_COLON', 'SEP_COMMA', 'OP_EQUALS', 'LOOP', 'SEP_DOT', 'FOR_EACH',
    'IN', 'SEP_SEMICOLON', 'ACTION', 'DO', 'BEGINS', 'ENDS', 'MOVE', 'POS_X', 'POS_Y', 'END',
    'SCALE', 'SIZE', 'HIDE', 'SHOW', 'CAMERA', 'OP_LESS_THAN', 'OP_GREATER_THAN', 'OP_NOT_EQUAL',
    'OP_GREATER_EQUAL', 'OP_LESS_EQUAL', 'OP_PLUS', 'OP_MINUS', 'OP_TIMES',
    'OP_DIVISION', 'OP_PLUS_EQUALS', 'OP_MINUS_EQUALS', 'IF', 'ELSIF', 'ELSE', 'HAS', 'COLOR',
    'SEP_HASHTAG', 'VAR', 'PRINT' , 'VAR_ANYCHAR' ,'FOR', 'ANGLE', 'VAR_VECTORID',
    'RETURN', 
    )

# SEPARATORS

#t_SEP_HASHTAG = r'\#'

# TOKENS
t_MOVE              = r'move'

#dot      = r'\.'
def t_SEP_DOT(t):
    r'\.'
    return t

def t_SEP_LPAR(t):
    r'\('
    return t

def t_SEP_COMMA(t):
    r','
    return t

def t_SEP_RPAR(t):
    r'\)'
    return t

def t_SEP_COLON(t):
    ':'
    return t

def t_SEP_SEMICOLON(t):
    ';'
    return t

def t_FUNCTION (t):
    r'function'
    return t

def t_SEP_LCBRACKET (t):
    r'{'
    return t

def t_SEP_RCBRACKET (t):
    r'}'
    return t

def t_LIGHT_TOKEN(t):
    r'light'
    return t

def t_RETURNS (t):
    r'returns'
    return t

def t_RETURN (t):
    r'return'
    return t

def t_VAR (t):
    r'var\s'
    return t

def t_DECIMAL (t):
    r'decimal'
    return t

def t_STRING (t):
    r'string'
    return t

def t_PRINT (t):
    r'print'
    return t

def t_VAR_VECTORID (t):
    r'v[0-9]+'
    return t

def t_ANGLE (t):
    r'angle'
    return t

def t_FOR_EACH (t):
    r'for_each'
    return t

def t_FOR (t):
    r'for'
    return t
    
def t_ACTION (t):
    r'action'
    return t

def t_DO (t):
    r'do'
    return t

def t_BEGINS (t):
    r'begins'
    return t

def t_ENDS (t):
    r'ends'
    return t
def t_MOVE (t):
    r'pos_x'
    return t
def t_POS_Y (t):
    r'pos_y'
    return t

def t_END (t):
    r'end'
    return t
  
def t_HAS (t):
    r'has'
    return t

def t_COLOR (t):
    r'color'
    return t

def t_SCALE (t):
    r'scale'
    return t

def t_SIZE (t) : 
    r'size'
    return t

def t_HIDE (t) : 
    r'hide'
    return t

def t_SHOW (t) : 
    r'show'
    return t

def t_CAMERA (t) : 
    r'camera'
    return t

def t_OP_LESS_THAN (t) : 
    r'<'
    return t

def t_OP_GREATER_THAN (t):
    r'>'
    return t

def t_OP_NOT_EQUAL (t):
    r'!='
    return t

def t_OP_MINUS_EQUALS (t):
    r'\+='
    return t

def t_OP_PLUS (t):
    r'\+'
    return t

def t_OP_MINUS (t):
    r'-'
    return t

def t_OP_TIMES (t):
    r'\*'
    return t

def t_OP_DIVISION (t):
    r'/'
    return t

def t_OP_EQUALS (t):
    r'='
    return t

def t_OP_PLUS_EQUALS (t):
    r'-='
    return t

def t_OP_LESS_THAN (t):
    r'<'
    return t

def t_OP_LESS_EQUAL (t):
    r'<='
    return t

def t_OP_GREATER_THAN (t):
    r'>'
    return t

def t_OP_GREATER_EQUAL (t):
    r'>='
    return t

def t_OP_NOT_EQUAL(t):
    r'!='
    return t

def t_PROGRAM (t):
    r'program'
    return t

def t_IF (t):
    r'if'
    return t

def t_ELSIF (t):
    r'elsif'
    return t

def t_ELSE (t):
    r'else'
    return t

def t_PRINT (t):
    r'print'
    return t

def t_INT (t):
    r'int'
    return t

def t_FLOAT (t):
    r'float'
    return t

def t_LOOP (t):
    r'loop'
    return t

def t_IN (t):
    r'in\s'
    return t

#Figures

def t_STAR (t):
    r'STAR'
    return t

def t_POLYGON (t):
    r'polygon'
    return t

def t_POINT (t):
    r'point'
    return t

def t_LINE (t):
    r'line'
    return t

def t_TRIANGLE (t):
    r'triangle'
    return t

def t_CIRCLE (t):
    r'circle'
    return t

def t_SQUARE (t):
    r'square'
    return t

def t_RECTANGLE (t):
    r'rectangle'
    return t

def t_VAR_FRACTION (t):
    r'[0-9]+[\\][0-9]+'

def t_VAR_IDENTIFIER (t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_VAR_DECIMAL (t):
    r'[0-9]+[\.][0-9]+'
    return t

def t_VAR_INT (t):
    r'[0-9]+'
    return t

def t_VAR_STRING (t) :    
    r'\"[a-zA-Z]([a-zA-Z0-9])*\"'
    return t

def t_VAR_BOOLEAN (t):
    r'[true|false]'
    return t

#not shure braw
def t_VAR_ANYCHAR(t) :
    r'.'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print "Syntax error at line " + str(t.lexer.lineno) + " Illegal character " + str(t.value[0])
    t.lexer.skip(1)
    sys.exit(0)

lexer = lex.lex()