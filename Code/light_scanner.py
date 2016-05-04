import ply.lex as lex

reserved_words = {
    # Basic tokens
    'program'   : 'PROGRAM',
    'light'     : 'LIGHT_TOKEN',
    'var'       : 'VAR',
    'print'     : 'PRINT',
    'true'      : 'VAR_BOOLEAN',
    'false'     : 'VAR_BOOLEAN',

    # Function tokens
    'function'  : 'FUNCTION',
    'returns'   : 'RETURNS',
    'return'    : 'RETURN',

    # Cycle tokens
    'while'      : 'WHILE',
    'for'       : 'FOR',
    'foreach'  	: 'FOR_EACH',
    'in'        : 'IN',

    # Conditional tokens
    'if'        : 'IF',
    'elsif'     : 'ELSIF',
    'else'      : 'ELSE',

    # Primitive type declaration tokens
    'boolean'   : 'BOOLEAN',
    'int'       : 'INT',
    'decimal'   : 'DECIMAL',
    'string'    : 'STRING',
    'fraction'  : 'FRACTION',

    # Figure type declaration tokens
    'point'     : 'POINT',
    'line'      : 'LINE',
    'triangle'  : 'TRIANGLE',
    'square'    : 'SQUARE',
    'rectangle' : 'RECTANGLE',
    'polygon'   : 'POLYGON',
    'star'      : 'STAR',
    'circle'    : 'CIRCLE',

    # Figure actions tokens
    'figure'	: 'FIGURE',
    'action'    : 'ACTION',
    'do'        : 'DO',
    'end'       : 'END',
    'begins'    : 'BEGINS',
    'ends'      : 'ENDS',
    'move'      : 'MOVE',
    'posX'      : 'POS_X',
    'posY'      : 'POS_Y',
    'v'         : 'VAR_VECTORID',
    'scale'     : 'SCALE',
    'size'      : 'SIZE',
    'hide'      : 'HIDE',
    'show'      : 'SHOW',
    'camera'    : 'CAMERA',
    'has'       : 'HAS',
    'color'     : 'COLOR',
    'rgb'       : 'RGB',
    'rotate'    : 'ROTATE',
    'window_size' : 'WINDOW_SIZE',
    'background_color' : 'BACKGROUND_COLOR',
    'window_name' : 'WINDOW_NAME',
    'wait'      : 'WAIT',
    'move_speed': 'MOVE_SPEED',
    'text_color': 'TEXT_COLOR',
    'printg'    : 'PRINT_G',
    'length'	: 'LENGTH',

    #MATH		
    'sin'		: 'SIN',
    'cos'		: 'COS',
    'tan'		: 'TAN',

    # AND OR Conditionals
    'and'		: 'AND',
    'or'		: 'OR',

    #MOD
    'mod'		: 'OP_MOD',

    #extra
    'exp'		: 'EXPONENTIAL',
    'log10'		: 'LOG10',
    'sqrt'		: 'SQRT',
    'pow'		: 'POW'

}

tokens = (
    'PROGRAM', 'VAR_IDENTIFIER' , 'SEP_LCBRACKET' , 'SEP_RCBRACKET',
    'FUNCTION', 'LIGHT_TOKEN', 'VAR_BOOLEAN', 'VAR_INT', 'VAR_DECIMAL',
    'VAR_STRING', 'VAR_FRACTION', 'POINT', 'LINE', 'TRIANGLE', 'SQUARE',
    'BOOLEAN', 'INT', 'DECIMAL', 'STRING', 'FRACTION', 'RECTANGLE', 'POLYGON', 
    'STAR', 'CIRCLE', 'SEP_LPAR', 'SEP_RPAR', 'RETURNS', 'SEP_COLON', 
    'SEP_COMMA', 'OP_EQUALS', 'WHILE', 'SEP_DOT', 'FOR_EACH', 'IN', 
    'SEP_SEMICOLON', 'ACTION', 'DO', 'BEGINS', 'ENDS', 'MOVE', 'POS_X', 'POS_Y',
    'END', 'SCALE', 'SIZE', 'HIDE', 'SHOW', 'CAMERA', 'OP_LESS_THAN', 
    'OP_GREATER_THAN', 'OP_NOT_EQUAL', 'OP_GREATER_EQUAL', 'OP_LESS_EQUAL', 'OP_EQUALSS', 
    'OP_PLUS', 'OP_MINUS', 'OP_TIMES', 'OP_DIVISION', 'OP_PLUS_EQUALS', 
    'OP_MINUS_EQUALS', 'IF', 'ELSIF', 'ELSE', 'HAS', 'COLOR', 'VAR', 'PRINT', 
    'FOR', 'ROTATE', 'VAR_VECTORID', 'RETURN', 'SEP_LBRACKET', 'SEP_RBRACKET', 'AND', 'OR', 'FIGURE',
    'RGB', 'WINDOW_SIZE', 'WAIT', 'MOVE_SPEED', 'BACKGROUND_COLOR', 'TEXT_COLOR', 'PRINT_G', 'WINDOW_NAME', 'LENGTH',
    'SIN', 'COS', 'OP_MOD', 'TAN', 'EXPONENTIAL', 'LOG10', 'SQRT', 'POW'
    )

# Ignoring comments, spaces and tabs

t_ignore = ' \t'
def t_COMMENT(t):
    r'\#.*'
    pass

# Separators and Operators

def t_SEP_DOT(t):
    r'\.'
    return t

def t_SEP_LPAR(t):
    r'\('
    return t

def t_SEP_LBRACKET(t):
    r'\['
    return t

def t_SEP_RBRACKET(t):
    r'\]'
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

def t_SEP_LCBRACKET (t):
    r'{'
    return t

def t_SEP_RCBRACKET (t):
    r'}'
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
    r'\-='
    return t

def t_OP_PLUS_EQUALS (t):
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

def t_OP_LESS_EQUAL (t):
    r'<='
    return t

def t_OP_GREATER_EQUAL (t):
    r'>='
    return t

def t_OP_GREATER_THAN (t):
    r'>'
    return t

def t_OP_LESS_THAN (t):
    r'<'
    return t

def t_OP_NOT_EQUAL(t):
    r'!='
    return t

def t_OP_EQUALSS (t):
    r'=='
    return t

def t_OP_EQUALS (t):
    r'='
    return t

# Regular Expressions

def t_VAR_FRACTION (t):
    r'[0-9]+[\\][0-9]+'

def t_VAR_IDENTIFIER (t):
    r'[a-zA-Z]+[0-9]*(_[a-zA-Z0-9]*)*'
    t.type = reserved_words.get(t.value, 'VAR_IDENTIFIER')
    return t

def t_VAR_DECIMAL (t):
    r'[0-9]+[\.][0-9]+'
    return t

def t_VAR_INT (t):
    r'[0-9]+'
    return t

def t_VAR_STRING (t) :    
    r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'
    return t

def t_VAR_BOOLEAN (t):
    r'[true|false]'
    return t

#not shure braw
# def t_VAR_ANYCHAR(t) :
#     r'.'
#     return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print "Syntax error at line " + str(t.lexer.lineno) + " Illegal character " + str(t.value[0])
    t.lexer.skip(1)
    sys.exit(0)

lexer = lex.lex()