from memory_handler import *
from light_datastructures import *
from quadruple import *
from figures import *
import time

import itertools
try:
    from itertools import izip_longest
except ImportError:
    # Python 3...
    from itertools import zip_longest
    izip_longest = zip_longest

win = None #GraphWin("LIGHT", 500, 500)
move_speed = 0.001
text_color = [0,0,0]
fig_dict = {}
win_name = "LIGHT"

def execute_operator(argument, quad, index):
	"""Execute quad operator
	
	Execute quad operator
	
	Arguments:
		argument {} -- 
		quad {Quadruple} -- quadruple
		index {int} -- int
	
	Returns:
		Function -- Function to execute
	"""

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
		12	:	mod,
		15	:	equal,
		16	:	gotof,
		17	:	gotot,
		18	:	goto,
		19	:	ret,
		20	:	_return,
		21	:	gosub,
		22	:	era,
		23	:	param,
		24	:	_print,
		25	:	end,	
		26	:	alloc,
		27	:	eqarr,
		28	:	newfig,
		29	:	addv,
		30	:	addc,
		31	:	adds,
		32	:	wsize,
		33	:	cam,
		34	:	move,
		35	:	rst,
		36 	:	wait,
		37	:	backgroundColor,
		38	:	moveSpeed,
		39	:	hide,
		40	:	show,
		41	:	textColor,
		42	:	gprint,
		43 	: 	winname,
		44	:	length,
		45	:	sine,
		46	:	cosine,
		47	:	tangent,
		48	:	exponential,
		49	:	log10,
		50	:	square_root,
		51	:	power

	}
	# Get the function from switcher dictionary
	func = switcher.get(argument, lambda: "nothing")
	# Execute the function
	return func(quad, index)

def plus(quad, index):
	""" Executes plus quadruple """
	MemoryHandler.binary_operator(quad)

def minus(quad, index):
	""" Executes minus quadruple """
	MemoryHandler.binary_operator(quad)

def times(quad, index):
	""" Executes times quadruple """
	MemoryHandler.binary_operator(quad)

def over(quad, index):
	""" Executes over quadruple """
	MemoryHandler.binary_operator(quad)

def mod(quad, index):
	""" Executes mod quadruple """
	MemoryHandler.binary_operator(quad)

def lessThan(quad, index):
	""" Executes less than quadruple """
	MemoryHandler.binary_operator(quad)

def greaterThan(quad, index):
	""" Executes greater than quadruple """
	MemoryHandler.binary_operator(quad)

def lessEqThan(quad, index):
	""" Executes less than or equal quadruple """
	MemoryHandler.binary_operator(quad)

def greaterEqThan(quad, index):
	""" Executes greater than or equal quadruple """
	MemoryHandler.binary_operator(quad)

def equals(quad, index):
	""" Executes equals quadruple """
	MemoryHandler.binary_operator(quad)

def notEqual(quad, index):
	""" Executes not equals quadruple """
	MemoryHandler.binary_operator(quad)

def _and(quad, index):
	""" Executes and quadruple """
	MemoryHandler.and_or_operator(quad)

def _or(quad, index):
	""" Executes or quadruple """
	MemoryHandler.and_or_operator(quad)

def equal(quad, index):
	""" Executes equal quadruple """
	MemoryHandler.assign_operator(quad)

def gotof(quad, index):
	"""go to false
	
	Executes go to false quadruple
	
	Arguments:
		quad {Quadruple} -- quadruple
		index {int} -- int
	
	Returns:
		int -- int
	"""
	index = MemoryHandler.gotof(quad, index)
	return index

def gotot(quad, index):
	"""go to true
	
	Executes go to true quadruple
	
	Arguments:
		quad {Quadruple} -- quadruple
		index {int} -- int
	
	Returns:
		int -- int
	"""
	index = MemoryHandler.gotot(quad, index)
	return index

def goto(quad, index):
	"""go to 
	
	Executes go to quadruple
	
	Arguments:
		quad {Quadruple} -- quadruple
		index {int} -- int
	
	Returns:
		int -- int
	"""
	index = MemoryHandler.goto(quad)
	return index

def ret(quad, index):
	"""return
	
	Executes return quadruple
	
	Arguments:
		quad {Quadruple} -- quadruple
		index {int} -- int
	
	Returns:
		int -- int
	"""
	index = MemoryHandler.ret_operator()
	return index

def _return(quad, index):
	"""return
	
	Executes return quadruple
	
	Arguments:
		quad {Quadruple} -- quadruple
		index {int} -- int
	
	Returns:
		int -- int
	"""
	index = MemoryHandler.return_operator(quad)
	return index

def gosub(quad, index):
	"""go sub
	
	Executes go sub quadruple
	
	Arguments:
		quad {Quadruple} -- quadruple
		index {int} -- int
	
	Returns:
		int -- int
	"""
	index = MemoryHandler.gosub(quad, index)
	return index

def era(quad, index):
	""" Executes era quadruple """
	MemoryHandler.era_operator(quad) 

def param(quad, index):
	""" Executes param quadruple """
	MemoryHandler.param_operator(quad)

def _print(quad, index):
	""" Executes print quadruple """
	MemoryHandler._print(quad)

def length(quad, index):
	""" Executes length quadruple """
	MemoryHandler.get_array_length(quad)

def sine(quad, index):
	""" Executes sine quadruple """
	MemoryHandler.do_math(quad, "sin")

def cosine(quad, index):
	""" Executes cosine quadruple """
	MemoryHandler.do_math(quad, "cos")

def tangent(quad, index):
	""" Executes tangent quadruple """
	MemoryHandler.do_math(quad, "tan")

def exponential(quad, index):
	""" Executes exponential quadruple """
	MemoryHandler.do_math(quad, "exp")

def log10(quad, index):
	""" Executes log10 quadruple """
	MemoryHandler.do_math(quad, "log10")

def square_root(quad, index):
	""" Executes square root quadruple """
	MemoryHandler.do_math(quad, "sqrt")

def power(quad, index):
	""" Executes power quadruple """
	MemoryHandler.do_math_double(quad, "pow")

def end(quad, index):
	""" Executes end quadruple """
	print "> PROGRAM EXECUTION DONE"

def alloc(quad, index):
	""" Executes alloc array quadruple """
	MemoryHandler.allocate_array_space(quad)

def eqarr(quad, index):
	""" Executes equal array quadruple """
	MemoryHandler.get_array_value(quad)

def newfig(quad, index):
	""" Executes new figure quadruple """
	MemoryHandler.set_new_fig(quad)

def addv(quad, index):
	""" Executes add vertex quadruple """
	obj_temp = MemoryHandler.get_fig(quad.result)
	MemoryHandler.add_vertex_fig(quad, obj_temp)
	#MemoryHandler.set_fig(obj_temp, quad)

def addc(quad, index):
	""" Executes add color quadruple """
	obj_temp = MemoryHandler.get_fig(quad.result)
	MemoryHandler.add_color_fig(quad, obj_temp)
	#MemoryHandler.set_fig(obj_temp, quad)
	
def adds(quad, index):
	""" Executes add size quadruple """
	obj_temp = MemoryHandler.get_fig(quad.result)
	MemoryHandler.add_size_fig(quad, obj_temp)
	#MemoryHandler.set_fig(obj_temp, quad)

def wsize(quad, index):
	""" Executes window size quadruple """

	width = MemoryHandler.get_address_value(quad.right_operand)
	height = MemoryHandler.get_address_value(quad.result)

	global win
	global win_name
	win = GraphWin(win_name, width, height)

def move(quad, index):
	""" Executes move quadruple """
	checkWindow()
	# Dejar comentado,
	# obj_temp = MemoryHandler.get_fig(quad.result)
	# MemoryHandler.move_fig(quad, obj_temp)

	if not quad.result in fig_dict:
		Error.figure_not_in_camera()

	fig = fig_dict[quad.result]
		
	x = MemoryHandler.get_address_value(quad.left_operand)
	y = MemoryHandler.get_address_value(quad.right_operand)

	x_step = 1
	if(x < 0):
		x_step = -1
	y_step = 1
	if(y < 0):
		y_step = -1

	for i, j in itertools.izip_longest(range(0, x, x_step), range(0, y, y_step), fillvalue=0):
	#for i, j in zip(range(0, x, x_step), range(0, y, y_step)):
		fig.move(i, j)
		time.sleep(move_speed)


def rst(quad, index):
	""" Executes reset quadruple """
	obj_temp = MemoryHandler.get_fig(quad.result)
	obj_temp.reset()

def wait(quad, index):
	""" Executes wait quadruple """
	MemoryHandler.wait(quad)

def backgroundColor(quad, index):
	""" Executes background color quadruple """
	checkWindow()
	color = MemoryHandler.set_background_color(quad)
	win.setBackground(color_rgb(color[0]%256, color[1]%256, color[2]%256))

def moveSpeed(quad, index):
	""" Executes move speed quadruple """
	move_speed = MemoryHandler.set_move_speed(quad)

def hide(quad, index):
	""" Executes hide quadruple """
	checkWindow()

	if not quad.result in fig_dict:
		Error.figure_not_in_camera()

	fig = fig_dict[quad.result]
	fig.undraw()

def show(quad, index):
	""" Executes show quadruple """
	checkWindow()
	if not quad.result in fig_dict:
		Error.figure_not_in_camera()

	fig = fig_dict[quad.result]
	fig.draw(win)

def textColor(quad, index):
	""" Executes text color quadruple """
	global text_color
	text_color = MemoryHandler.get_text_color(quad)

def gprint(quad, index):
	""" Executes graphical print quadruple """
	checkWindow()
	text = MemoryHandler.get_text(quad)
	t = Text(Point(text[0], text[1]), text[2])
	print(text_color)
	t.setFill(color_rgb(text_color[0]%256, text_color[1]%256, text_color[2]%256))
	t.draw(win)

def winname(quad, index):
	""" Executes window name quadruple """
	global win_name
	name = MemoryHandler.get_window_name(quad)
	win_name = name

def checkWindow():
	""" Check if window is defined """
	if not win:
		Error.window_not_defined()

def cam(quad, index):
	""" Executes camera quadruple """
	checkWindow()
	obj_temp = MemoryHandler.get_fig(quad.result)

	type = abs(quad.result) // 1000

	if type == 6 : #Line
		x = Line(obj_temp.getPoints())
		x.setFill(obj_temp.getColor())
		x.draw(win)
		fig_dict[quad.result] = x

	elif type == 7 : #triangle
		x = Polygon(obj_temp.getPointsList())
		x.setFill(obj_temp.getColor())
		x.draw(win)
		fig_dict[quad.result] = x


	elif type == 8 : #square
		x = Rectangle(obj_temp.getPoints())
		x.setFill(obj_temp.getColor())
		x.draw(win)
		fig_dict[quad.result] = x


	elif type == 9 : #rectangle
		x = Rectangle(obj_temp.getPoints())
		x.setFill(obj_temp.getColor())
		x.draw(win)
		fig_dict[quad.result] = x


	elif type == 10 : #polygon
		x = Polygon(obj_temp.getPointsList())
		x.setFill(obj_temp.getColor())
		x.draw(win)
		fig_dict[quad.result] = x


	elif type == 12 : #circle
		x = Circle(obj_temp.getPointCenter(), obj_temp.radius)
		x.setFill(obj_temp.getColor())
		x.draw(win)
		fig_dict[quad.result] = x

	else:
		pass

def display_print_queue():
	MemoryHandler.display_print()

def RUN_AT_LIGHTSPEED():
	""" Start the virtual machine """
	MemoryHandler.init_class_vars() # Supah weird hack...
	quads = Quadruples.quad_list
	print "\nVIRTUAL MACHINE ==============================="
	QuadIterator(0, quads)

	display_print_queue()

	raw_input("Press enter to exit\n")
	#win.getMouse() # Pause to view result
	if win:
		win.close()

	print "> PROGRAM EXIT"

def QuadIterator(index, quads):
	""" Executes executes the operators quadruple """

	while(index < len(quads)):
		op = quads[index].operator
		print("\n> EXECUTION LINE: {}, Quad: {}".format(index, quads[index].get_list()))
		new_index = execute_operator(op, quads[index], index)
		index = new_index if new_index else (index + 1)
