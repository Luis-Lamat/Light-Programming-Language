#Semantic Controller
from ligt_datastructures import *

#INITIALIZE DICTIONARIES

type_dict = {
	'boolean'   : 0,
    'int'       : 1,
    'decimal'   : 2,
    'string'    : 3,
    'fraction'  : 4
}

var_dict = {
	'global'	: {},
	'local'		: {		'funcExemple' : {}
	}
}


#DEFINE CLASSES

class Var:
	def __init__(self, id, name, scope, type, value):
		self.id = id
		self.name = name
		self.scope = scope
		self.type = type
		self.value = value


class Global_information:
	var_id_num = 0
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

    def get_next_var_id():
    	var_id_num = var_id_num + 1
    	return var_id_num - 1
    

gl_info = Global_information()


#DICTIONARY FUNCTIONS
def add_var_dic(var_name, var_type, var_value, var_function):
	if var_function == '':
		if !var_exists_light(var_name):
			var_dict['global'][var_name] = Var(gl_info.get_next_var_id, var_name,'global', type_dict[var_type], var_value)
			return True
		else:
			return False
	else:
		if !var_exists_func(var_name, var_function):
			var_dict['local'][var_function][var_name] = Var(gl_info.get_next_var_id, var_name,'local', type_dict[var_type], var_value)

def var_exists_light(var_name):
	if var_name in var_dict['global']:
		return True
	else:
		return False

def var_exists_func(var_name, var_function):
	if var_name in var_dict['local']['var_function']:
		return True
	else:
		return False
