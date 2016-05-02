
# INITIALIZE DICTIONARIES
type_dict = {
    # Primitive Types
    'void'      : 0,
    'boolean'   : 1,
    'int'       : 2,
    'decimal'   : 3,
    'string'    : 4,

    # Figure types
    'point'     : 5,
    'line'      : 6,
    'triangle'  : 7,
    'square'    : 8,
    'rectangle' : 9,
    'polygon'   : 10,
    'star'      : 11,
    'circle'    : 12 
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
}
special_operator_dict = {
    '('     : 12,
    ')'     : 13,
	'='     : 14,
	'gotof'	: 15,
	'gotot'	: 16,
	'goto'	: 17,
    'ret'   : 18,
    'return': 19,
    'gosub' : 20,
    'era'   : 21,
    'param' : 22,
    'print' : 23,
    'end'   : 24,
    'alloc'	: 25,
    'eqarr'	: 26,
    'newfig': 27,
    'addv'	: 28,
    'addc'	: 29,
    'adds'  : 30,
    'wsize' : 31,
    'cam'	: 32,
    'move'	: 33,
    'rst'	: 34,
    'wait'	: 35,
    'bgc'	: 36,
    'mvs'	: 37,
    'hide'	: 38,
    'show'	: 39,
    'txtc'	: 40,
    'printg': 41,
    'winame': 42,
    'length': 43

}

merged_dict = dict(operator_dict, **special_operator_dict)
inv_op_dict = {v: k for k, v in merged_dict.items()}

initializer_dict = {
    # Primitive Types
    0   :   "",         #void
    1   :   False,      #boolean
    2   :   0,          #int
    3   :   0.0,        #decimal
    4   :   "",         #string
    5   :   "",         #decimal, missing probably a fraction class

    #figure types, missing class 
    6   :   "",         #point
    7   :   "",         #line
    8   :   "",         #triangle
    9   :   "",         #square
    10  :   "",         #rectangle
    11  :   "",         #polygon
    12  :   "",         #star
    13  :   "",         #circle
}

# Helper Classes

class Stack(object):
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
