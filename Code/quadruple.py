from light_datastructures import *

class Quadruple(object):
	def __init__(self):
		self.id = -1 # auto_incremented
		self.operator = None
		self.left_operand = None
		self.right_operand = None
		self.result = None

	def build(self, operator, left_operand, right_operand, result):
		self.operator = operator
		self.left_operand = left_operand
		self.right_operand = right_operand
		self.result = result

	def get_list(self):
		return [self.operator, self.left_operand, self.right_operand, self.result]

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
		cls.quad_list.append(quad)
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

	@classmethod
	def print_all(cls):
		print("Quads ===============================")
		print([x.get_list() for x in cls.quad_list])
		pass