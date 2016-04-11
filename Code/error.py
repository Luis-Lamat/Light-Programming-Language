import sys
from light_datastructures import *

class Error:
	@staticmethod
	def already_defined(type, name):
		print "Semantic Error: {} '{}' already defined".format(type, name)
		sys.exit()

	@staticmethod #TODO: Dafuq we need this for, #ANSWER: To check if we are accesing a valid array space
	def out_of_bounds(name, num):
		print "Out Of Bounds Error: Array '{}' out of bounds at index: {}".format(name, num)
		sys.exit()

	@staticmethod
	def type_mismatch(lineno, t1, t2, op):
		t1 = inv_type_dict[t1]
		t2 = inv_type_dict[t2]
		print "Type Mismatch (line {}): expresion '{} {} {}' is invalid".format(lineno-2, t1, op, t2)
		sys.exit()

	@staticmethod
	def variable_not_defined(name, line):
		print "Semantic Error: Variable '" + name +"' not defined in line: " + str(line)
		sys.exit()

	@staticmethod
	def function_not_defined(name, line):
		print "Semantic Error: Function '" + name +"' not defined in line: " + str(line)
		sys.exit()

	@staticmethod
	def return_type_function_void(name, line):
		print "Semantic Error: Function '" + name +"' is void, return invalid, in line:  " + str(line)
		sys.exit()

	@staticmethod
	def no_return_type(name, line):
		print "Semantic Error: Function '" + name +"' do not have a return, in line " + str(line)
		sys.exit()

	@staticmethod
	def condit(txt, line):
		print "Semantic Error: " + txt + ", in line " + str(line)
		sys.exit()

	@staticmethod
	def not_a_condition(t1, lineno):
		t1 = inv_type_dict[t1]
		print "Semantic Error: Expected type Bool and got type " + str(t1) + ", in line " + str(lineno)
		sys.exit()

