from light_datastructures import *
import sys

class Quadruple(object):
	"""Quadruple class
	
	Quadrupe
	"""
	def __init__(self):
		self.id = -1 # auto_incremented
		self.operator = None
		self.left_operand = None
		self.right_operand = None
		self.result = None

	def build(self, operator, left_operand, right_operand, result):
		"""Build quadruple
		
		Build quadruple
		
		Arguments:
			operator {int} -- operator
			left_operand {operand} -- left operand
			right_operand {operand} -- right operand
			result {operand} -- result operand
		"""
		self.operator = operator
		self.left_operand = left_operand
		self.right_operand = right_operand
		self.result = result

	def get_list(self):
		"""Get list
		
		Get Quadruple list
		"""
		op = inv_op_dict[self.operator]
		return [op, self.left_operand, self.right_operand, self.result]

class Quadruples(object):
	"""Quadruples class
	
	Quadruple class manager
	"""
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
		"""Push quadruple
		
		Push quadruple to quadruple list
		
		Arguments:
			quad {Quadruple} -- Quadruple
		"""
		quad.id = cls.next_free_quad
		cls.quad_list.append(quad)
		cls.next_free_quad = len(cls.quad_list)

	@classmethod
	def pop_quad(cls):
		"""Pop quadruple
		
		Pop quadruple from quadruple list
		
		Returns:
			Quadruple -- Quadruple
		"""
		cls.next_free_quad = len(cls.quad_list) - 1
		return cls.quad_list.pop()

	@classmethod
	def fill_missing_quad(cls, quad_id, value):
		"""fill missing quad
		
		Fill missing quadruple with value
		
		Arguments:
			quad_id {int} -- quadruple id
			value {value} -- any primitive
		"""
		cls.quad_list[quad_id].result = value

	# Jump Stack Methods
	@classmethod
	def push_jump(cls, offset):
		"""Push jump
		
		Pushes the id of next free quad plus offset to the jump stack
		
		Arguments:
			offset {int} -- number
		"""
		cls.jump_stack.push(cls.next_free_quad + offset)

	@classmethod
	def pop_jump(cls):
		"""Pop jump
		
		Pop the id of quadruple from jump stack
		
		Returns:
			int -- number
		"""
		return cls.jump_stack.pop()
		
	@classmethod
	def peek_jump(cls):
		"""Peek jump
		
		Peeks the id of jump quadruple
		
		Returns:
			int -- number
		"""
		return cls.jump_stack.peek()

	@classmethod
	def print_jump_stack(cls):
		"""print jump stack
		
		Prints the jump stack
		"""
		cls.jump_stack.pprint()

	@classmethod
	def print_all(cls):
		"""prints all quadruples from list """
		count = 0
		print("Quads ===============================")
		l = [x.get_list() for x in cls.quad_list]
		for e in l:
			sys.stdout.write(str(count) + ":\t")
			for se in e:
				if not se == None:
					sys.stdout.write(str(se))
				sys.stdout.write("\t")
			count += 1
			print ""
		pass