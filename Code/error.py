import sys
from light_datastructures import *

class Error:
	@staticmethod
	def already_defined(type, name):
		print "Semantic Error: {} '{}' already defined".format(type, name)
		sys.exit()

	@staticmethod #TODO: Dafuq we need this for
	def out_of_bounds(name, num):
		print "Out Of Bounds Error: Array '{}' out of bounds at index: {}".format(name, num)
		sys.exit()

	@staticmethod
	def type_mismatch(lineno, t1, t2, op):
		t1 = inv_type_dict[t1]
		t2 = inv_type_dict[t2]
		print "Type Mismatch (line {}): expresion '{} {} {}' is invalid".format(lineno-2, t1, op, t2)
		sys.exit()