import light_scanner as lexer
import ply.yacc as yacc
from light_semantic_controller import *
from quadruple import *

tokens = lexer.tokens
function_stack = Stack()
tmp_var = Var()

tmp_function = Function()
function_stack.push('program')

#TODO: Chech what data structure is the best for this case
function_queue = Queue()

#Default functions in queue
function_queue.enqueue('program')
# function_queue.enqueue('window_size')
# function_queue.enqueue('coordinates')

# Quads global structures
operand_stack   = Stack()
operator_stack  = Stack()
type_stack      = Stack()

# Global track keeping
last_func_called = ""
param_counter = 0

# Temp QuadQueue
tmp_quad_stack = Stack()

# Temp ArrayIndex
tmp_array_index = Stack()

# STUFF 4 PUSSEYS
# IF ELDA:
#	IGNORE
IS_ARRAY = True

#Figure Array


# Helper Functions
def build_and_push_quad(op, l_op, r_op, res):
	tmp_quad = Quadruple()
	tmp_quad.build(op, l_op, r_op, res)
	Quadruples.push_quad(tmp_quad)

def exp_quad_helper(p, op_list):
	if operator_stack.isEmpty():
		return
	op = operator_stack.peek()
	str_op = inv_op_dict[op]
	if str_op in op_list:
		t1 = type_stack.pop()
		t2 = type_stack.pop()
		return_type = SemanticCube.cube[op][t1][t2]
		if return_type == -1:
			Error.type_mismatch(p.lexer.lineno, t1, t2, str_op)
		o1 = operand_stack.pop()
		o2 = operand_stack.pop()
		tmp_var_id = SemanticInfo.get_next_var_id(return_type)
		# FunctionTable.function_dict[function_stack.peek()].var_quantities[return_type] += 1


		# Generate Quadruple and push it to the list
		build_and_push_quad(op, o2, o1, tmp_var_id)
		operator_stack.pop()

		# push the tmp_var_id and the return type to stack
		operand_stack.push(tmp_var_id)
		type_stack.push(return_type)

		print "\n> PUSHING OPERATOR '{}' -> op2 = {}, op1 = {}, res = {}".format(str_op, o2, o1, tmp_var_id)
		print_stacks()

def assign_quad_helper(p):
	t1 = type_stack.pop()
	t2 = type_stack.pop()
	if t1 != t2:
		Error.type_mismatch(p.lexer.lineno, t1, t2, '=')
	op = operator_stack.pop()
	o1 = operand_stack.pop()
	o2 = operand_stack.pop()
	print "YAAAAAAAAASSSS {}".format(o2)

	# Generate Quadruple and push it to the list

	if not tmp_array_index.isEmpty():
		print(">Temp array index {}".format(tmp_array_index.peek()))
		build_and_push_quad(op, o1, tmp_array_index.pop(), o2)
	else:
		build_and_push_quad(op, o1, None, o2)

def temporary_quad_4_array():
	o1 = operand_stack.pop()
	temp_id = SemanticInfo.get_next_var_id(abs(o1 // 1000))

	operand_stack.push(temp_id)
	build_and_push_quad(special_operator_dict['eqarr'], o1, tmp_array_index.pop(), temp_id)

def allocate_arr_helper(addr, size):
	op = special_operator_dict['alloc']
	o1 = addr
	o2 = size
	build_and_push_quad(op, o1, o2, None)

def print_quad_helper():
	operand = operand_stack.pop()
	op = operator_stack.pop()
	build_and_push_quad(op, None, None, operand)
	type_stack.pop()

def fig_color_quad_helper(p, color_char, fig_addr):
	type = type_stack.pop()
	if type != type_dict['int']:
		Error.wrong_type('RGB value', type, type_dict['int'], p.lexer.lineno)
	exp_result = operand_stack.pop()
	op = special_operator_dict['addc'] # 'Add Color'
	build_and_push_quad(op, color_char, exp_result, fig_addr)

def fig_size_quad_helper(p, fig_addr):
	fig_type = (abs(fig_addr) // 1000)
	if fig_type != type_dict['circle'] and fig_type != type_dict['square']:
		Error.wrong_attribute_for_figure(fig_type, 'size', p.lexer.lineno)
	type = type_stack.pop()
	if type != type_dict['int']:
		Error.wrong_type('Size value', type, type_dict['int'], p.lexer.lineno)
	exp_result = operand_stack.pop()
	op = special_operator_dict['adds'] # 'Add Color'
	build_and_push_quad(op, None, exp_result, fig_addr)

def push_const_operand_and_type(operand, type):
	type_stack.push(type_dict[type])
	if operand in FunctionTable.constant_dict.keys():
		operand_stack.push(FunctionTable.constant_dict[operand])
		return
	addr = SemanticInfo.get_next_const_id()
	operand_stack.push(addr)
	FunctionTable.constant_dict[operand] = addr

def print_stacks():
	sys.stdout.write("> Operand Stack = ")
	operand_stack.pprint()

	sys.stdout.write("> Operator Stack = ")
	operator_stack.pprint()

	sys.stdout.write("> Type Stack = ")
	type_stack.pprint()


def build_fig_quad():
	#HERE
	op = special_operator_dict['newfig']
	build_and_push_quad(op, None, None, tmp_var.id)


def fig_vertex_quad_helper(p, fig_addr):
	Y = operand_stack.pop()
	X = operand_stack.pop()
	type1 = type_stack.pop()
	type2 = type_stack.pop()

	if type1 != type_dict['int']:
		Error.wrong_type('Vertex value', type1, type_dict['int'], p.lexer.lineno)
	if type2 != type_dict['int']:
		Error.wrong_type('Vertex value', type2, type_dict['int'], p.lexer.lineno)

	op = special_operator_dict['addv'] # 'Add Vertex'
	build_and_push_quad(op, X, Y, fig_addr)

# STATEMENTS ###################################################################
# http://snatverk.blogspot.mx/2011/01/parser-de-mini-c-en-python.html

def p_program (p):
	'''
	program  : PROGRAM VAR_IDENTIFIER SEP_LCBRACKET pr_a main_gosub_quad pr_b main_func SEP_RCBRACKET
	'''
	FunctionTable.add_var_quantities_to_func(function_stack.peek())
	function_stack.pop()
	FunctionTable.print_all()
	sys.stdout.write("Constants dict: ")
	print FunctionTable.constant_dict
	Quadruples.print_all()
	

def p_main_gosub_quad(p):
	'main_gosub_quad : '
	build_and_push_quad(special_operator_dict['era'], 'light', None, None)
	build_and_push_quad(special_operator_dict['gosub'], 'light', None, None)
	Quadruples.push_jump(-1)

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
	main_func : LIGHT_TOKEN new_func_scope main_fill_quad SEP_LPAR SEP_RPAR SEP_LCBRACKET window_name window_func pr_a stmt_loop SEP_RCBRACKET
	'''
	FunctionTable.add_var_quantities_to_func(function_stack.peek())
	function_stack.pop()
	SemanticInfo.reset_var_ids()
	# Generates the 'END' action to finish execution
	build_and_push_quad(special_operator_dict['end'], None, None, None)
	# TODO: Liberar tabla de variables

def p_window_func(p):
	'''
	window_func : WINDOW_SIZE SEP_LPAR VAR_IDENTIFIER SEP_COLON cnt_prim SEP_COMMA VAR_IDENTIFIER SEP_COLON cnt_prim SEP_RPAR
		| epsilon
	'''
	if len(p) < 6:
		return None
	if p[3] != 'width' or p[7] != 'height':
		Error.wrong_window_declaration(p.lexer.lineno)
	t1 = type_stack.pop()
	t2 = type_stack.pop()
	int_type = type_dict['int']
	if t1 != int_type or t2 != int_type:
		tmp_type = t1 if t1 != int_type else t2
		Error.wrong_type('window_size', tmp_type, int_type, p.lexer.lineno)

	n1 = operand_stack.pop(); type_stack.pop();
	n2 = operand_stack.pop(); type_stack.pop();
	build_and_push_quad(special_operator_dict['wsize'], None, n1, n2)


def p_main_fill_quad(p):
	'main_fill_quad : '
	tmp_end = Quadruples.pop_jump()
	tmp_count = Quadruples.next_free_quad
	Quadruples.fill_missing_quad(tmp_end, tmp_count)

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
	'''
	p[0] = p[1]
	tmp_var.type = type_dict[p[1]]
	tmp_function.type = type_dict[p[1]]

def p_figure (p):
	'''
	figure :  LINE 
			| TRIANGLE 
			| SQUARE 
			| RECTANGLE 
			| POLYGON 
			| CIRCLE
	'''
	p[0] = p[1]
	type_stack.push(type_dict[p[1]])
	

def p_stmt_loop (p):
	'''
	stmt_loop : statement  stmt_loop
		| epsilon
	'''

def p_function (p):
	'''
	function : FUNCTION VAR_IDENTIFIER new_func_scope SEP_LPAR func_a SEP_RPAR func_b add_return_val SEP_LCBRACKET func_c stmt_loop tmp_return verify_return_stmt SEP_RCBRACKET
	'''
	FunctionTable.add_var_quantities_to_func(function_stack.peek())
	function_stack.pop()
	SemanticInfo.reset_var_ids()
	# Generates the 'RET' action at the end of the function
	build_and_push_quad(special_operator_dict['ret'], None, None, None)
	# TODO: Liberar tabla de variables

def p_func_a (p):
	'''
	func_a : parameters
		| epsilon
	'''
def p_func_b (p):
	'''
	func_b : RETURNS primitive_type
		| epsilon epsilon
	'''
	p[0] = p[2] # IMPORTANT, TODO: ugh, this is ugly

def p_add_return_val (p):
	'''
	add_return_val : epsilon
	'''
	tmp_type = type_dict[p[-1]] if p[-1] else type_dict['void']
	print "\n> Adding return value to '{}': type = {}".format(tmp_function.name, tmp_type)
	FunctionTable.add_return_type_to_func(tmp_function.name, tmp_type)

def p_func_c (p):
	'''
	func_c : vars func_c
		| epsilon
	'''

def p_tmp_return(p):
	'''
	tmp_return : RETURN opt_exp
		| epsilon
	'''

def p_opt_exp(p):
	'''
	opt_exp : exp return_found 
		| empty_return_found
	'''

def p_return_found(p):
	'return_found : epsilon '
	#if function is void and has return
	if FunctionTable.function_returns_void(function_stack.peek()):
		Error.return_type_function_void(function_stack.peek(), p.lexer.lineno)

	#found Return Type
	FunctionTable.set_return_found(function_stack.peek(), True)

	# building and pushing the 'return' quad
	op = special_operator_dict['return']
	glbl_addr = FunctionTable.function_dict['program'].vars[tmp_function.name].id
	build_and_push_quad(op, operand_stack.pop(), None, glbl_addr)

def p_empty_return_found(p):
	'empty_return_found : '
	# building and pushing the 'ret' quad becuase of empty return stmt
	build_and_push_quad(special_operator_dict['ret'], None, None, None)

def p_verify_return_stmt(p):
	'''
	verify_return_stmt : 
	'''
	#if function is not void
	if not FunctionTable.function_returns_void(function_stack.peek()):
		if not FunctionTable.function_has_return_stmt(function_stack.peek()):
			Error.no_return_type(function_stack.peek(), p.lexer.lineno)


def p_new_func_scope(p):
	'new_func_scope :'
	function_stack.push(p[-1])
	function_queue.enqueue(p[-1])
	tmp_function.name = p[-1]
	tmp_function.type = type_dict['void']
	tmp_function.quad_index = Quadruples.next_free_quad
	FunctionTable.add_function(tmp_function)

##TODO VERIFY VAR_IDENTIFIER
def p_parameters (p):
	'parameters : VAR_IDENTIFIER SEP_COLON type new_param_seen param_a'

def p_new_param_seen(p):
	'new_param_seen : '
	aux_var = Var() # TODO: Wtf hack
	tmp_var.name = p[-3]
	tmp_var.type = type_dict[p[-1]]
	aux_var = tmp_var
	aux_var = FunctionTable.add_var_to_func(tmp_function.name, tmp_var)
	FunctionTable.add_param_to_func(tmp_function.name, p[-3], aux_var)

def p_param_a (p):
	'''
	param_a : SEP_COMMA parameters
		| epsilon
	'''

def p_var_array_ver(p):
	'''
	var_array_ver : SEP_LBRACKET exp var_array_ver_aux SEP_RBRACKET 
		| epsilon
	'''
	if(len(p) > 3):
		p[0] = True

def p_var_array_ver_aux(p):
	'var_array_ver_aux : epsilon' #ERROR HERE
	tmp_array_index.push(operand_stack.pop())


def p_function_call(p):
	'''
	function_call : VAR_IDENTIFIER verify_function_call SEP_LPAR call_parameters SEP_RPAR pop_ff
	'''
	func = FunctionTable.function_dict[p[1]]
	address = func.quad_index
	build_and_push_quad(special_operator_dict['gosub'], p[1], None, address)

	# create a temporal var_id on the function as the same type of func_call
	next_id = SemanticInfo.get_next_var_id(func.type)
	# glbl_addr = FunctionTable.get_var_in_scope(p, 'program', func.name).id
	glbl_addr = operand_stack.pop(); type_stack.pop();
	build_and_push_quad(special_operator_dict['='], glbl_addr, None, next_id)
	operand_stack.push(next_id)
	type_stack.push(func.type)

	# verify arguments count
	global param_counter
	n = len(func.params)
	if param_counter != n:
		Error.param_number_mismatch(p.lexer.lineno-1, p[1], n, param_counter)

	param_counter = 0 # global var reset

def p_verify_function_call(p):
	'verify_function_call : push_ff'
	# print("Function queue")
	# TODO: delegate this task to FunctionTable class

	if not function_queue.inQueue(p[-1]):
		Error.function_not_defined(p[-1],p.lexer.lineno)
	global last_func_called
	last_func_called = p[-1]
	func = FunctionTable.function_dict[p[-1]]
	build_and_push_quad(special_operator_dict['era'], func.name, None, None)

	# Pushing the fucntion as a variable id when a function is called
	func_var = FunctionTable.get_var_in_scope(p, 'program', func.name)
	operand_stack.push(func_var.id)
	type_stack.push(func_var.type)

def p_test(p):
	'''
	test : 
	'''
	print("test: " + str(p.lexer.lineno))

def p_call_parameters(p):
	'''
	call_parameters : VAR_IDENTIFIER var_array_ver SEP_COLON exp verify_param call_param_a
		| epsilon
	'''
def p_call_param_a(p):
	'''
	call_param_a : SEP_COMMA call_parameters
		| epsilon
	'''
def p_verify_param(p):
	'verify_param : '
	param_name = p[-4]
	arg = operand_stack.pop()
	arg_type = type_stack.pop()
	if not FunctionTable.verify_param_at_index(last_func_called, param_name, arg_type, param_counter):
		Error.param_mismatch( p.lexer.lineno, param_name, arg_type)
	build_and_push_quad(special_operator_dict['param'], arg, last_func_called, param_counter)
	global param_counter
	param_counter = param_counter + 1
 
def p_assignment (p):
	'''
	assignment : var_id OP_EQUALS push_operator exp 
	'''
	print("assignment: " + str(p.lexer.lineno))
	assign_quad_helper(p)

def p_cycle (p):
	'''
	cycle : while 
		| for 
	'''
	print("cycle: " + str(p.lexer.lineno))

def p_while (p):
	'''
	while : WHILE SEP_LPAR condition SEP_RPAR start_loop_helper do_block end_while_helper
	'''

def p_end_while_helper (p) :
	'''
	end_while_helper : epsilon
	'''
	tmp_false = Quadruples.pop_jump()
	tmp_return = Quadruples.pop_jump()

	#fill the return value #CHANGED
	build_and_push_quad(special_operator_dict['goto'], None, None, tmp_return - 1)

	#fill false with count
	tmp_count = Quadruples.next_free_quad
	tmp_quad = Quadruples.fill_missing_quad(tmp_false, tmp_count)

def p_for (p):
	'''
	for : FOR SEP_LPAR for_a SEP_SEMICOLON condition start_loop_helper SEP_SEMICOLON for_b SEP_RPAR do_block end_for_helper
	'''
	print("for" + str(p.lexer.lineno))

def p_start_loop_helper (p):
	'''
	start_loop_helper : epsilon
	'''

	#Put count in JUMPSTACK
	Quadruples.push_jump(0)

	aux = type_stack.pop()
	if aux != 1 :
		Error.not_a_condition(aux, p.lexer.lineno)
	else :
		res = operand_stack.pop()
		operator = special_operator_dict['gotof']

		# Generate Quadruple and push it to the list
		tmp_quad = Quadruple()
		tmp_quad.build(operator, res, None, None)
		Quadruples.push_quad(tmp_quad)

		#Push into jump stack
		Quadruples.push_jump(-1)

def p_end_for_helper (p) :
	'''
	end_for_helper : epsilon
	'''
	tmp_false = Quadruples.pop_jump()
	tmp_return = Quadruples.pop_jump()

	offset = p[-3]

	Quadruples.push_quad(tmp_quad_stack.pop())
	if(offset == 1) :
		Quadruples.push_quad(tmp_quad_stack.pop())

	#fill the return value
	build_and_push_quad(17, None, None, tmp_return - offset)

	#fill false with count
	tmp_count = Quadruples.next_free_quad
	tmp_quad = Quadruples.fill_missing_quad(tmp_false, tmp_count)


def p_for_a (p):
	'''
	for_a : assignment 
		| epsilon
	'''

def p_for_b (p):
	'''
	for_b : increment tmp_increment
		| assignment tmp_assign
	'''
	p[0] = p[2]

def p_tmp_increment (p):
	'tmp_increment : epsilon'
	p[0] = 1
	tmp_quad_stack.push(Quadruples.pop_quad())
	tmp_quad_stack.push(Quadruples.pop_quad())

def p_tmp_assign (p):
	'tmp_assign : epsilon'
	p[0] = 0
	tmp_quad_queue.push(Quadruples.pop_quad())



# def p_action (p):
# 	'''
# 	action : ACTION act_a 
# 	'''

# def p_act_a (p):
# 	'''
# 	act_a : act_move
# 		| act_scale
# 		| act_visible
# 	'''

# def p_act_header (p):
# 	'act_header : VAR_IDENTIFIER DO  BEGINS SEP_COLON exp SEP_COMMA  ENDS SEP_COLON exp'

# def p_act_move (p):
# 	'act_move : MOVE act_header SEP_COMMA POS_X SEP_COLON exp SEP_COMMA  POS_Y SEP_COLON exp END'

# def p_act_scale (p):
# 	'act_scale : SCALE act_header SEP_COMMA SIZE SEP_COLON exp END'

# # def p_act_rotate (p):
# # 	'act_rotate : SCALE act_header SEP_COMMA ANGLE SEP_COLON exp SEP_COMMA END'

# def p_act_visible (p):
# 	'''
# 	act_visible : HIDE act_header END
# 		| SHOW act_header END
# 	'''

def p_camera (p):
	'camera : CAMERA VAR_IDENTIFIER verify_variable'
	aux_var = FunctionTable.get_var_in_scope(p, function_stack.peek(), p[2])
	build_and_push_quad(special_operator_dict['cam'], None, None, aux_var.id)

def p_move (p):
	'move : MOVE VAR_IDENTIFIER verify_variable SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_COMMA VAR_IDENTIFIER SEP_COLON exp SEP_RPAR'
	if p[5] != 'x' or p[9] != 'y':
		Error.wrong_move_declaration(p.lexer.lineno)
	aux_var = FunctionTable.get_var_in_scope(p, function_stack.peek(), p[2])
	y = operand_stack.pop(); type_stack.pop();
	x = operand_stack.pop(); type_stack.pop();
	build_and_push_quad(special_operator_dict['move'], x, y, aux_var.id)

def p_wait (p):
	'wait : WAIT SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_RPAR'
	if p[3] != 'ms':
		Error.wrong_wait_declaration(p.lexer.lineno)
	type = type_stack.pop();
	if type != type_dict['int'] and type != type_dict['decimal']:
		Error.wrong_type('wait', type, type_dict['decimal'], p.lexer.lineno)
	time_in_ms = operand_stack.pop()
	build_and_push_quad(special_operator_dict['wait'], None, None, time_in_ms)

def p_move_speed (p):
	'move_speed : MOVE_SPEED SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_RPAR'
	if p[3] != 'ms':
		Error.wrong_wait_declaration(p.lexer.lineno)
	type = type_stack.pop();
	if type != type_dict['int'] and type != type_dict['decimal']:
		Error.wrong_type('move speed', type, type_dict['decimal'], p.lexer.lineno)	
	time_in_ms = operand_stack.pop()
	build_and_push_quad(special_operator_dict['mvs'], None, None, time_in_ms)

def p_hide (p):
	'hide : HIDE VAR_IDENTIFIER verify_variable fig_tmp_var'
	build_and_push_quad(special_operator_dict['hide'], None, None, tmp_var.id)

def p_show (p):
	'show : SHOW VAR_IDENTIFIER verify_variable fig_tmp_var'
	build_and_push_quad(special_operator_dict['show'], None, None, tmp_var.id)

# def p_rotate(p):
# 	'rotate : ROTATE VAR_IDENTIFIER verify_variable SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_RPAR'
# 	if p[5] != 'deg':
# 		Error.wrong_rotate_declaration(p.lexer.lineno)
# 	type = type_stack.pop()
# 	if type != type_dict['int']:
# 		Error.wrong_type('rotate', type, type_dict['int'], p.lexer.line)
# 	degree = operand_stack.pop()
# 	build_and_push_quad(special_operator_dict['rotate'], degree, None, tmp_var.id)

# def p_scale(p):
# 	'scale : SCALE VAR_IDENTIFIER verify_variable SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_RPAR'
# 	if p[5] != 'by':
# 		Error.wrong_scale_declaration(p.lexer.lineno)
# 	type = type_stack.pop()
# 	if type != type_dict['int']:
# 		Error.wrong_type('scale', type, type_dict['int'], p.lexer.line)

# 	by = operand_stack.pop()
# 	build_and_push_quad(special_operator_dict['scale'], by , None, tmp_var.id)

def p_window_name(p):
	'''
	window_name : WINDOW_NAME SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_RPAR
				| epsilon
	'''
	if len(p) > 2:
		if p[3] != "name":
			Error.wrong_name_window(p.lexer.lineno)

		type = type_stack.pop()
		if type != type_dict['string']:
			Error.wrong_name_window(p.lexer.lineno)

		name = operand_stack.pop()

		build_and_push_quad(special_operator_dict['winame'], None, None, name)


def p_background_color (p):
	'background_color : BACKGROUND_COLOR SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_COMMA VAR_IDENTIFIER SEP_COLON exp SEP_COMMA VAR_IDENTIFIER SEP_COLON exp SEP_RPAR'
	if p[3] != 'r' or p[7] != 'g' or p[11] != 'b':
		Error.wrong_bgc_declaration(p.lexer.lineno)

	exp_type_list = [type_stack.pop() for x in xrange(3)]
	type_list = [type_dict['int'], type_dict['decimal']]
	intersect = [i for i in exp_type_list if i in type_list]

	if len(intersect) != len(exp_type_list):
		diff = [i for i in exp_type_list if i not in intersect]
		Error.wrong_type('background_color attr', diff[0], type_dict['decimal'], p.lexer.lineno)

	res = [operand_stack.pop() for x in xrange(3)]
	build_and_push_quad(special_operator_dict['bgc'], res[2], res[1], res[0])

# TODO: refactor this and the above rule
def p_text_color (p):
	'text_color : TEXT_COLOR SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_COMMA VAR_IDENTIFIER SEP_COLON exp SEP_COMMA VAR_IDENTIFIER SEP_COLON exp SEP_RPAR'
	if p[3] != 'r' or p[7] != 'g' or p[11] != 'b':
		Error.wrong_txtc_declaration(p.lexer.lineno)

	exp_type_list = [type_stack.pop() for x in xrange(3)]
	type_list = [type_dict['int'], type_dict['decimal']]
	intersect = [i for i in exp_type_list if i in type_list]

	if len(intersect) != len(exp_type_list):
		diff = [i for i in exp_type_list if i not in intersect]
		Error.wrong_type('text_color attr', diff[0], type_dict['int'], p.lexer.lineno)

	res = [operand_stack.pop() for x in xrange(3)]
	build_and_push_quad(special_operator_dict['txtc'], res[2], res[1], res[0])

	# TODO: refactor this and the above rule
def p_print_g (p):
	'print_g : PRINT_G SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_COMMA VAR_IDENTIFIER SEP_COLON exp SEP_COMMA VAR_IDENTIFIER SEP_COLON exp SEP_RPAR'
	if p[3] != 'text' or p[7] != 'x' or p[11] != 'y':
		Error.wrong_printg_declaration(p.lexer.lineno)

	exp_type_list = [type_stack.pop() for x in xrange(2)]
	type_list = [type_dict['int']]
	intersect = [i for i in exp_type_list if i in type_list]

	if len(intersect) != len(exp_type_list):
		diff = [i for i in exp_type_list if i not in intersect]
		Error.wrong_type('text_color x or y', diff[0], type_dict['int'], p.lexer.lineno)

	text_type = type_stack.pop()
	type_list += [type_dict['decimal'], type_dict['string']]
	if text_type not in type_list:
		Error.wrong_type('text_color text', text_type, type_dict['string'], p.lexer.lineno)

	res = [operand_stack.pop() for x in xrange(3)]
	build_and_push_quad(special_operator_dict['printg'], res[1], res[0], res[2])

##AND OR ret
def p_condition (p):
	'''
	condition : expresion quad_helper_and_or cond_a
	'''
	print("condition: " + str(p.lexer.lineno))

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
	operator_stack.push(operator_dict[p[1]])

def p_quad_helper_and_or(p):
	'quad_helper_and_or : '
	exp_quad_helper(p, ['and', 'or'])

def p_expresion(p):
	'''
	expresion : exp quad_helper_cond expresion_a
	'''
	print("expresion: " + str(p.lexer.lineno))

def p_expresion_a(p):
	'''
	expresion_a : ex_a expresion
		| epsilon
	'''

def p_ex_a (p):
	'''
	ex_a : OP_LESS_THAN
		| OP_GREATER_THAN
		| OP_NOT_EQUAL
		| OP_EQUALSS
		| OP_GREATER_EQUAL
		| OP_LESS_EQUAL
	'''
	operator_stack.push(operator_dict[p[1]])

def p_quad_helper_cond(p):
	'quad_helper_cond : '
	exp_quad_helper(p, ['<', '>', '!=', '==', '>=', '<='])

def p_exp (p):
	'''
	exp : term quad_helper_sum exp_a
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
	operator_stack.push(operator_dict[p[1]])

def p_quad_helper_sum(p):
	'quad_helper_sum : '
	print "\n> QUAD HELPER SUM:"
	print_stacks()
	exp_quad_helper(p, ['+', '-'])

def p_term (p):
	'''
	term : factor quad_helper_mult term_a
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
	operator_stack.push(operator_dict[p[1]])

def p_quad_helper_mult(p):
	'quad_helper_mult : '
	exp_quad_helper(p, ['*', '/'])

def p_factor (p):
	'''
	factor : SEP_LPAR quad_push_lpar condition SEP_RPAR quad_pop_lpar
		| function_call 
		| var_cte
	'''
	print("factor: " + str(p.lexer.lineno))

def p_push_ff(p):
	'push_ff : '
	operator_stack.push(special_operator_dict['('])

def p_pop_ff(p):
	'pop_ff : '
	operator_stack.pop()

def p_quad_push_lpar(p):
	'quad_push_lpar : '
	operator_stack.push(special_operator_dict[p[-1]])

def p_quad_pop_lpar(p):
	'quad_pop_lpar : '
	operator_stack.pop()

def p_var_cte(p):
	'''
	var_cte : var_id 
		| cnt_prim
	'''
	if p[1] == IS_ARRAY:
		temporary_quad_4_array()

def p_increment (p):
	#exp 			
	'''
	increment : VAR_IDENTIFIER verify_variable var_array_ver double_pushID inc_a exp do_sum_rest
	'''

	#push equals
	op = special_operator_dict["="]
	operator_stack.push(op)

	assign_quad_helper(p)

def p_double_pushID (p):
	'''
	double_pushID : epsilon
	'''

	func = FunctionTable.function_dict[function_stack.peek()]
	type_stack.push(func.vars[p[-3]].type)
	operand_stack.push(func.vars[p[-3]].id)

	func = FunctionTable.function_dict[function_stack.peek()]
	type_stack.push(func.vars[p[-3]].type)
	operand_stack.push(func.vars[p[-3]].id)

def p_do_sum_rest (p):
	'''
	do_sum_rest : epsilon
	'''

	print(p[-2])
	if p[-2] == "+=":
		operator_stack.push(0)
	else:
		operator_stack.push(1)

	exp_quad_helper(p, ['+', '-'])


def p_inc_a (p):
	'''
	inc_a :  OP_PLUS_EQUALS
		| OP_MINUS_EQUALS
	'''

	print(p[1])
	p[0] = p[1]
	
#This was in increment
def p_inc_var_cte(p): 
	'''
	inc_var_cte : var_id
		| sign VAR_INT push_num 
		| exp
	'''
#PROBADO VAR_INT y VAR_IDENTIFIER

def p_if (p):
	'''
	if : IF SEP_LPAR condition SEP_RPAR quad_if_helper do_block if_a if_b end_if_stmt_quad_helper
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

def p_quad_if_helper(p):
	'''
	quad_if_helper : epsilon
	'''
	type = type_stack.pop()
	if type != type_dict['boolean']:
		Error.not_a_condition(type, p.lexer.lineno)
	else :
		res = operand_stack.pop()
		operator = special_operator_dict['gotof']

		# Generate Quadruple and push it to the list
		tmp_quad = Quadruple()
		tmp_quad.build(operator, res, None, None)
		Quadruples.push_quad(tmp_quad)

		#Push into jump stack
		Quadruples.push_jump(-1)

		print("PUSH JUMP :")
		Quadruples.print_jump_stack()

def p_elsif (p):
	'''
	elsif : ELSIF end_if_stmt_quad_helper SEP_LPAR condition SEP_RPAR quad_if_helper do_block if_a
	'''

def p_else (p):
	'''
	else : ELSE quad_else_helper do_block
	'''

def p_quad_else_helper(p):
	'''
	quad_else_helper : epsilon
	'''
	operator = special_operator_dict['goto']

	tmp_quad = Quadruple()
	tmp_quad.build(operator, None, None, None)
	Quadruples.push_quad(tmp_quad)

	tmp_false = Quadruples.pop_jump()
	tmp_count = Quadruples.next_free_quad
	tmp_quad = Quadruples.fill_missing_quad(tmp_false, tmp_count)

	Quadruples.push_jump(-1)

def p_end_if_stmt_quad_helper(p):
	'end_if_stmt_quad_helper : epsilon'

	#print("PUSH JUMP BEF POP:")
	Quadruples.print_jump_stack()

	tmp_end = Quadruples.pop_jump()
	#print("POPJUMP")
	print(tmp_end)	
	tmp_count = Quadruples.next_free_quad
	tmp_quad = Quadruples.fill_missing_quad(tmp_end, tmp_count)


def p_condition_block (p):
	'condition_block : SEP_LPAR condition SEP_RPAR do_block'
	print("conditionBlock " + str(p.lexer.lineno))

def p_do_block (p):
	'do_block : DO stmt_loop END'
	print("doBlock " + str(p.lexer.lineno))

# WARNING: Watch out for "figure_creations"
def p_statement (p):
	'''
	statement : assignment 
				| if 
				| cycle  
				| camera 
				| move
				| wait
				| move_speed
				| hide
				| show
				| background_color
				| text_color
				| print_g
				| function_call 
				| print
				| increment
				| fig_description
				| return
	'''

def p_vars (p):
	'vars : vars_start'

#array
def p_v_a (p):
	'''
	v_a : vars_prim
		| vars_arr
	'''

def p_vars_start (p):
	'''
	vars_start : VAR VAR_IDENTIFIER push_var_name SEP_COLON v_a
			| FIGURE VAR_IDENTIFIER push_var_name SEP_COLON figure add_fig_quad vf_a
	'''


def p_push_var_name(p):
	'push_var_name : epsilon'
	tmp_var.name = p[-1]

def p_vf_a (p):
	'''
	vf_a : HAS fig_create_block
		| epsilon
	'''

def p_vars_prim (p):
	'vars_prim : primitive_type var_p_a'
	aux_var = FunctionTable.add_var_to_func(function_stack.peek(), tmp_var)
	tmp_var.id = aux_var.id # Nasty hack brawh

def p_var_p_a (p):
	'''
	var_p_a : init_prim
		| epsilon
	'''

def p_init_prim (p):
	'init_prim : push_tmp_var OP_EQUALS push_operator exp'
	assign_quad_helper(p)

def p_push_tmp_var(p):
	'push_tmp_var : '
	type_stack.push(tmp_var.type)
	# TODO: Refactor this nasty shieeet
	if function_stack.peek() == 'program':
		tmp_var.id = -SemanticInfo.current_global_var_id[tmp_var.type]
	else:
		tmp_var.id = SemanticInfo.current_var_id[tmp_var.type]
	operand_stack.push(tmp_var.id)

#array
def p_vars_arr (p):
	'''
	vars_arr : SEP_LBRACKET primitive_type SEP_RBRACKET SEP_LPAR VAR_INT SEP_RPAR init_arr 
	'''

#SEP_LPAR VAR_INT SEP_RPAR
#initalization of empty array
def p_init_arr(p):
	'''
	init_arr : 
	'''
	arr_var = Array()
	arr_var.name = tmp_var.name
	arr_var.type = tmp_var.type
	arr_var.length = p[-2]

	arr_var = FunctionTable.add_arr_to_func(function_stack.peek(), arr_var)
	allocate_arr_helper(arr_var.id, arr_var.length)

	#FunctionTable.get_var_in_scope(p, function_stack.peek(), arr_var.name)

# WARNING: Adds a shift reduce conflict because of function_call
def p_init_a (p):
       '''
       init_a : function_call
               | var_cte
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
		| fig_color_attr
		| SIZE SEP_COLON exp add_size 
	'''

def p_add_size(p):
	'add_size : '
	fig_size_quad_helper(p, tmp_var.id)

def p_fig_description(p):
	'fig_description : VAR_IDENTIFIER HAS fig_tmp_var fig_create_block'
	build_and_push_quad(special_operator_dict['rst'], None, None, tmp_var.id)

def p_fig_tmp_var(p):
	'fig_tmp_var : '
	aux_var = FunctionTable.get_var_in_scope(p, function_stack.peek(), p[-2])
	tmp_var.id = aux_var.id
	tmp_var.name = aux_var.name
	tmp_var.type = aux_var.type

def p_vector (p):
	'''
	vector : VAR_VECTORID SEP_COLON SEP_LPAR VAR_IDENTIFIER SEP_COLON exp SEP_COMMA VAR_IDENTIFIER SEP_COLON exp SEP_RPAR 
	'''
	if p[4] != "x" or p[8] != "y":
		Error.wrong_figure_vertex_declaration(p.lexer.lineno)
	fig_vertex_quad_helper(p, tmp_var.id)

def p_fig_color_attr(p):
	'fig_color_attr : COLOR SEP_COLON SEP_LPAR VAR_IDENTIFIER SEP_COLON exp add_red SEP_COMMA VAR_IDENTIFIER SEP_COLON exp add_green SEP_COMMA VAR_IDENTIFIER SEP_COLON exp add_blue SEP_RPAR'
	if p[4] != "r" or p[9] != "g" or p[14] != "b":
		Error.wrong_figure_color_declaration(p.lexer.lineno)	

def p_add_red(p):
	'add_red : '
	fig_color_quad_helper(p, 'r', tmp_var.id)

def p_add_green(p):
	'add_green : '
	fig_color_quad_helper(p, 'g', tmp_var.id)
	
def p_add_blue(p):
	'add_blue : '
	fig_color_quad_helper(p, 'b', tmp_var.id)
	

def p_cnt_prim (p):
	'''
	cnt_prim : sign VAR_INT push_num
		| sign VAR_DECIMAL push_num
		| VAR_STRING push_string
		| VAR_BOOLEAN push_bool
	'''

def p_sign (p):
	'''
	sign : OP_PLUS
		| OP_MINUS
		| epsilon
	'''
	p[0] = p[1]

def p_return (p):
	'''
	return : RETURN opt_exp
	'''

def p_print (p):
	'''
	print : PRINT push_operator SEP_LPAR print_a SEP_RPAR
	'''
	print("print " + str(p.lexer.lineno))

def p_print_a (p):
	'print_a : exp'
	print_quad_helper()
	
def p_figure_creations (p):
	'''
	figure_creations : FIGURE VAR_IDENTIFIER push_var_name SEP_COLON figure add_fig_quad HAS fig_create_block
	'''
	pass

def p_add_fig_quad(p):
	'''
	add_fig_quad : epsilon
	'''
	#HERE
	tmp_var.type = type_stack.pop()
	aux_var = FunctionTable.add_var_to_func(function_stack.peek(), tmp_var)
	tmp_var.id = aux_var.id
	build_fig_quad()

def p_var_id(p):
	'var_id : VAR_IDENTIFIER verify_variable var_array_ver push_id'
	if p[3]:
		p[0] = True

def p_push_id(p):
	'push_id : '
	var = FunctionTable.get_var_in_scope(p, function_stack.peek(), p[-3])
	type_stack.push(var.type)
	operand_stack.push(var.id)

def p_push_num(p):
	'push_num : '
	num = eval(p[-1])
	if p[-2]:
		print p[-2]
		num = num * -1 if p[-2] == '-' else num
		print num
	type = 'decimal' if isinstance(num, (float)) else 'int'
	push_const_operand_and_type(num, type)

def p_push_string(p):
	'push_string : '
	push_const_operand_and_type(p[-1], 'string')

def p_push_bool(p):
	'push_bool : '
	push_const_operand_and_type(p[-1], 'boolean')

def p_push_operator(p):
	'push_operator : '
	try:
		op = operator_dict[p[-1]]
	except KeyError:
		op = special_operator_dict[p[-1]]
	operator_stack.push(op)

def p_verify_variable(p):
	'verify_variable : '
	func = function_stack.peek()
	if not FunctionTable.verify_var_in_func(func, p[-1]):
		Error.variable_not_defined(p[-1], p.lexer.lineno)

def p_epsilon(p):
	'epsilon :'
	pass


def p_error(p):
	print "Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value)
	sys.exit(0)

# MAIN #########################################################################

from virtual_machine import *

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

	RUN_AT_LIGHTSPEED()

