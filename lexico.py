import ply.lex as lex

#LENGUAJE PHP

reserved = {
  'and':'AND',
  'or':'OR',
  'xor':'XOR',
  'SplFixedArray':'SPLFIXEDARRAY', 
  'setSize':'SETSIZE', 
  'SpleDoublyLinkedList': 'SPLEDOUBLYLINKEDLIST', 
  'push': 'PUSH', 
  'new': 'NEW' ,
  'echo':'ECHO',
  'print':'PRINT',
  'fgets':'FGETS',
  'fscanf':'FSCANF',
  'readline': 'READLINE',
  'if':'IF',
  'else':'ELSE',
  'while':'WHILE',
  'for':'FOR',
  'function':'FUNCTION'
}

tokens = (
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
  'IS_EQUAL',
  'IS_GREATER_OR_EQUAL',
  'IS_NOT_EQUAL',
  'IS_SMALLER_OR_EQUAL',
  'IS_GREATER',
  'IS_SMALLER',
  'IDENTITY',
  'NEGATION',
  'ADDITION',
  'SUBTRACTION',
  'MULTIPLICATION',
  'DIVISION',
  'MODULO',
  'EXPONENTIATION',
  'ECHO',
  'PRINT',
  'FGETS',
  'FSCANF',
  'READLINE',
  'WHITESPACE',
  'TAB_VERTICAL',
  'ESCAPE',
  'ADVANCE_PAGE',
  'OPERADOR_DECREMENTO',
  'SINTAXIS_ARRAY',
  'OPERADOR_INCREMENTO',
  'OPERADOR_CONCATENACION'
)+tuple(reserved.values())

t_STRING = r"'.[^'\n]*'"
t_INTEGER = r'\d+'
t_FLOAT = r'(\.?\d*)\.(\d)+'
t_BOOLEAN = r'true|TRUE|false|FALSE'
t_NULL = r'null|NULL'
t_VARIABLE = r'\${1,2}([a-z]+[\d]*)+'
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
t_SPLEDOUBLYLINKEDLIST = r'SpleDoublyLinkedList'
t_PUSH = r'push'
t_NEW = r'new'
t_ENDLINE = r';'
t_IS_EQUAL = r'=='
t_IS_GREATER_OR_EQUAL = r'>='
t_IS_NOT_EQUAL = r'!='
t_IS_SMALLER_OR_EQUAL = r'<='
t_IS_GREATER= r'>'
t_IS_SMALLER = r'<'
t_IDENTITY=r'\+$.'
t_NEGATION=r'-$.'
t_ADDITION=r'\+'
t_SUBTRACTION = r'-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\\'
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
t_OPERADOR_DECREMENTO = r'--'
t_SINTAXIS_ARRAY = r'=>'
t_OPERADOR_INCREMENTO = r'\+\+'
t_OPERADOR_CONCATENACION = r'\.'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_FUNCTION = r'function'



def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*|\/\/.*'


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


lexer = lex.lex()


def getTokens(lexer):
  for tok in lexer:
    print(tok)

script = open("algoritmo-pincay.txt")
lexer.input(script.read())

while True:
  tok = lexer.token()
  if not tok: 
      break      
  print(tok)
