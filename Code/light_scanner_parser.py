
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

t_SEP_COMMA         = r','
t_SEP_DOT           = r'\.'
t_INT       = r'int'
#t_SEP_HASHTAG       = r'\#'

# TOKENS
t_MOVE              = r'move'

#dot      = r'\.'
def t_SEP_LPAR(t):
    r'\('
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

def t_RETURN (t):
    r'return'
    return t

def t_VAR (t):
    r'var'
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

def t_OP_MINUS_EQUALS (t):
    r'\+='
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

def t_RETURNS (t):
    r'RETURNS'
    return t

def t_LOOP (t):
    r'loop'
    return t

def t_FOR_EACH (t):
    r'for_each'
    return t

def t_IN (t):
    r'in'

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

import ply.lex as lex
lex.lex()


# STATEMENTS ###################################################################
# http://snatverk.blogspot.mx/2011/01/parser-de-mini-c-en-python.html

def p_program (p):
    '''
    program  : PROGRAM VAR_IDENTIFIER SEP_LCBRACKET pr_a pr_b main_func SEP_RCBRACKET
    '''

def p_pr_a (p):
    '''
    pr_a  : vars pr_a 
        | epsilon
    '''

def p_pr_b (p):
    '''
    pr_b  : function pr_b 
        | epsilon
    '''

def p_main_func (p):
    '''
    main_func : LIGHT_TOKEN SEP_LPAR SEP_RPAR SEP_LCBRACKET m_a SEP_RCBRACKET
    '''

def p_m_a (p):
    '''
    m_a : statement m_a
        | epsilon
    '''

def p_type (p):
    '''
    type : primitive 
        | figure 
        | epsilon
    '''

def p_primitive (p):
    '''
    primitive : BOOLEAN 
                | INT 
                | DECIMAL 
                | STRING 
                | FRACTION
    '''

def p_figure (p):
    '''
    figure : POINT 
            | LINE 
            | TRIANGLE 
            | SQUARE 
            | RECTANGLE 
            | POLYGON 
            | STAR 
            | CIRCLE
    '''

def p_function (p):
    '''
    function : FUNCTION VAR_IDENTIFIER SEP_LPAR func_a SEP_RPAR func_b SEP_LCBRACKET func_c stmt_loop SEP_RCBRACKET
    '''
def p_func_a (p):
    '''
    func_a : parameters
        | epsilon
    '''
def p_func_b (p):
    '''
    func_b : RETURNS type
        | epsilon
    '''
def p_func_c (p):
    '''
    func_c : vars  func_c
        | epsilon
    '''
def p_stmt_loop (p):
    '''
    stmt_loop : statement  stmt_loop
        | epsilon
    '''
def p_parameters (p):
    '''
    parameters : VAR_IDENTIFIER SEP_COLON type param_a
    '''

def p_param_a (p):
    '''
    param_a : SEP_COMMA
        | epsilon
    '''

def p_assignment (p):
    '''
    assignment : VAR_IDENTIFIER OP_EQUALS exp 
    '''

def p_cycle (p):
    '''
    cycle : loop cyc_a
        | for_each cyc_a
        | for cyc_a
    '''

def p_cyc_a (p):
    '''
    cyc_a : do_block
    '''

def p_loop (p):
    '''
    loop : LOOP SEP_LPAR l_a SEP_DOT SEP_DOT l_a SEP_RPAR do_block 
    '''

def p_l_a (p):
    '''
    l_a : VAR_INT
        | VAR_IDENTIFIER 
    '''

def p_for_each (p):
    '''
    for_each : FOR_EACH SEP_LPAR VAR_IDENTIFIER IN fore_a SEP_RPAR SEP_LCBRACKET stmt_loop SEP_RCBRACKET
    '''

def p_fore_a (p):
    '''
    fore_a : VAR_IDENTIFIER
    '''

def p_for (p):
    '''
    for : FOR SEP_LPAR for_a SEP_SEMICOLON condition SEP_SEMICOLON for_b SEP_RPAR SEP_LCBRACKET stmt_loop SEP_RCBRACKET
    '''

def p_for_a (p):
    '''
    for_a : assignment
        | epsilon
    '''
def p_for_b (p):
    '''
    for_b : increment
        | assignment
    '''

def p_action (p):
    '''
    action : ACTION act_a 
    '''

def p_act_a (p):
    '''
    act_a : act_move
        | act_scale
        | act_visible
        | act_rotate
    '''

def p_act_header (p):
    '''
    act_header : VAR_IDENTIFIER DO  BEGINS SEP_COLON exp SEP_COMMA  ENDS SEP_COLON exp SEP_COMMA 
    '''

def p_act_move (p):
    '''
    act_move : MOVE act_header POS_X SEP_COLON exp SEP_COMMA  POS_Y SEP_COLON exp  END
    '''

def p_act_scale (p):
    '''
    act_scale : SCALE act_header SIZE SEP_COLON exp SEP_COMMA  END
    '''

def p_act_rotate (p):
    '''
    act_rotate : SCALE act_header ANGLE SEP_COLON exp SEP_COMMA  END
    '''

def p_act_visible (p):
    '''
    act_visible : HIDE act_header END
        | SHOW act_header END
    '''

def p_camera (p):
    '''
    camera : CAMERA VAR_IDENTIFIER 
    '''

def p_condition (p):
    '''
    condition : exp ex_a
        | exp
    '''

def p_ex_a (p):
    '''
    ex_a : OP_LESS_THAN exp
        | OP_GREATER_THAN exp
        | OP_NOT_EQUAL exp
        | OP_EQUALS exp
        | OP_GREATER_EQUAL exp
        | OP_LESS_EQUAL exp
    '''

def p_exp (p):
    '''
    exp : term exp_a
    '''

def p_exp_a (p):
    '''
    exp_a : exp_b
        | epsilon
    '''

def p_exp_b (p):
    '''
    exp_b : term exp_c exp_d
    '''

def p_exp_c (p):
    '''
     exp_c : OP_PLUS
        | OP_MINUS
    '''

def p_exp_d (p):
    '''
    exp_d : exp_b
        | epsilon
    '''

def p_term (p):
    '''
    term : factor term_a
    '''

def p_term_a (p):
    '''
    term_a : term_b
        | epsilon
    '''

def p_term_b (p):
    '''
    term_b : factor term_c term_d
    '''

def p_term_c (p):
    '''
    term_c : OP_TIMES
        | OP_DIVISION
    '''

def p_term_d (p):
    '''
    term_d : term_b
        | epsilon
    '''

def p_factor (p):
    '''
    factor : VAR_IDENTIFIER
        | cnt_prim
        | SEP_LPAR exp SEP_RPAR
    '''

def p_increment (p):
    '''
    increment : VAR_IDENTIFIER inc_a exp
    '''

def p_inc_a (p):
    '''
    inc_a :  OP_PLUS_EQUALS
        | OP_MINUS_EQUALS
    '''

def p_if (p):
    '''
    if : IF condition_block if_a if_b
    '''
def p_if_a (p):
    '''
    if_a : elsif
        | epsilon
    '''
def p_if_b (p):
    '''
    if_b : else
        | epsilon
    '''

def p_elsif (p):
    '''
    elsif : ELSIF condition_block
    '''

def p_else (p):
    '''
    else : ELSE do_block
    '''

def p_condition_block (p):
    '''
    condition_block : SEP_LPAR condition SEP_RPAR do_block
    '''

def p_do_block (p):
    '''
    do_block : DO stmt_loop END
    '''

def p_statement (p):
    '''
    statement : assignment 
                | if 
                | cycle 
                | action 
                | camera 
                | comments 
                | print 
                | figure_creations 
                | return
    '''

def p_vars_start (p):
    '''
    vars_start : VARS var_a SEP_COLON
    '''

def p_var_a(p):
    '''
    var_a : VAR_IDENTIFIER var_b
    '''
def p_var_b (p):
    '''
    var_b : SEP_COMMA var_a
        | epsilon
    '''

def p_vars (p):
    '''
    vars : vars_start v_a
    '''
def p_v_a (p):
    '''
    v_a : vars_figs
        | vars_prim
    '''

def p_vars_start (p):
    '''
    vars_start : VAR vs_a SEP_COLON
    '''
def p_vs_a (p):
    '''
    vs_a : VAR_IDENTIFIER vs_b
    '''
def p_vs_b (p):
    '''
    vs_b : SEP_COMMA vs_a 
        | epsilon
    '''

def p_vars_figs (p):
    '''
    vars_figs : figure vf_a
    '''
def p_vf_a (p):
    '''
    vf_a : init_fig
        | epsilon
    '''

def p_vars_prim (p):
    '''
    vars_prim : primitive var_p_a
    '''

def p_var_p_a (p):
    '''
    var_p_a : init_prim
        | epsilon
    '''

def p_init_prim (p):
    '''
    init_prim : OP_EQUALS init_a
    '''

def p_init_a (p):
    '''
    init_a : VAR_IDENTIFIER
        | cnt_prim
    '''

def p_init_fig (p):
    '''
    init_fig : OP_EQUALS VAR_IDENTIFIER
        | HAS fig_create_block
    '''

def p_fig_create_block (p):
    '''
    fig_create_block : fig_a  END
    '''

def p_fig_a (p):
    '''
    fig_a :  fig_attr fig_b
    '''
def p_fig_b (p):
    '''
    fig_b : SEP_COMMA fig_a
        | epsilon
    '''

def p_fig_attr (p):
    '''
    fig_attr : vector
        | COLOR SEP_COLON VAR_IDENTIFIER
        | SIZE SEP_COLON exp 
    '''

def p_vector (p):
    '''
    vector : VAR_VECTORID SEP_COLON SEP_LPAR exp SEP_COMMA exp SEP_RPAR 
    '''

def p_cnt_prim (p):
    '''
    cnt_prim : VAR_INT
        | VAR_DECIMAL
        | VAR_FRACTION
    '''

def p_return (p):
    '''
    return : RETURN exp
    '''

def p_comments (p):
    '''
    comments : SEP_HASHTAG co_a 
    '''
    pass

def p_co_a (p):
    '''
    co_a : VAR_ANYCHAR co_a
        | epsilon
    '''
    pass

def p_print (p):
    '''
    print : PRINT SEP_LPAR prin_a SEP_RPAR
    '''
    pass

def p_prin_a (p):
    '''
    prin_a : exp
        | VAR_STRING
    '''
    pass

def p_figure_creations (p):
    '''
    figure_creations : VAR VAR_IDENTIFIER SEP_COLON figure HAS fig_create_block
    '''
    pass

def p_epsilon(p):
    'epsilon :'
    pass


def p_error(p):
    print "Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value)
    sys.exit(0)

# MAIN #########################################################################

import ply.yacc as yacc
parser = yacc.yacc()

import sys


if __name__ == '__main__':

    if (len(sys.argv) > 1) : fin = sys.argv[1]
    else : fin = 'input.in'

    f = open(fin, 'r')
    data = f.read()
    # print data
    # print "End of file"
    parser.parse(data, tracking=True)

    print("Successful")