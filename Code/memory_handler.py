import operator
from light_semantic_controller import *
from memory import *
from error import *
from figures import *
import time
import ast
import math

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

		if val == 0:
			return operator.add(x,y)
		elif val == 1:
			return operator.sub(x,y)
		elif val == 2:
			return operator.mul(x,y)
		elif val == 3:
			return operator.div(x,y)
		elif val == 4:
			return operator.lt(x,y)
		elif val == 5:
			return operator.gt(x,y)
		elif val == 6:
			return operator.le(x,y)
		elif val == 7:
			return operator.ge(x,y)
		elif val == 8:
			return operator.eq(x,y)
		elif val == 9:
			return operator.ne(x,y)
		elif val == 12:
			return operator.mod(x,y)

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
		print "  Called get_address_value({})".format(addr)
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
		else:
			print "> Stack memory: {}".format(cls.stack.peek().memory)
			return cls.stack.peek().memory[type][relative_address]

	@classmethod
	def set_address_value(cls, addr, val):
		print "  Called set_address_value({}, {})".format(addr, val)
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

		###HELP: faltaba el else???
		else:
			cls.stack.peek().memory[type][relative_address] = val
			print "> Stack memory: {}".format(cls.stack.peek().memory)

	@classmethod
	def set_arr_value(cls, addr, sub_addr, val):
		sub_index = cls.get_address_value(sub_addr)
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Rel = {} - {}".format(abs(addr), (type * 1000))
		print "> Set ARR mem value: type = {}, rel = {}, sub = {},  val = {}".format(type, relative_address, sub_index, val)
		try:
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
		except TypeError:
			Error.not_type_array()

	@classmethod
	def get_array_value(cls, quad):
		addr = quad.left_operand
		sub_index = cls.get_address_value(quad.right_operand)
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		print "> Rel = {} - {}".format(abs(addr), (type * 1000))
		print "> Get ARR mem value: type = {}, rel = {}, sub = {},  set_to = {}".format(type, relative_address, sub_index, quad.result)

		try:
			if addr < 0:
				if len(cls.heap.memory[type][abs(relative_address)]) > sub_index and sub_index >= 0 :
					val = cls.heap.memory[type][abs(relative_address)][sub_index]
				else:
					print "> Error on Heap memory: {}".format(cls.heap.memory)				
					Error.out_of_bounds(len(cls.heap.memory[type][abs(relative_address)]), sub_index)
			else:
				if len(cls.stack.peek().memory[type][relative_address]) > sub_index and sub_index >= 0 :
					val = cls.stack.peek().memory[type][relative_address][sub_index]
				else:
					Error.out_of_bounds(len(cls.stack.peek().memory[type][relative_address]), sub_index)
		except TypeError:
			Error.type_array()

		cls.set_address_value(quad.result, val)
		

	@classmethod
	def get_array_length(cls, quad):
		addr = quad.left_operand
		type = abs(addr) // 1000 # integer division
		relative_address = abs(addr) - (type * 1000)
		
		if addr < 0:
			val = len(cls.heap.memory[type][abs(relative_address)]) 
			
		else:
		 	val = len(cls.stack.peek().memory[type][relative_address])
					
		cls.set_address_value(quad.result, val)

	@classmethod
	def do_math(cls, quad, type):
		data = cls.get_address_value(quad.left_operand)
		val = 0.0
		if(type == "sin"):
			val = math.sin(data)
		elif(type == "cos"):
			val = math.cos(data)
		elif(type == "tan"):
			val = math.tan(data)
		elif(type == "exp"):
			val = math.exp(data)
		elif(type == "log10"):
			val = math.log10(data)
		elif(type == "sqrt"):
			val = math.sqrt(data)

		cls.set_address_value(quad.result, val)

	@classmethod
	def do_math_double(cls, quad, type):
		data1 = cls.get_address_value(quad.left_operand)
		data2 = cls.get_address_value(quad.right_operand)
		val = 0.0
		if(type == "pow"):
			val = math.pow(data1, data2)

		cls.set_address_value(quad.result, val)

	@classmethod
	def wait(cls, quad):
		wait_time = cls.get_address_value(quad.result)
		time.sleep(wait_time/1000.0)

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
		obj_temp.setNextVertex(x, y)
		# if not obj_temp.setNextVertex(x, y):
		# 	type = abs(quad.result) // 1000
		# 	Error.wrong_vertex_number(type)

	@classmethod
	def move_fig(cls, quad, obj_temp):
		x = cls.get_address_value(quad.left_operand)
		y = cls.get_address_value(quad.right_operand)
		obj_temp.move(x, y)

	@classmethod
	def set_move_speed(cls, quad):

		speed = cls.get_address_value(quad.result)
		return speed/1000.0

	@classmethod
	def get_window_name(cls, quad):
		return ast.literal_eval(str(cls.get_address_value(quad.result)))

	@classmethod
	def throwColorError(type, r,g,b):
		if not (r >= 0): 
			Error.wrong_color_number(type, r)
		elif not (g >= 0):
			Error.wrong_color_number(type, g)
		else:
			Error.wrong_color_number(type, b)

	@classmethod
	def get_text_color(cls, quad):

		r = cls.get_address_value(quad.left_operand)
		g = cls.get_address_value(quad.right_operand)
		b = cls.get_address_value(quad.result)

		if r >= 0 and g >= 0 and b >= 0:
			return [r,g,b]
		else:
			cls.throwColorError("text", r,g,b)

	@classmethod
	def set_background_color(cls, quad):

		r = cls.get_address_value(quad.left_operand)
		g = cls.get_address_value(quad.right_operand)
		b = cls.get_address_value(quad.result)

		if r >= 0 and g >= 0 and b >= 0:
			return [r,g,b]
		else:
			cls.throwColorError("background",r,g,b)

	@classmethod
	def add_color_fig(cls, quad, obj_temp):

		type = quad.left_operand
		color = cls.get_address_value(quad.right_operand)

		if not obj_temp.setTypeColor(type, color):
			Error.wrong_color_number("figure", color)


	@classmethod
	def get_text(cls, quad):
		text = ast.literal_eval(str(cls.get_address_value(quad.result)))
		x = cls.get_address_value(quad.left_operand)
		y = cls.get_address_value(quad.right_operand)
		return [x, y, text]

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
			