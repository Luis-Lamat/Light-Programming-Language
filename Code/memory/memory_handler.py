from light_datastructures import *
from light_semantic_controller import *
from memory import *

class MemoryHandler(object):
	"""MemoryHandler class"""

	# Global and local memory declarations
	global_size = len(FunctionTable.function_dict['program'].vars)

	heap = Memory()

	__shared_state = {}
	def __init__(cls):
		cls.__dict__ = cls.__shared_state


		