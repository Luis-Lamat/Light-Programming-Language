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


		