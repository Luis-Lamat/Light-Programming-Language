from memory_handler import *
from light_datastructures import *
from quadruple import *

def execute_operator(argument, quad, index):
	switcher = {
		0	: 	plus,
		1	: 	minus,
		2	: 	times,
		3	:	over,
		4	:	lessThan,
		5	:	greaterThan,
		6	:	lessEqThan,
		7	: 	greaterEqThan,
		8	:	equals,
		9	:	notEqual,
		10	:	_and,
		11	:	_or,
		14	:	equal,
		15	:	gotof,
		16	:	gotot,
		17	:	goto,
		18	:	ret,
		19	:	_return,
		20	:	gosub,
		21	:	era,
		22	:	param,
		23	:	_print,
		24	:	end,	

	}
	# Get the function from switcher dictionary
	func = switcher.get(argument, lambda: "nothing")
	# Execute the function
	return func(quad, index)

def plus(quad, index):
	MemoryHandler.binary_operator(quad)

def minus(quad, index):
	MemoryHandler.binary_operator(quad)

def times(quad, index):
	MemoryHandler.binary_operator(quad)

def over(quad, index):
	MemoryHandler.binary_operator(quad)

def lessThan(quad, index):
	MemoryHandler.binary_operator(quad)

def greaterThan(quad, index):
	MemoryHandler.binary_operator(quad)

def lessEqThan(quad, index):
	MemoryHandler.binary_operator(quad)

def greaterEqThan(quad, index):
	MemoryHandler.binary_operator(quad)

def equals(quad, index):
	MemoryHandler.binary_operator(quad)

def notEqual(quad, index):
	MemoryHandler.binary_operator(quad)

def _and(quad, index):
	MemoryHandler.and_or_operator(quad)

def _or(quad, index):
	MemoryHandler.and_or_operator(quad)

def equal(quad, index):
	MemoryHandler.assign_operator(quad)

def gotof(quad, index):
	index = MemoryHandler.gotof(quad)
	return index

def gotot(quad, index):
	index = MemoryHandler.gotot(quad)
	return index

def goto(quad, index):
	index = MemoryHandler.goto(quad)
	return index

def ret(quad, index):
	pass

def _return(quad, index):
	pass

def gosub(quad, index):
	index = MemoryHandler.gosub(quad)
	return index

def era(quad, index):
	MemoryHandler.era_operator(quad)
	pass 

def param(quad, index):
	pass

def _print(quad, index):
	pass

def end(quad, index):
	pass


def RUN_AT_LIGHTSPEED():
	MemoryHandler.init_class_vars() # Supah weird hack...
	quads = Quadruples.quad_list
	print "\nVIRTUAL MACHINE ==============================="
	QuadIterator(0, quads)

def QuadIterator(index, quads):

	while(index < len(quads)):
		op = quads[index].operator
		print("\n> EXECUTION LINE: {}, Quad: {}".format(index, quads[index].get_list()))
		new_index = execute_operator(op, quads[index], index)
		index = new_index if new_index else (index + 1)
