from light_datastructures import *
from light_semantic_controller import *
from memory import *
import operator




class MemoryHandler(object):
	"""MemoryHandler class"""

	# Global and local memory declarations
	global_function = FunctionTable.function_dict['program']
	global_size = len(global_function.vars)

	heap  = Memory(global_size, global_function.var_quantities) # Global Memory
	stack = Stack()  # Local Memory, stores Memory objects

	__shared_state = {}
	def __init__(cls):
		cls.__dict__ = cls.__shared_state

	@classmethod
	def binary_operator(cls, quad, index):
		left_op = cls.get_address_value(quad.left_operand)
		right_op = cls.get_address_value(quad.right_operand)
		result = execute_binary_operator(quad.operator, left_op, right_op)
		cls.set_address_value(quad.result, result)

	@classmethod
	def execute_binary_operator(cls, val, x, y):
		ops = {

			0	: operator.add(x,y),
			1	: operator.sub(x,y),
			2	: operator.mul(x,y),
			3	: operator.div(x,y),
			4	: operator.lt(x,y),
			5	: operator.gt(x,y),
			6	: operator.le(x,y),
			7	: operator.ge(x,y),
			8	: operator.eq(x,y),
			9	: operator.ne(x,y),
		}
		return ops[val]

	@classmethod
	def assign_operator(cls, quad, index):
		from_value = cls.get_address_value(quad.left_operand)
		cls.set_address_value(quad.result, from_value)

	def and_or_operator(cls, quad, index):
		left_op = cls.get_address_value(quad.left_operand)
		right_op = cls.get_address_value(quad.right_operand)
		if quad.operator == 10 :
			cls.set_address_value(quad.result, (left_op and right_op))
		else if quad.operator == 11 :
			cls.set_address_value(quad.result, (left_op or right_op))

	@classmethod
	def get_address_value(cls, addr):
		type = (addr // 1000) # integer division
		relative_address = addr - type
		# use heap for search if addr is negative, else the current local mem
		heap_or_stack = cls.heap if addr < 0 else cls.stack.peek()
		return heap_or_stack.memory[type][abs(relative_address)]

	@classmethod
	def set_address_value(cls, addr, val):
		type = (addr // 1000) # integer division
		relative_address = addr - type
		# use heap for search if addr is negative, else the current local mem
		if addr < 0:
			cls.heap[type][relative_address] = val
		else:
			cls.stack.peek().[type][relative_address] = val



