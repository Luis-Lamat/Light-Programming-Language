
# INITIALIZE DICTIONARIES
type_dict = {
    # Primitive Types
    'void'      : 0,
    'boolean'   : 1,
    'int'       : 2,
    'decimal'   : 3,
    'string'    : 4,
    'fraction'  : 5,

    # Figure types
    'point'     : 6,
    'line'      : 7,
    'triangle'  : 8,
    'square'    : 9,
    'rectangle' : 10,
    'polygon'   : 11,
    'star'      : 12,
    'circle'    : 13 
}
inv_type_dict = {v: k for k, v in type_dict.items()}

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
    '!=' : 9
}
inv_op_dict = {v: k for k, v in operator_dict.items()}

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
