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
		12	:	lPar,
		13	:	rPar,
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
	pass

def minus(quad, index):
	pass

def times(quad, index):
	pass

def over(quad, index):
	pass

def lessThan(quad, index):
	pass

def greaterThan(quad, index):
	pass

def lessEqThan(quad, index):
	pass

def greaterEqThan(quad, index):
	pass

def equals(quad, index):
	pass

def notEqual(quad, index):
	pass

def _and(quad, index):
	pass

def _or(quad, index):
	pass

def lPar(quad, index):
	pass

def rPar(quad, index):
	pass

def equal(quad, index):
	pass

def gotof(quad, index):
	pass

def gotot(quad, index):
	pass

def goto(quad, index):
	pass

def ret(quad, index):
	pass

def _return(quad, index):
	pass

def gosub(quad, index):
	pass

def era(quad, index):
	pass

def param(quad, index):
	pass

def _print(quad, index):
	pass

def end(quad, index):
	pass


def RUN_AT_LIGHTSPEED():
	quads = Quadruples.quad_list

	for i in xrange(len(quads)):

		op = quads[i].operator
		execute_operator(op, quads[i], i)

