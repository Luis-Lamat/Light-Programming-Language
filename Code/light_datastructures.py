
# INITIALIZE DICTIONARIES
type_dict = {
	# Primitive Types
	'void'	  	: 0,
	'boolean'   : 1,
	'int'	   	: 2,
	'decimal'   : 3,
	'string'	: 4,

	# Figure types
	'point'	 	: 5,
	'line'	  	: 6,
	'triangle'  : 7,
	'square'	: 8,
	'rectangle' : 9,
	'polygon'   : 10,
	'star'	  	: 11,
	'circle'	: 12 
}
inv_type_dict = {v: k for k, v in type_dict.items()}

# WARNING: each time you add an op below, you create a 13x13 matrix of '-1'
operator_dict = {
	'+'  : 0,
	'-'  : 1,
	'*'  : 2,
	'/'  : 3,
	'<'  : 4,
	'>'  : 5,
	'<=' : 6,
	'>=' : 7,
	'==' : 8,
	'!=' : 9,
	'and': 10,
	'or' : 11,
	'mod': 12,
}
special_operator_dict = {
	'('	 	: 13,
	')'	 	: 14,
	'='	 	: 15,
	'gotof'	: 16,
	'gotot'	: 17,
	'goto'	: 18,
	'ret'   : 19,
	'return': 20,
	'gosub' : 21,
	'era'   : 22,
	'param' : 23,
	'print' : 24,
	'end'   : 25,
	'alloc'	: 26,
	'eqarr'	: 27,
	'newfig': 28,
	'addv'	: 29,
	'addc'	: 30,
	'adds'  : 31,
	'wsize' : 32,
	'cam'	: 33,
	'move'	: 34,
	'rst'	: 35,
	'wait'	: 36,
	'bgc'	: 37,
	'mvs'	: 38,
	'hide'	: 39,
	'show'	: 40,
	'txtc'	: 41,
	'printg': 42,
	'winame': 43,
	'length': 44,
	'sin'	: 45,
	'cos'	: 46,
	'tan'	: 47,
	'exp'	: 48,
	'log10'	: 49,
	'sqrt'	: 50,
	'pow'	: 51

}

merged_dict = dict(operator_dict, **special_operator_dict)
inv_op_dict = {v: k for k, v in merged_dict.items()}

initializer_dict = {
	# Primitive Types
	0   :   "",		 #void
	1   :   False,	  #boolean
	2   :   0,		  #int
	3   :   0.0,		#decimal
	4   :   "",		 #string
	5   :   "",		 #decimal, missing probably a fraction class

	#figure types, missing class 
	6   :   "",		 #point
	7   :   "",		 #line
	8   :   "",		 #triangle
	9   :   "",		 #square
	10  :   "",		 #rectangle
	11  :   "",		 #polygon
	12  :   "",		 #star
	13  :   "",		 #circle
}

# Helper Classes

class Stack(object):
	"""Stack Class
	
	Stack class, using a list simulates a stack
	"""
	def __init__(self):
		self.values = []
	def isEmpty(self):
		return self.values == []
	def push(self,  value):
		self.values.append(value)
	def pop(self):
		if(len(self.values) > 0):
			return self.values.pop()
		else :
			print("Empty Stack")
	def peek(self):
		if(len(self.values) == 0):
			return None
		else:
			return self.values[len(self.values)-1]
	def size(self):
		return len(self.values)
	def pprint(self):
		print self.values
	def inStack(self, var_name):
		return var_name in self.values


class Queue(object):
	"""Queue Class
	
	Queue class, using a list simulates a queue
	"""

	def __init__(self):
		self.values = []
	def isEmpty(self):
		return self.values == []
	def enqueue(self, value):
		self.values.insert(0,value)
	def dequeue(self):
		if(len(self.values) > 0):
			return self.values.pop()
		else :
			print("Empty Queue")
	def peek(self):
		return self.values[len(self.values)-1]
	def size(self):
		return len(self.values)
	def pprint(self):
		print self.values
	def inQueue(self, var_name):
		return var_name in self.values
