from light_datastructures import *
from light_semantic_controller import *
from memory import *

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


		