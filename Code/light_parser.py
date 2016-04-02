import light_scanner as lexer
import ply.yacc as yacc
from light_semantic_controller import *

tokens = lexer.tokens
function_stack = Stack()
tmp_var = Var()
tmp_function = Function()
function_stack.push('program')



# STATEMENTS ###################################################################
# http://snatverk.blogspot.mx/2011/01/parser-de-mini-c-en-python.html

def p_program (p):
    '''
    program  : PROGRAM VAR_IDENTIFIER SEP_LCBRACKET pr_a pr_b main_func SEP_RCBRACKET
    '''
    function_stack.pop()
    FunctionTable.print_all()

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
    main_func : LIGHT_TOKEN new_func_scope SEP_LPAR SEP_RPAR SEP_LCBRACKET pr_a stmt_loop SEP_RCBRACKET
    '''
    function_stack.pop()

def p_type (p):
    '''
    type : primitive_type 
        | figure 
        | epsilon
    '''
    p[0] = p[1]

def p_primitive_type (p):
    '''
    primitive_type : BOOLEAN 
                | INT 
                | DECIMAL 
                | STRING 
                | FRACTION
    '''
    p[0] = p[1]
    tmp_var.type = type_dict[p[1]]
    tmp_function.type = type_dict[p[1]]

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
    p[0] = p[1]

def p_stmt_loop (p):
    '''
    stmt_loop : statement  stmt_loop
        | epsilon
    '''

def p_function (p):
    '''
    function : FUNCTION VAR_IDENTIFIER new_func_scope SEP_LPAR func_a SEP_RPAR func_b SEP_LCBRACKET func_c stmt_loop SEP_RCBRACKET
    '''
    function_stack.pop()

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
    FunctionTable.add_return_type_to_func(tmp_function.name, tmp_function.type)

def p_func_c (p):
    '''
    func_c : vars  func_c
        | epsilon
    '''

def p_new_func_scope(p):
    'new_func_scope :'
    function_stack.push(p[-1])
    tmp_function.name = p[-1]
    tmp_function.type = type_dict['void']
    FunctionTable.add_function(tmp_function)

def p_parameters (p):
    'parameters : VAR_IDENTIFIER SEP_COLON type new_param_seen param_a'

def p_new_param_seen(p):
    'new_param_seen : '
    tmp_var.name = p[-3]
    tmp_var.type = type_dict[p[-1]]
    FunctionTable.add_var_to_func(tmp_function.name, tmp_var)

def p_param_a (p):
    '''
    param_a : SEP_COMMA parameters
        | epsilon
    '''

def p_function_call(p):
    '''
    function_call : VAR_IDENTIFIER test SEP_LPAR call_parameters SEP_RPAR
    '''
def p_test(p):
	'''
	test : 
	'''
	print("test: " + str(p.lexer.lineno))

def p_call_parameters(p):
    '''
    call_parameters : VAR_IDENTIFIER SEP_COLON cnt_prim call_param_a
    	| epsilon
    '''
def p_call_param_a(p):
    '''
    call_param_a : SEP_COMMA call_parameters
        | epsilon
    '''
    pass
 

def p_assignment (p):
    '''
    assignment : VAR_IDENTIFIER OP_EQUALS assgn_a 
    '''
    print("assignment: " + str(p.lexer.lineno))

def p_assgn_a(p):
    '''
    assgn_a : VAR_IDENTIFIER
    	| exp
    	| function_call
     
    '''
    print("ASSIGN A: " + str(p.lexer.lineno))

def p_cycle (p):
    '''
    cycle : loop do_block
        | for_each do_block
        | for do_block
    '''
    print("cycle: " + str(p.lexer.lineno))

def p_loop (p):
    '''
    loop : LOOP SEP_LPAR l_a SEP_DOT SEP_DOT l_a SEP_RPAR 
    '''

def p_l_a (p):
    '''
    l_a : VAR_INT
        | VAR_IDENTIFIER 
    '''

def p_for_each (p):
    '''
    for_each : FOR_EACH SEP_LPAR VAR_IDENTIFIER IN for_each_collection SEP_RPAR
    '''
def p_for_each_collection(p):
    '''
    for_each_collection : VAR_IDENTIFIER
        | SEP_LBRACKET VAR_INT SEP_DOT SEP_DOT VAR_INT SEP_RBRACKET
    '''

def p_for (p):
    '''
    for : FOR SEP_LPAR for_a SEP_SEMICOLON condition SEP_SEMICOLON for_b SEP_RPAR
    '''
    print("for" + str(p.lexer.lineno))

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
    act_header : VAR_IDENTIFIER DO  BEGINS SEP_COLON exp SEP_COMMA  ENDS SEP_COLON exp 
    '''

def p_act_move (p):
    '''
    act_move : MOVE act_header SEP_COMMA POS_X SEP_COLON exp SEP_COMMA  POS_Y SEP_COLON exp  END
    '''

def p_act_scale (p):
    '''
    act_scale : SCALE act_header SEP_COMMA SIZE SEP_COLON exp END
    '''

def p_act_rotate (p):
    '''
    act_rotate : SCALE act_header SEP_COMMA ANGLE SEP_COLON exp SEP_COMMA  END
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


##AND OR ret
def p_condition (p):
    '''
    condition : expresion cond_a
    '''
    print("condition" + str(p.lexer.lineno))

def p_cond_a(p):
	'''
	cond_a : oper_a condition
		| epsilon
	'''

def p_oper_a(p):
	'''
	oper_a : AND
		| OR
	'''

def p_expresion(p):
	'''
	expresion : exp expresion_a
	'''
	print("expresion" + str(p.lexer.lineno))

def p_expresion_a(p):
	'''
	expresion_a : ex_a exp
		| epsilon
	'''

def p_ex_a (p):
    '''
    ex_a : OP_LESS_THAN
        | OP_GREATER_THAN
        | OP_NOT_EQUAL
        | OP_EQUALS
        | OP_GREATER_EQUAL
        | OP_LESS_EQUAL
    '''
    print("Greater less etc: " + str(p.lexer.lineno))


def p_exp (p):
    '''
    exp : term exp_a
    '''
    print("exp: " + str(p.lexer.lineno))

def p_exp_a (p):
    '''
    exp_a : exp_b exp
        | epsilon
    '''

# Changed position of term 
def p_exp_b (p):
    '''
    exp_b : OP_PLUS
        | OP_MINUS
    '''


def p_term (p):
    '''
    term : factor term_a
    '''
    print("term: " + str(p.lexer.lineno))

def p_term_a (p):
    '''
    term_a : term_b term
        | epsilon
    '''
def p_term_b (p):
    '''
    term_b : OP_TIMES
        | OP_DIVISION
    '''

def p_factor (p):
    '''
    factor : SEP_LPAR condition SEP_RPAR
    	| var_cte
    '''
    print("factor: " + str(p.lexer.lineno))

# def p_fact_a(p):
# 	'''
# 	fact_a : exp_b
# 		| epsilon
# 	'''

def p_var_cte(p):
	'''
	var_cte : VAR_IDENTIFIER
		| VAR_INT
        | VAR_DECIMAL
	'''
	print("varCTE: " + str(p.lexer.lineno))

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
    print("conditionBlock " + str(p.lexer.lineno))

def p_do_block (p):
    '''
    do_block : DO stmt_loop END
    '''
    print("doBlock " + str(p.lexer.lineno))

# WARNING: Watch out for "figure_creations"
def p_statement (p):
    '''
    statement : assignment 
                | if 
                | cycle 
                | action 
                | camera 
                | function_call 
                | print
                | increment
                | figure_creations 
                | fig_description
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

#array
def p_v_a (p):
    '''
    v_a : vars_figs
        | vars_prim
        | vars_arr
    '''

def p_vars_start (p):
    '''
    vars_start : VAR VAR_IDENTIFIER SEP_COLON
    '''
    tmp_var.name = p[2]

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
    vars_prim : primitive_type var_p_a
    '''
    FunctionTable.add_var_to_func(function_stack.peek(), tmp_var)


def p_var_p_a (p):
    '''
    var_p_a : init_prim
        | epsilon
    '''

def p_init_prim (p):
    '''
    init_prim : OP_EQUALS init_a
    '''

#array
def p_vars_arr (p):
	'''
	vars_arr : SEP_LBRACKET primitive_type SEP_RBRACKET arr_a
	'''

#array
def p_arr_a (p):
	'''
	arr_a : arr_init_arr
		| init_empty_arr
	'''

#array
#initalization of empty array
def p_init_empty_arr(p):
	'''
	init_empty_arr : 
	'''
	arr_var = Array()
	arr_var.name = tmp_var.name
	arr_var.type = tmp_var.type

	FunctionTable.add_arr_empty_to_func(function_stack.peek(), arr_var)

#array 
#missing array initialization 
def p_arr_init_arr (p):
	'''
	arr_init_arr : SEP_LPAR VAR_INT SEP_RPAR
	'''	
	arr_var = Array()
	arr_var.name = tmp_var.name
	arr_var.type = tmp_var.type
	arr_var.length = p[2]
	FunctionTable.add_arr_complete_to_func(function_stack.peek(), arr_var)


# WARNING: Adds a shift reduce conflict because of function_call
def p_init_a (p):
    '''
    init_a : function_call
        | VAR_IDENTIFIER
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

def p_fig_description(p):
    '''
    fig_description : VAR_IDENTIFIER HAS fig_create_block
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
        | VAR_STRING
    '''

def p_return (p):
    '''
    return : RETURN exp
    '''

def p_print (p):
    '''
    print : PRINT SEP_LPAR print_a SEP_RPAR
    '''
    print("print " + str(p.lexer.lineno))

def p_print_a (p):
    '''
    print_a : exp
        | function_call
        | VAR_STRING
        | VAR_IDENTIFIER
    '''
    


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

parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1) : fin = sys.argv[1]
    else : fin = 'input.in'

    f = open(fin, 'r')
    data = f.read()
    # print data
    # print "End of file"
    parser.parse(data, tracking=True)

    print("Successful")