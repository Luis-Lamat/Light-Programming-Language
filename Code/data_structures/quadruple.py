from light_datastructures import *

class Quadruple(object):
	def __init__(self):
		self.id = -1 # auto_incremented
		self.operator = None
		self.left_operand = None
		self.right_operand = None
		self.result = None

class Quadruples(object):
	# Class variables
	quad_list = []
	jump_stack = Stack()
	next_free_quad = 0
	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state

	# Quad Methods
	@classmethod
	def push_quad(cls, quad):
		cls.quad_list.append(uad)
		next_free_quad = len(cls.quad_list)

	@classmethod
	def fill_missing_quad(cls, quad_id, value):
		cls.quad_list[quad_id].result = value

	# Jump Stack Methods
	@classmethod
	def push_jump(cls, quad_id):
		cls.jump_stack.push(quad_id)

	@classmethod
	def pop_jump(cls):
		return cls.jump_stack.pop()
		
	@classmethod
	def peek_jump(cls):
		return cls.jump_stack.peek()