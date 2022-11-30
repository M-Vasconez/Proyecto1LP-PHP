import ply.lex as lex

#LENGUAJE PHP

reserved = {
  # Leonardo Pincay
  'and':'AND',
  'or':'OR',
  'xor':'XOR',
  'SplFixedArray':'SPLFIXEDARRAY', 
  'setSize':'SETSIZE', 
  'SplQueue': 'SPLQUEUE', 
  'push': 'PUSH', 
  'new': 'NEW' ,
  'echo':'ECHO',
  'print':'PRINT',
  'fgets':'FGETS',
  'fscanf':'FSCANF',
  'readline': 'READLINE',
  'push': 'PUSH',
  'pop': 'POP',
  #Bryan Segovia
  'if':'IF',
  'else':'ELSE',
  'while':'WHILE',
  'for':'FOR',
  'function':'FUNCTION'
}

tokens = (
  # Leonardo Pincay
  'STRING',
  'INTEGER',
  'FLOAT',
  'BOOLEAN',
  'NULL',
  'VARIABLE',
  'EQUAL',
  'PLUS_EQUAL',
  'CONCAT_EQUAL',
  'NOT',
  'BOOLEAN_AND',
  'BOOLEAN_OR',
  'LPAREN',
  'RPAREN',
  'LKEY',
  'RKEY',
  'ENDLINE',
  'LBRACKET',
  'RBRACKET',
  'OPEN_TAG',
  'CLOSE_TAG',
  'COMA',
  'ARROW',
  #Matias Vasconez
  'IS_EQUAL',
  'IS_GREATER_OR_EQUAL',
  'IS_NOT_EQUAL',
  'IS_SMALLER_OR_EQUAL',
  'IS_GREATER',
  'IS_SMALLER',
  'COLON',
  'IDENTITY',
  'NEGATION',
  'ADDITION',
  'SUBTRACTION',
  'MULTIPLICATION',
  'DIVISION',
  'MODULO',
  'EXPONENTIATION',
  'WHITESPACE',
  'TAB_VERTICAL',
  'ESCAPE',
  'ADVANCE_PAGE',
  #Bryan Segovia
  'OPERADOR_DECREMENTO',
  'SINTAXIS_ARRAY',
  'OPERADOR_INCREMENTO',
  'OPERADOR_CONCATENACION',
  'COMILLA_DOBLE',
  'ARGUMENTO'
)+tuple(reserved.values())

# Leonardo Pincay
t_STRING = r"'.[^'\n]*'"
t_INTEGER = r'\d+'
t_FLOAT = r'(\.?\d*)\.(\d)+'
t_BOOLEAN = r'true|TRUE|false|FALSE'
t_NULL = r'null|NULL'
t_EQUAL = r'=' 
t_PLUS_EQUAL = r'\+='
t_CONCAT_EQUAL = r'\.='
t_NOT = r'!'
t_BOOLEAN_AND = r'&&'
t_BOOLEAN_OR = r'\|\|'
t_AND = r'and'
t_OR = r'or'
t_XOR = r'xor'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_SPLFIXEDARRAY = r'SplFixedArray'
t_SETSIZE = r'setSize'
t_PUSH = r'push'
t_NEW = r'new'
t_ENDLINE = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_OPEN_TAG = r'<\?php'
t_CLOSE_TAG = r'\?>'
t_COMA = r','
t_ARROW = r'->'
#Matias Vasconez
t_IS_EQUAL = r'=='
t_IS_GREATER_OR_EQUAL = r'>='
t_IS_NOT_EQUAL = r'!='
t_IS_SMALLER_OR_EQUAL = r'<='
t_IS_GREATER= r'>'
t_IS_SMALLER = r'<'
t_COLON = r'\:'
t_IDENTITY=r'\+$.'
t_NEGATION=r'-$.'
t_ADDITION=r'\+'
t_SUBTRACTION = r'-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_EXPONENTIATION = r'\*\*'
t_ECHO=r'echo'
t_PRINT=r'print'
t_FGETS=r'fgets'
t_FSCANF=r'fscanf'
t_READLINE=r'readline'
t_WHITESPACE=r'\\t | \\r | \\n'
t_TAB_VERTICAL = r'\\v'
t_ESCAPE = r'\\e'
t_ADVANCE_PAGE = r'\\f'
#Bryan Segovia
t_OPERADOR_DECREMENTO = r'--'
t_SINTAXIS_ARRAY = r'=>'
t_OPERADOR_INCREMENTO = r'\+\+'
t_OPERADOR_CONCATENACION = r'\.'
t_COMILLA_DOBLE= r'"'

#Bryan Segovia
def t_ARGUMENTO(t):
  r'[a-zA-Z]+'
  t.type=reserved.get(t.value,'ARGUMENTO')
  t.type = reserved.get(t.value, 'BOOLEAN')
  return t

#Bryan Segovia
def t_VARIABLE(t):
  r'\${1,2}([a-z]+[\d]*)+'
  t.type=reserved.get(t.value,'VARIABLE')
  return t


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
  


t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*|\/\/.*'


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
  


lexer = lex.lex()


# def getTokens(lexer):
#   for tok in lexer:
#     print(tok)

# script = open("algoritmo_Vasconez.txt")
# lexer.input(script.read())

# while True:
#   tok = lexer.token()
#   if not tok: 
#       break      
#   print(tok)
