#Semantic Controller
from light_datastructures import *
import sys

# INITIALIZE DICTIONARIES
type_dict = {
    'void'      : 0,
	'boolean'   : 1,
    'int'       : 2,
    'decimal'   : 3,
    'string'    : 4,
    'fraction'  : 5
}

# DEFINE CLASSES
class Var:
    # Instance
    def __init__(self):
        self.id = -1
        self.name = ""
        self.type = 0
        self.value = None

    def erase(self):
        self.id = -1
        self.name = ""
        self.type = 0
        self.value = None

class Function:
    def __init__(self):
        self.id = -1
        self.name = ""
        self.next_var_id = 0
        self.type = ""
        self.vars = {}

    def erase(self):
        self.id = -1
        self.name = ""
        self.next_var_id = 0
        self.type = ""
        self.vars = {}

    def add_var(self, var):
        if var.name not in self.vars:
            self.vars[var.name] = (self.next_var_id, var.name, var.type, var.value)
            self.next_var_id += 1
        else:
            Error.already_defined('variable', var.name)

    def init_func(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type


class FunctionTable:

    global_func = Function()
    global_func.init_func(0, 'program', type_dict['void'])
    
    function_dict = {
        'program' : global_func
    }
    next_func_id = 1
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

    @classmethod
    def add_function(cls, func):
        if func.name not in cls.function_dict:
            cls.function_dict[func.name] = Function(cls.next_func_id, func.name, func.type)
            cls.next_func_id += 1
        else:
            Error.already_defined('function', func.name)

    @classmethod
    def print_all(cls):
        print cls.function_dict

    @classmethod
    def get(cls, function_name):
        return cls.function_dict.get(function_name)
    

class SemanticInfo:
    current_func_id = 0

    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

    def get_next_func_id():
        current_func_id = current_func_id + 1
        return current_func_id - 1

class Error:

    @staticmethod
    def already_defined(type, name):
        print "Semantic Error: " + type + " '" + name + "' already defined\n"
        sys.exit()