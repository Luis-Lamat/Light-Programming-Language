from light_datastructures import *
from light_semantic_controller import *
from memory import *
import operator




class MemoryHandler(object):
	"""MemoryHandler class"""

	# Global and local memory declarations
	global_size = len(FunctionTable.function_dict['program'].vars)

	heap  = Memory() # Global Memory
	stack = Stack()  # Local Memory, stores Memory objects

	__shared_state = {}
	def __init__(cls):
		cls.__dict__ = cls.__shared_state

	def arithmetic_operator(cls, quad, index):
		left_op = cls.get_address_value(quad.left_operand)
		right_op = cls.get_address_value(quad.right_operand)
		result = execute_arithmetic_operator(quad.operator, left_op, right_op)
		cls.set_address_value(quad.result, result)

	def execute_arithmetic_operator(cls, val, x, y):
		ops = {

			0	: operator.add(x,y),
			1	: operator.sub(x,y),
			2	: operator.mul(x,y),
			3	: operator.div(x,y)
		}
		return ops[val]

	def assign_operator(cls, quad, index):
		from_value = cls.get_address_value(quad.left_operand)
		cls.set_address_value(quad.result, from_value)



