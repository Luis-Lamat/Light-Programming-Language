
class Memory(object):
	"""Memory class object"""

	# @param size (num): the amount of types it will hold
	# @param sublists_sizes (list(num)): the amount of variables in each type
	def __init__(self, size, sublists_sizes):
		self.return_address = None
		self.memory = [[] for x in xrange(size)]
		for i in xrange(size):
			self.memory[i] = [None for x in xrange(sublists_sizes[i])]
