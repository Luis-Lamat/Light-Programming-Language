tokens = (
	'INT', 'FLOAT', 'STRING', 'ID', 'PLUS',
	'MINUS', 'TIMES', 'SLASH', 'LPAREN', 'RPAREN',
	'LCURL', 'RCURL', 'SEMICOLON', 'COLON', 'COMMA',
	'EQL', 'NEG', 'LSS', 'GTR', 'IFSYM', 'ELSESYM',
	'PROGRAMSYM', 'PRINTSYM', 'VARSYM', 'INTSYM', 'FLOATSYM',
	)

t_PLUS 		= r'\+'
t_MINUS 	= r'-'
t_TIMES		= r'\*'
t_SLASH		= r'/'
t_LPAREN 	= r'\('
t_RPAREN	= r'\)'
t_SEMICOLON	= r';'
t_LCURL		= r'{'
t_RCURL		= r'}'
t_COLON 	= r':'
t_COMMA		= r','
t_EQL		= r'='
t_NEG		= r'<>'
t_LSS 		= r'<'
t_GTR		= r'>'


#dot      = r'\.'

def t_FLOAT(t):
	r'[0-9]+[\.][0-9]+'
	return t

def t_PROGRAMSYM(t):
	r'program'
	return t

def t_IFSYM(t):
	r'if'
	return t


def t_ELSESYM(t):
	r'else'
	return t

def t_PRINTSYM(t):
	 r'print'
	 return t
def t_VARSYM(t):
	 r'var'
	 return t

def t_INTSYM(t):
 	 r'int'
 	 return t

def t_FLOATSYM(t):
 	r'float'
 	return t

def t_ID(t):
	r'[a-zA-Z][a-zA-Z0-9]*'
	return t

def t_INT(t):
	r'[0-9]+'
	return t

def t_STRING(t):	
	r'\"[a-zA-Z]([a-zA-Z0-9])*\"'
	return t


t_ignore = ' \t'

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")
def t_error(t):
	print "Syntax error at line " + str(t.lexer.lineno) + " Illegal character " + str(t.value[0])
	#print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	sys.exit(0)

import ply.lex as lex
lex.lex()


# ###STATEMENTS!!!!


#http://snatverk.blogspot.mx/2011/01/parser-de-mini-c-en-python.html
def p_program(p):
	'program 	: PROGRAMSYM ID SEMICOLON program1 bloque'
	pass

def p_program1(p):
	'''program1	: vars
				| epsilon'''
	pass

def p_vars(p):
	' vars 		: VARSYM vars1'
	pass

def p_vars1(p):
	'vars1 	: vars2 COLON tipo SEMICOLON vars3'
	pass
def p_vars2(p):
	'vars2 	: ID vars4'
	pass
def p_vars3(p):
	'''vars3 	: vars1
				| epsilon'''
	pass
def p_vars4(p):
	'''vars4 	: COMMA vars2
				| epsilon'''
	pass
def p_tipo(p):
	''' tipo 	: INTSYM
				| FLOATSYM'''
	pass
def p_bloque(p):
	'''bloque 	: LCURL bloque1 RCURL'''
	pass
def p_bloque1(p):
	'''bloque1 	: estatuto bloque1
				| epsilon'''
	pass
def p_estatuto(p):
	'''estatuto : asignacion
				| condicion
				| escritura'''
	pass
def p_asignacion(p):
	'asignacion : ID EQL expresion SEMICOLON'
	pass
def p_expresion(p):
	'expresion 	: exp expresion1'
	pass
def p_expresion1(p):
	'''expresion1 	: epsilon
					| expresion2 exp'''
	pass
def p_expresion2(p):
	'''expresion2 	: LSS
					| GTR
					| NEG'''
	pass

def p_escritura(p):
	'escritura 		: PRINTSYM LPAREN escritura1 RPAREN SEMICOLON'
	pass
def p_escritura1(p):
	'escritura1 	: escritura2 escritura3'
	pass
def p_escritura2(p):
	'''escritura2 	: expresion
					| STRING'''
	pass

def p_escritura3(p):
	''' escritura3 	: COMMA escritura1
					| epsilon'''

def p_exp(p):
	'exp 	: termino exp1'
	pass
def p_exp1(p):
	''' exp1 	: PLUS termino exp1
				| MINUS termino exp1
				| epsilon'''
	pass

def p_condicion(p):
	'''condicion 	: IFSYM LPAREN expresion RPAREN bloque condicion1 SEMICOLON'''
	pass

def p_condicion1(p):
	'''condicion1	: ELSESYM bloque
					| epsilon'''
	pass
def p_termino(p):
	'''termino 	: factor termino1'''
	pass

def p_termono1(p):
	'''termino1 : TIMES factor termino1
				| SLASH factor termino1
				| epsilon'''
	pass

def p_factor(p):
	''' factor	: LPAREN expresion RPAREN
				| factor1 varcte'''
	pass 

def p_factor1(p):
	''' factor1 : PLUS
				| MINUS
				| epsilon'''
	pass

def p_varcte(p):
	''' varcte 	: FLOAT
				| INT
				| ID'''
	pass

def p_epsilon(p):
	'epsilon :'
	pass


def p_error(p):
	print "Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value)
	sys.exit(0)

import ply.yacc as yacc
parser = yacc.yacc()

import sys


if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'programa1.in'

	f = open(fin, 'r')
	data = f.read()
	# print data
	# print "End of file"
	parser.parse(data, tracking=True)

	print("Successful")