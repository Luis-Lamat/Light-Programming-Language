# Semantic Controller

from error import * # Includes light_data_structures.py
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

# DEFINE CLASSES
class Var:
	# Instance
	def __init__(self):
		self.id = -1
		self.name = ""
		self.type = 0
		self.value = None

	def erase(self):
		self.id = -1
		self.name = ""
		self.type = 0
		self.value = None

	def init_var(self, id, name, type, value):
		self.id = id
		self.name = name
		self.type = type
		self.value = value

	def print_var(self):
		print "\t\tid: " + str(self.id) + ",\n\t\tname: " + self.name  + ",\n\t\ttype: " + str(self.type) + ",\n\t\tvalue: " + str(self.value)
		print "\t\t---------"

class Array:

	def __init__(self):
		self.id = -1
		self.name = ""
		self.type = 0
		self.length = 0
		#self.data = []

	# #initialize when length is received 
	# def init_arr_all(self, id, name, type, length):
	# 	self.id = id
	# 	self.name = name
	# 	self.type = type 
	# 	self.length = int(length)
	# 	for i in range(self.length):
 # 			self.data.append(initializer_dict[type])

 	#initialize when length is unknown
 	def init_arr(self, id, name, type, length):
 		self.id = id
		self.name = name
		self.type = type
		self.length = length

	# # add length when known
	# def add_length(self, length):
	# 	self.length = length
	# 	for i in range(length):
 # 			self.data.append(initializer_dict[self.type])

 # 	#return n element on the array
 # 	def get_element(self, num):
 # 		if sum < self.length:
 # 			return data[num]
 # 		else:
 # 			Error.out_of_bounds(self.name, num)

 	def print_arr(self):
 		print "\t\tARRAY! \n\t\tid: " + str(self.id) + ",\n\t\tname: " + self.name  + ",\n\t\ttype: " + str(self.type) + ",\n\t\tlength: " + str(self.length)
 	# 	if isinstance(self.data, str) :
		# 	print(', '.join(self.data))
		# else:
 	# 		print("\t\t" + str(self.data))
 	# 	print "\t\t---------"

 	#to be able to print all
 	def print_var(self):
 		self.print_arr()


class Function:
	def __init__(self):
		self.id = -1
		self.name = ""
		self.type = 0 # "" before
		self.vars = {}
		self.var_quantities = [0 for x in xrange(len(type_dict))]
		self.params = []
		self.quad_index = -1
		self.has_return = False

	def erase(self):
		self.id = -1
		self.name = ""
		self.type = 0 # "" before
		self.vars = {}
		self.var_quantities = [0 for x in xrange(len(type_dict))]
		self.params = []
		self.quad_index = -1
		self.has_return = False

	def init_func(self, id, name, type, q_index):
		self.id = id
		self.name = name
		self.type = type
		self.quad_index = q_index
		self.has_return = False

	def add_var(self, var):
		print "\n> Add_var called"
		if var.name not in self.vars:
			tmp_var = Var() # TODO: dafuq with this????
			tmp_var.init_var(None, var.name, var.type, var.value)

			# leave this code as if else, DON'T refactor
			if self.name == 'program':
				tmp_var.id = SemanticInfo.get_next_global_var_id(var.type)
			else:
				tmp_var.id = SemanticInfo.get_next_var_id(var.type)

			self.vars[var.name] = tmp_var
			print self.vars
			return tmp_var
		else:
			print "> Else entered"
			print self.vars
			Error.already_defined('variable', var.name)


	def add_arr(self, arr):
		if arr.name not in self.vars:
			tmp_arr = Array()
			tmp_arr.init_arr(None, arr.name, arr.type, arr.length)
			
			# leave this code as if else, DON'T refactor
			if self.name == 'program':
				tmp_arr.id = SemanticInfo.get_next_global_var_id(arr.type)
			else:
				tmp_arr.id = SemanticInfo.get_next_var_id(arr.type)

			self.vars[arr.name] = tmp_arr
			return tmp_arr
		else:
			Error.already_defined('variable array', arr.name)

	def is_arr(self, name):
		if hasattr(self.vars[name], 'length'):
			return True
		else:
			return False

	# def add_arr_complete(self, arr):
	# 	if arr.name not in self.vars:
	# 		tmp_arr = Array()
	# 		tmp_arr.init_arr_all(SemanticInfo.get_next_var_id(arr.type), arr.name, arr.type, arr.length)
	# 		self.vars[arr.name] = tmp_arr
	# 	else:
	# 		Error.already_defined('variable array', arr.name)

	# TODO: Oh gosh, refactor please...
	def var_in_func(self, name):
		if name in self.vars.keys():
			return True
		else :
			return False

	def print_all(self):
		print "\tid: " + str(self.id) + ",\n\tname: " + self.name  + ",\n\ttype: " + str(self.type)
		sys.stdout.write("\tParams: ")
		print self.params
		print "\tStarting quad index = " + str(self.quad_index)
		for k in self.vars:
			print "\tVAR - " + k + ":"
			self.vars[k].print_var()

	def function_is_void(self):
		return self.type == 0

	def set_has_Return(self, type):
		self.has_return = type

	def get_has_Return(self):
		return self.has_return


class FunctionTable:
	global_func = Function()
	global_func.init_func(0, 'program', type_dict['void'], None)
	
	function_dict = {
		'program' : global_func
	}

	constant_dict = {}

	next_func_id = 1
	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state

	@classmethod
	def add_function(cls, func):
		if func.name not in cls.function_dict:
			tmp_func = Function() # TODO: Why so much copy?
			tmp_func.init_func(cls.next_func_id, func.name, func.type, func.quad_index)
			cls.function_dict[func.name] = tmp_func
			cls.next_func_id += 1
		else:
			Error.already_defined('function', func.name)

	@classmethod
	def add_return_type_to_func(cls, name, type):
		cls.function_dict[name].type = type
		# Here we add a global var with the name of the func to make return
		# values easier to handle
		tmp_var = Var()
		tmp_var.init_var(-1, name, type, None)
		cls.function_dict['program'].add_var(tmp_var)

	@classmethod
	def add_var_quantities_to_func(cls, function_name):
		if function_name == 'program':
			var_qs = SemanticInfo.current_global_var_id
		else:
			var_qs = SemanticInfo.current_var_id

		q = [(x%1000) for x in var_qs]
		print "> Var q's for func '{}': {}".format(function_name, q)
		cls.function_dict[function_name].var_quantities = q

	@classmethod
	def print_all(cls):
		for x in cls.function_dict:
			print (x + ":")
			cls.function_dict[x].print_all()

	@classmethod
	def add_var_to_func(cls, function_name, var_obj):
		# cls.function_dict[function_name].var_quantities[var_obj.type] += 1
		return cls.function_dict[function_name].add_var(var_obj)

	@classmethod
	def verify_var_in_func(cls, function_name, var_name):
		return cls.function_dict[function_name].var_in_func(var_name) or cls.verify_var_global(var_name)

	@classmethod
	def verify_if_arr(cls, function_name, var_name):
		return cls.function_dict[function_name].is_arr(var_name)

	@classmethod
	def add_param_to_func(cls, function_name, param_name, param_var):
		cls.function_dict[function_name].params.append((param_name, param_var.type, param_var.id))

	@classmethod
	def verify_var_global(cls, var_name):
		return cls.function_dict["program"].var_in_func(var_name)

	@classmethod
	def get_var_in_scope(cls, p, function_name, var_name):
		if not cls.verify_var_in_func(function_name, var_name):
			Error.variable_not_defined(var_name, p.lexer.lineno)
		try:
			var = cls.function_dict[function_name].vars[var_name]
		except KeyError:
			var = cls.function_dict["program"].vars[var_name]
		return var

	@classmethod
	def verify_param_at_index(cls, function_name, param_name, param_type, index):
		func = cls.function_dict[function_name]
		if index >= len(func.params):
			return False
		param_tuple = func.params[index]
		return (param_tuple[0] == param_name and param_tuple[1] == param_type)

	@classmethod
	def add_arr_to_func(cls, function_name, arr_obj):
		return cls.function_dict[function_name].add_arr(arr_obj)

	# @classmethod
	# def add_arr_complete_to_func(cls, function_name, arr_obj):
	# 	cls.function_dict[function_name].add_arr_complete(arr_obj)

	@classmethod
	def function_returns_void(cls, function_name):
		return cls.function_dict[function_name].function_is_void()

	@classmethod
	def set_return_found(cls, function_name, type):
		cls.function_dict[function_name].set_has_Return(type)

	@classmethod
	def function_has_return_stmt(cls, function_name):
		return cls.function_dict[function_name].get_has_Return()

	@classmethod
	def flipped_constant_dict(cls):
		return {v: k for k, v in cls.constant_dict.items()}


class SemanticCube(object):
	# Declaring the 3D matrix with dimensions
	n = len(type_dict)
	ops = len(operator_dict)

	# Every square starts in -1, which is an 'ERROR' return value
	cube = [[[-1 for j in xrange(n)] for i in xrange(n)] for k in xrange(ops)]

	__shared_state = {}
	def __init__(cls):
		cls.__dict__ = cls.__shared_state

	@classmethod
	def set_return_value_for(cls, type1, op_or_list, type2, value):
		i = type_dict[type1]
		j = type_dict[type2]
		value = type_dict[value]
		if isinstance(op_or_list, list):
			indeces = [operator_dict[x] for x in op_or_list] # cool but no need
			for k in indeces:
				cls.set_cube_value(k, i, j, value)
		else:
			k = operator_dict[op_or_list]
			cls.set_cube_value(k, i, j, value)

	@classmethod
	def set_cube_value(cls, op, t1, t2, v):
		cls.cube[op][t1][t2] = v
		cls.cube[op][t2][t1] = v

	@classmethod
	def print_cube(cls):
		pp.pprint(cls.cube)

class SemanticInfo:
	#void, boolean, int, decimal, string,, point, line, triangle, square, rectangle, polygon, star, circle
	current_var_id = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
	current_global_var_id = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
	current_const_id = 14000

	__shared_state = {}
	def __init__(cls):
		cls.__dict__ = cls.__shared_state

	@classmethod
	def get_next_var_id(cls, type):
		cls.current_var_id[type] += 1
		print "> Asking for a new var id -> {}".format(cls.current_var_id[type] - 1)
		return cls.current_var_id[type] - 1

	@classmethod
	def get_next_global_var_id(cls, type):
		cls.current_global_var_id[type] += 1
		return -1 * (cls.current_global_var_id[type] - 1)

	@classmethod
	def get_next_const_id(cls):
		cls.current_const_id += 1
		return cls.current_const_id - 1

	@classmethod
	def reset_var_ids(cls):

		cls.current_var_id = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 
							  9000, 10000, 11000, 12000]

################################################################################
# Filling out the SemanticCube matrix ##########################################
################################################################################

arim_ops = ['+', '-', '*', '/']
comp_ops = ['<', '>', '<=', '>=', '==', '!=']
cond_ops = ['and', 'or']
num_types = ['int', 'decimal']
prim_types = num_types + ['boolean']

for type in num_types:
	# Setting the matrix diagonals
	SemanticCube.set_return_value_for(type, arim_ops, type, type)
	# int with anything always returns that anything
	SemanticCube.set_return_value_for('int', arim_ops, type, type)
	# decimal with anything always returns decimal
	SemanticCube.set_return_value_for('decimal', arim_ops, type, 'decimal')

	for type2 in num_types:
		# every numerical conditional comparison returns a boolean value
		SemanticCube.set_return_value_for(type, comp_ops, type2, 'boolean')

SemanticCube.set_return_value_for('string', '+', 'string', 'string')
SemanticCube.set_return_value_for('boolean', cond_ops, 'boolean', 'boolean')
