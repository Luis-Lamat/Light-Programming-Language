import operator
from light_semantic_controller import *
from memory import *
from error import *
from figures import *

class MemoryHandler:
	# Global and local memory declarations
	global_size = None

	# Global Memory
	const_vars = None
	heap = None

	# Local Memory, stores Memory objects
	stack = Stack()
	mem_to_push = None

	__shared_state = {}
	def __init__(cls):
		cls.__dict__ = cls.__shared_state

	@classmethod
	def init_class_vars(cls):
		cls.const_vars = FunctionTable.flipped_constant_dict()
		print "-----> HEAP VAR Q's: {}".format(FunctionTable.function_dict['program'].var_quantities)
		cls.heap = Memory(len(type_dict), FunctionTable.function_dict['program'].var_quantities)
		cls.stack = Stack()
		cls.mem_to_push = None

	@classmethod
	def binary_operator(cls, quad):
		left_op = cls.get_address_value(quad.left_operand)
		right_op = cls.get_address_value(quad.right_operand)
		result = cls.execute_binary_operator(quad.operator, left_op, right_op)
		cls.set_address_value(quad.result, result)

	@classmethod
	def division(cls, quad):
		left_op = cls.get_address_value(quad.left_operand)
		right_op = cls.get_address_value(quad.right_operand)
		result = operator.div(left_op, right_op)
		cls.set_address_value(quad.result, result)

	@classmethod
	def execute_binary_operator(cls, val, x, y):
		ops = {
			0	: operator.add(x,y),
			1	: operator.sub(x,y),
			2	: operator.mul(x,y),
		# 	3	: operator.div(x,y),
			4	: operator.lt(x,y),
			5	: operator.gt(x,y),
			6	: operator.le(x,y),
			7	: operator.ge(x,y),
			8	: operator.eq(x,y),
			9	: operator.ne(x,y)
		}
		return ops[val]

	@classmethod
	def gosub(cls, quad, return_index):
		print "> Pushing memory to stack: {}".format(cls.mem_to_push.memory)
		print "> Returning addr for quad: {}".format(return_index)
		cls.mem_to_push.return_address = return_index + 1
		cls.stack.push(cls.mem_to_push)
		return quad.result

	@classmethod
	def gotof(cls, quad, index):
		left_op = cls.get_address_value(quad.left_operand)
		print "> GoTo False with **{}** to {}".format(left_op, index+1)
		# return +1 to continue with next quadruple
		return quad.result if left_op == "false" or left_op == False else index + 1

	@classmethod
	def gotot(cls, quad, index):
		left_op = cls.get_address_value(quad.left_operand)
		print "> GoTo True with **{}** to {}".format(left_op, index+1)
		# return +1 to continue with next quadruple
		return quad.result if left_op == "true" or left_op == True else index + 1

	@classmethod
	def goto(cls, quad):
		return quad.result

	@classmethod
	def _print(cls, quad):
		print("\nLIGHT OUTPUT:\n<<<<{}>>>>".format(cls.get_address_value(quad.result)))
		print("END")

	@classmethod
	def ret_operator(cls):
		mem = cls.stack.pop()
		print "> Returning to quad index: {}".format(mem.return_address)
		print "> Returning memory = {}".format(mem.memory)
		return mem.return_address

	@classmethod
	def return_operator(cls, quad):
		val = cls.get_address_value(quad.left_operand)
		mem = cls.stack.pop()
		cls.set_address_value(quad.result, val)
		print "> Returning to quad index: {}".format(mem.return_address)
		print "> Returning memory = {}".format(cls.stack.peek().memory)
		return mem.return_address

	@classmethod
	def assign_operator(cls, quad):
		value = cls.get_address_value(quad.left_operand)
		if quad.right_operand :
			cls.set_arr_value(quad.result, quad.right_operand, value)
		else:
			cls.set_address_value(quad.result, value)

	@classmethod
	def allocate_array_space(cls, quad):
		from_value = quad.left_operand
		size = quad.right_operand
		empty_list = [None] * int(size)
		cls.set_address_value(from_value, empty_list)
		#HERE

	@classmethod
	def and_or_operator(cls, quad):
		left_op = cls.get_address_value(quad.left_operand)
		right_op = cls.get_address_value(quad.right_operand)
		# TODO: The next set of lines will fail at a specific case
		if quad.operator == 10 :
			cls.set_address_value(quad.result, (left_op and right_op))
		elif quad.operator == 11 :
			cls.set_address_value(quad.result, (left_op or right_op))

	@classmethod
	def era_operator(cls, quad):
		func_name = quad.left_operand
		func = FunctionTable.function_dict[func_name]
		cls.mem_to_push = Memory(len(type_dict), func.var_quantities) 
		print "> Created new memory for '{}': {}".format(func_name, cls.mem_to_push.memory)

	@classmethod # TODO: Refactor if possible
	def param_operator(cls, quad):
		func_name 	 = quad.right_operand
		param_index  = quad.result
		param_tuple  = FunctionTable.function_dict[func_name].params[param_index]
		print "> Param: func = {}, index = {}, tuple = {}".format(func_name, param_index, param_tuple[2])
		new_rel_addr = cls.get_type_and_rel_addr(param_tuple[2])
		val = cls.get_address_value(quad.left_operand)

		print "> Param: val = {} @ {}, to = {}".format(val, quad.left_operand, new_rel_addr)
		cls.mem_to_push.memory[new_rel_addr[0]][new_rel_addr[1]] = val

	@classmethod
	def get_type_and_rel_addr(cls, addr):
		type = abs(addr // 1000) # integer division
		relative_address = abs(addr) - (type * 1000)
		return (type, relative_address)

	@classmethod
	def get_address_value(cls, addr):
		print "> Called get_address_value({})".format(addr)
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Get mem value: type = {}, addr = {}".format(type, relative_address)
		# use heap for search if addr is negative, else the current local mem
		if addr >= 14000:
			print "> Const vars memory: {}".format(cls.const_vars)
			return cls.const_vars[addr]
		elif addr < 0:
			print "> Heap memory: {}".format(cls.heap.memory)
			return cls.heap.memory[type][abs(relative_address)]
		print "> Stack memory: {}".format(cls.stack.peek().memory)
		return cls.stack.peek().memory[type][relative_address]

	@classmethod
	def set_address_value(cls, addr, val):
		print "> Called set_address_value({}, {})".format(addr, val)
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Rel = {} - {}".format(abs(addr), (type * 1000))
		print "> Set mem value: type = {}, addr = {}, val = {}".format(type, relative_address, val)
		# use heap for search if addr is negative, else the current local mem
		if addr >= 14000:
			cls.const_vars[addr] = val
			print "> Const vars memory: {}".format(cls.const_vars)
		elif addr < 0:
			cls.heap.memory[type][abs(relative_address)] = val
			print "> Heap memory: {}".format(cls.heap.memory)
		else:
			cls.stack.peek().memory[type][relative_address] = val
			print "> Stack memory: {}".format(cls.stack.peek().memory)

	@classmethod
	def set_arr_value(cls, addr, sub_addr, val):
		sub_index = cls.get_address_value(sub_addr)
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Rel = {} - {}".format(abs(addr), (type * 1000))
		print "> Set ARR mem value: type = {}, addr[{}] = {},  val = {}".format(type, sub_index, relative_address, val)
		if addr < 0:
			#out_of_bounds(name, num)
			if len(cls.heap.memory[type][abs(relative_address)]) > sub_index and sub_index >= 0 :
				cls.heap.memory[type][abs(relative_address)][sub_index] = val
				print "> Heap memory: {}".format(cls.heap.memory)
			else:
				Error.out_of_bounds(len(cls.heap.memory[type][abs(relative_address)]), sub_index)
		else:
			if len(cls.stack.peek().memory[type][relative_address]) > sub_index and sub_index >= 0 :
				cls.stack.peek().memory[type][relative_address][sub_index] = val
				print "> Stack memory: {}".format(cls.stack.peek().memory)
			else:
				Error.out_of_bounds(len(cls.stack.peek().memory[type][relative_address]), sub_index)

	@classmethod
	def get_array_value(cls, quad):
		addr = quad.left_operand
		sub_index = cls.get_address_value(quad.right_operand)
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Rel = {} - {}".format(abs(addr), (type * 1000))
		print "> Get ARR mem value: type = {}, addr[{}] = {},  val = {}".format(type, sub_index, quad.right_operand, quad.result)

		if addr < 0:
			if len(cls.heap.memory[type][abs(relative_address)]) > sub_index and sub_index >= 0 :
				val = cls.heap.memory[type][abs(relative_address)][sub_index]
			else:
				Error.out_of_bounds(len(cls.heap.memory[type][abs(relative_address)]), sub_index)
		else:
			if len(cls.stack.peek().memory[type][relative_address]) > sub_index and sub_index >= 0 :
				val = cls.stack.peek().memory[type][relative_address][sub_index]
			else:
				Error.out_of_bounds(len(cls.stack.peek().memory[type][relative_address]), sub_index)

		cls.set_address_value(quad.result, val)


	#FIGURES
	@classmethod
	def create_empty_fig(cls, val):
		figs = {
			6	: L_Line(),			#line
			7	: L_Triangle(),		#triangle
			8	: L_Square(),		#square
			9	: L_Rectangle(),	#rectangle
			10	: L_Polygon(),		#polygon
			12	: L_Circle(),		#circle
		}
		return figs[val]

	@classmethod
	def fig_can_add_size(cls, val):
		figs = {
			6	: False,		#line
			7	: False,		#triangle
			8	: True,			#square
			9	: False,		#rectangle
			10	: False,		#polygon
			12	: True,			#circle
		}
		return figs[val]

	@classmethod
	def add_vertex_fig(cls, quad, obj_temp):

		x = cls.get_address_value(quad.left_operand)
		y = cls.get_address_value(quad.right_operand)

		if not obj_temp.setNextVertex(x, y):
			type = abs(quad.result) // 1000
			Error.wrong_vertex_number(type)

	@classmethod
	def add_color_fig(cls, quad, obj_temp):

		type = quad.left_operand
		color = cls.get_address_value(quad.right_operand)

		if not obj_temp.setTypeColor(type, color):
			Error.wrong_color_number(color)

	@classmethod
	def add_size_fig(cls, quad, obj_temp):

		type = abs(quad.result) // 1000 # integer division
		if not cls.fig_can_add_size(type):
			Error.wrong_attribute_for_figure_execution(type, "size")

		size = cls.get_address_value(quad.right_operand)
		obj_temp.setSize(size)


	@classmethod
	def set_new_fig(cls, quad):
		addr = quad.result
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Rel = {} - {}".format(abs(addr), (type * 1000))
		print "> Set New Fig mem value: type = {}, addr = {}".format(type, relative_address)

		new_obj = cls.create_empty_fig(type)

		if addr < 0:
			cls.heap.memory[type][abs(relative_address)] = new_obj
			print "> Heap memory: {}".format(cls.heap.memory)
		else:
			cls.stack.peek().memory[type][relative_address] = new_obj
			print "> Stack memory: {}".format(cls.stack.peek().memory)


	@classmethod
	def set_fig(cls, obj, quad):
		addr = quad.result
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Rel = {} - {}".format(abs(addr), (type * 1000))
		print "> Set New Fig mem value: type = {}, addr = {}".format(type, relative_address)

		if addr < 0:
			cls.heap.memory[type][abs(relative_address)] = obj
			print "> Heap memory: {}".format(cls.heap.memory)
		else:
			cls.stack.peek().memory[type][relative_address] = obj
			print "> Stack memory: {}".format(cls.stack.peek().memory)

	@classmethod
	def get_fig(cls, addr):
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Rel = {} - {}".format(abs(addr), (type * 1000))
		print "> Get Fig mem value: type = {}, addr = {}".format(type, relative_address)

		if addr < 0:
			print "> Heap memory: {}".format(cls.heap.memory)
			return cls.heap.memory[type][abs(relative_address)]
		else:
			print "> Stack memory: {}".format(cls.stack.peek().memory)
			return cls.stack.peek().memory[type][relative_address]
			