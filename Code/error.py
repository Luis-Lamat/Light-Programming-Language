import sys
from light_datastructures import *

class Error:
	""" Error class
	
		Static class used throughout the application to display certain errors in
		a standirdized format.
	"""

	@staticmethod
	def already_defined(type, name):
		""" already defined error"""
		print "Semantic Error: {} '{}' already defined".format(type, name)
		sys.exit()

	@staticmethod
	def out_of_bounds(size, num):
		""" out of bounds error """
		print "Array Index Out Of Bounds Error: Array of size: '{}' out of bounds at index: {}".format(size, num)
		sys.exit()

	@staticmethod
	def type_mismatch(lineno, t1, t2, op):
		"""type mismathc error """
		t1 = inv_type_dict[t1]
		t2 = inv_type_dict[t2]
		print "Type Mismatch (line {}): expresion '{} {} {}' is invalid".format(lineno-2, t2, op, t1)
		sys.exit()

	@staticmethod
	def param_mismatch(lineno, p, t):
		"""parameter mismatch error"""
		t = inv_type_dict[t]
		print "Parameter Mismatch (line {}): param '{}' is not valid or can't be of type '{}'".format(lineno, p, t)
		sys.exit()

	@staticmethod
	def param_number_mismatch(lineno, f, n, m):
		""" paramenter number mismatch error"""
		print "Parameter Mismatch (line {}): function '{}' takes {} arguments, {} given".format(lineno, f, n, m)
		sys.exit()

	@staticmethod
	def variable_not_defined(name, line):
		""" variable not defined error"""
		print "Semantic Error (line {}): Variable '{}' not defined".format(line, name)
		sys.exit()

	@staticmethod
	def variable_already_defined(name, line):
		"""variable alreadt refined error """
		print "Semantic Error (line {}): Variable '{}' already defined".format(line, name)
		sys.exit()

	@staticmethod
	def function_not_defined(name, line):
		""" function not defined error """
		print "Semantic Error: Function '" + name +"' not defined in line: " + str(line)
		sys.exit()

	@staticmethod
	def return_type_function_void(name, line):
		""" return type is invalid function is void """
		print "Semantic Error: Function '" + name +"' is void, return invalid, in line:  " + str(line)
		sys.exit()

	@staticmethod
	def no_return_type(name, line):
		""" function do not have a return type """
		print "Semantic Error: Function '" + name +"' do not have a return, in line " + str(line)
		sys.exit()

	@staticmethod
	def condit(txt, line):
		""" Condition init error """
		print "Semantic Error: " + txt + ", in line " + str(line)
		sys.exit()

	@staticmethod
	def not_a_condition(t1, lineno):
		""" not a condition error """
		t1 = inv_type_dict[t1]
		print "Semantic Error: Expected type Bool and got type " + str(t1) + ", in line " + str(lineno)
		sys.exit()

	@staticmethod
	def wrong_type(cntxt, t1, t2, lineno):
		""" wrong type error """
		t1 = inv_type_dict[t1]
		t2 = inv_type_dict[t2]
		print "Semantic Error (line {}): '{}' cannot be of type '{}', must be of type '{}'".format(lineno, cntxt, t1, t2)
		sys.exit()

	@staticmethod
	def wrong_attribute_for_figure(fig_t, attr, lineno):
		""" wrong attribute type for figure error """
		fig_t = inv_type_dict[fig_t]
		print "Semantic Error (line {}): The figure type '{}' does not accept the attribute '{}'".format(lineno, fig_t, attr)
		sys.exit()

	@staticmethod
	def wrong_size_initialization( lineno):
		""" wrong size initialization error """
		print "Semantic Error (line {}): Array initialization error, arguments should be equal to the length'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_window_declaration(lineno):
		""" wrong window declaration error """
		print "Syntax Error (line {}): The correct syntax for window size is 'window_size (width: <int>, height: <int>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_move_declaration(lineno):
		""" wrong move declaration error """
		print "Syntax Error (line {}): The correct syntax for move is 'move <figure_name> (x: <exp>, y: <exp>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_wait_declaration(lineno):
		""" wrong wait declaration error """
		print "Syntax Error (line {}): The correct syntax for wait is 'wait (ms: <exp>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_figure_color_declaration(lineno):
		""" wrong figure color declaration error """
		print "Syntax Error (line {}): The correct syntax for figure attribute color is 'color : (r: <exp>, g: <exp>, b: <exp>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_figure_vertex_declaration(lineno):
		""" wrong figure vertex declaration error """
		print "Syntax Error (line {}): The correct syntax for figure attribute vertex is 'v : (x: <exp>, y: <exp>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_move_speed_declaration(lineno):
		""" wrong move speed declaration error """
		print "Syntax Error (line {}): The correct syntax for move speed is 'move_speed (ms: <exp>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_bgc_declaration(lineno):
		""" wrong background color declaration error """
		print "Syntax Error (line {}): The correct syntax for background color is 'background_color (r: <exp>, g: <exp>, b: <exp>)'".format(lineno)
		sys.exit()
  
	@staticmethod
	def wrong_name_window(lineno):
		""" wrong window name error """
		print "Syntax Error (line {}): The correct syntax for window name 'window_name (name: <string>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_txtc_declaration(lineno):
		""" wrong text color declaration error"""
		print "Syntax Error (line {}): The correct syntax for text color is 'text_color (r: <exp>, g: <exp>, b: <exp>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_printg_declaration(lineno):
		""" wrong Graphical print declaration error """
		print "Syntax Error (line {}): The correct syntax for printg is 'printg (text: <string exp>, x: <exp>, y: <exp>)'".format(lineno)
		sys.exit()

	@staticmethod
	def wrong_vertex_number(fig_t):
		""" Wrong vertex number error"""
		fig_t = inv_type_dict[fig_t]
		print "RunTime Error: Wrong number of Vertices for figure type '{}'".format(fig_t)
		sys.exit()

	@staticmethod
	def wrong_color_number(color, data):
		""" wrong color number error """
		print "RunTime Error: Wrong color number in {}, shuld be in range (0...255) and is '{}'".format(data, color)
		sys.exit()

	@staticmethod
	def window_not_defined():
		""" window not defined error """
		print "RunTime Error: Window_size not defined"
		sys.exit()

	@staticmethod
	def not_type_array():
		""" not type array error """
		print "RunTime Error: Variable is not of type Array"
		sys.exit()

	@staticmethod
	def type_array():
		""" type array error """
		print "RunTime Error: Variable is of type Array"
		sys.exit()

	@staticmethod
	def figure_not_in_camera():
		""" figure not in camera error """
		print "RunTime Error: Figure not in camera"
		sys.exit()

	@staticmethod
	def wrong_attribute_for_figure_execution(fig_t, attr):
		""" Wrong attribute for figure execution error """
		fig_t = inv_type_dict[fig_t]
		print "Semantic Error: The figure type '{}' does not accept the attribute '{}'".format( fig_t, attr)
		sys.exit()

