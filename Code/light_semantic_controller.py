#Semantic Controller
from light_datastructures import *
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

# INITIALIZE DICTIONARIES
type_dict = {
	# Primitive Types
	'void'		: 0,
	'boolean'	: 1,
	'int'		: 2,
	'decimal'	: 3,
	'string'	: 4,
	'fraction'	: 5,

	# Figure types
    'point'     : 6,
    'line'      : 7,
    'triangle'  : 8,
    'square'    : 9,
    'rectangle' : 10,
    'polygon'   : 11,
    'star'      : 12,
    'circle'    : 13 
}

operator_dict = {
	'+' 	: 0,
	'-' 	: 1,
	'*' 	: 2,
	'/' 	: 3
}

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
		print "\t\tid: " + str(self.id) + ",\n\t\tname: " + self.name  + ",\n\t\ttype: " + str(self.type)
		print "\t\t---------"



class Function:
	def __init__(self):
		self.id = -1
		self.name = ""
		self.next_var_id = 0
		self.type = ""
		self.vars = {}

	def erase(self):
		self.id = -1
		self.name = ""
		self.next_var_id = 0
		self.type = ""
		self.vars = {}

	def init_func(self, id, name, type):
		self.id = id
		self.name = name
		self.type = type

	def add_var(self, var):
		if var.name not in self.vars:
			tmp_var = Var()
			tmp_var.init_var(self.next_var_id, var.name, var.type, var.value)
			self.vars[var.name] = tmp_var
			self.next_var_id += 1
		else:
			Error.already_defined('variable', var.name)

	def print_all(self):
		#print "Hola"
		print "\tid: " + str(self.id) + ",\n\tname: " + self.name  + ",\n\ttype: " + str(self.type)
		for k in self.vars:
			print "\tVAR - " + k + ":"
			self.vars[k].print_var()


class FunctionTable:
	global_func = Function()
	global_func.init_func(0, 'program', type_dict['void'])
	
	function_dict = {
		'program' : global_func
	}
	next_func_id = 1
	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state

	@classmethod
	def add_function(cls, func):
		if func.name not in cls.function_dict:
			tmp_func = Function()
			tmp_func.init_func(cls.next_func_id, func.name, func.type)
			cls.function_dict[func.name] = tmp_func
			cls.next_func_id += 1
		else:
			Error.already_defined('function', func.name)

	@classmethod
	def add_return_type_to_func(cls, name, type):
		cls.function_dict[name].type = type

	@classmethod
	def print_all(cls):
		for x in cls.function_dict:
			print (x + ":")
			cls.function_dict[x].print_all()

	@classmethod
	def add_var_to_func(cls, function_name, var_obj):
		cls.function_dict[function_name].add_var(var_obj)


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
			indeces = [operator_dict[x] for x in op_or_list]
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
	current_func_id = 0

	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state

	def get_next_func_id():
		current_func_id = current_func_id + 1
		return current_func_id - 1

class Error:
	@staticmethod
	def already_defined(type, name):
		print "Semantic Error: " + type + " '" + name + "' already defined"
		sys.exit()

################################################################################
# Filling out the SemanticCube matrix ##########################################
################################################################################

arim_ops = ['+', '-', '*', '/']
num_types = ['int', 'decimal', 'fraction']

for type in num_types:
	# Setting the matrix diagonals
	SemanticCube.set_return_value_for(type, arim_ops, type, type)
	# int with anything always returns that anything
	SemanticCube.set_return_value_for('int', arim_ops, type, type)
	# decimal with anything always returns decimal
	SemanticCube.set_return_value_for('decimal', arim_ops, type, 'decimal')

SemanticCube.set_return_value_for('string', '+', 'string', 'string')

SemanticCube.print_cube()

