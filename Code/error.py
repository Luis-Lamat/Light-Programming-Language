import sys
from light_datastructures import *

class Error:
	@staticmethod
	def already_defined(type, name):
		print "Semantic Error: {} '{}' already defined".format(type, name)
		sys.exit()

	@staticmethod
	def out_of_bounds(size, num):
		print "Array Index Out Of Bounds Error: Array of size: '{}' out of bounds at index: {}".format(size, num)
		sys.exit()

	@staticmethod
	def type_mismatch(lineno, t1, t2, op):
		t1 = inv_type_dict[t1]
		t2 = inv_type_dict[t2]
		print "Type Mismatch (line {}): expresion '{} {} {}' is invalid".format(lineno-2, t2, op, t1)
		sys.exit()

	@staticmethod
	def param_mismatch(lineno, p, t):
		t = inv_type_dict[t]
		print "Parameter Mismatch (line {}): param '{}' is not valid or can't be of type '{}'".format(lineno, p, t)
		sys.exit()

	@staticmethod
	def param_number_mismatch(lineno, f, n, m):
		print "Parameter Mismatch (line {}): function '{}' takes {} arguments, {} given".format(lineno, f, n, m)
		sys.exit()

	@staticmethod
	def variable_not_defined(name, line):
		print "Semantic Error (line {}): Variable '{}' not defined".format(line, name)
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

	@staticmethod
	def wrong_type(cntxt, t1, t2, lineno):
		t1 = inv_type_dict[t1]
		t2 = inv_type_dict[t2]
		print "Semantic Error (line {}): '{}' cannot be of type '{}', must be of type '{}'".format(lineno, cntxt, t1, t2)
		sys.exit()

	@staticmethod
	def wrong_attribute_for_figure(fig_t, attr, lineno):
		fig_t = inv_type_dict[fig_t]
		print "Semantic Error (line {}): The figure type '{}' does not accept the attribute '{}'".format(lineno, fig_t, attr)
		sys.exit()

	@staticmethod
	def wrong_window_declaration(lineno):
		print "Syntax Error (line {}): The correct syntax for window size is 'window_size(width: <int>, height: <int>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_vertex_number(fig_t):
		fig_t = inv_type_dict[fig_t]
		print "RunTime Error: Wrong number of Vertices for figure type '{}'".format(fig_t)
		sys.exit()

