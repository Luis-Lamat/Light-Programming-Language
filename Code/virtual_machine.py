from light_datastructures import *
from quadruple import *


quads = Quadruples.quad_list
iteratorValue = 0

for i in xrange(len(quads)):

	op = quads[i].operator
	iteratorValue = i
	execute_operator(op)


def plus():
    pass

def minus():
	pass

def times():
	pass

def over():
	pass

def lessThan():
	pass

def greaterThan():
	pass

def lessEqThan():
	pass

def greaterEqThan():
	pass

def equals():
	pass

def notEqual():
	pass

def _and():
	pass

def _or():
	pass

def lPar():
	pass

def rPar():
	pass

def equal():
	pass

def gotof():
	pass

def gotof():
	pass

def goto():
	pass

def ret():
	pass

def _return():
	pass

def gosub():
	pass

def era():
	pass

def param():
	pass

def _print():
	pass

def end():
	pass


def execute_operator(argument):
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
        14	:	equal
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
    return func()

