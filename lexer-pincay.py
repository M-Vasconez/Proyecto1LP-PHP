import ply.lex as lex

#LENGUAJE PHP

reserved = {
  'echo':'ECHO',
  'and':'AND',
  'or':'OR',
  'xor':'XOR',
  'SplFixedArray':'SPLFIXEDARRAY', 
  'setSize':'SETSIZE', 
  'SpleDoublyLinkedList': 'SPLEDOUBLYLINKEDLIST', 
  'push': 'PUSH', 
  'new': 'NEW' 
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
t_ECHO = r'echo'


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