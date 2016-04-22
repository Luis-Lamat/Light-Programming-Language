import operator
from light_semantic_controller import *
from memory import *

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
		return quad.result if left_op == "false" else index + 1

	@classmethod
	def gotot(cls, quad, index):
		left_op = cls.get_address_value(quad.left_operand)
		print "> GoTo True with **{}** to {}".format(left_op, index+1)
		# return +1 to continue with next quadruple
		return quad.result if left_op == "true" else index + 1

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
		return mem.return_address

	@classmethod
	def assign_operator(cls, quad):
		from_value = cls.get_address_value(quad.left_operand)
		cls.set_address_value(quad.result, from_value)

	@classmethod
	def and_or_operator(cls, quad):
		left_op = cls.get_address_value(quad.left_operand)
		right_op = cls.get_address_value(quad.right_operand)
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
		type = abs(addr // 1000) # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Get mem value: type = {}, addr = {}".format(type, abs(relative_address))
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
		type = abs(addr // 1000) # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Set mem value: type = {}, addr = {}, val = {}".format(type, abs(relative_address), val)
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
	