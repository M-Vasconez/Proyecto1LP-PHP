from lexico import tokens
import ply.yacc as yacc

def p_cuerpo(p):
  '''cuerpo : salida 
  | asignacion 
  | funcion
  | estructuras_control'''

#Bryan Segovia
def p_salida(p):
  "salida : ECHO valor ENDLINE"


#Bryan Segovia
def p_salida_print(p):
  "salida : PRINT LPAREN valor RPAREN ENDLINE"

def p_valor(p):
  '''valor : ARGUMENTO 
  | INTEGER 
  | FLOAT 
  | BOOLEAN
  | STRING
  | VARIABLE
  | estructuras_datos
  | funciones'''

def p_funcion(p):
  'funcion : FUNCTION ARGUMENTO LPAREN VARIABLE RPAREN LKEY ARGUMENTO RKEY'

def p_asignacion(p):
  'asignacion : VARIABLE operador_asignacion valor ENDLINE'

def p_operador_asignacion(p):
  '''operador_asignacion : EQUAL
  | PLUS_EQUAL
  | CONCAT_EQUAL'''
  
def p_estructuras_datos(p):
  'estructuras_datos : array'

def p_operador_comparacion(p):
  '''operador_comparacion : IS_EQUAL
  | IS_GREATER_OR_EQUAL
  | IS_NOT_EQUAL
  | IS_SMALLER_OR_EQUAL
  | IS_GREATER
  | IS_SMALLER'''
  

#Bryan Segovia
def p_operacion_comparacion(p):
  'operacion_comparacion : VARIABLE operador_comparacion VARIABLE'
  
def p_estructuras_control(p):
  '''estructuras_control : if
  | else 
  | while 
  | for'''
   

def p_if(p):
  'if : IF LPAREN expresion_logica RPAREN LKEY cuerpo RKEY '

def p_else(p):
  'else : if ELSE LKEY cuerpo RKEY'

def p_expresion_logica(p):
  #cambiar AND y OR por operador logico y de comparacion
  '''expresion_logica : BOOLEAN
  | valor AND valor
  | valor OR valor
  | valor XOR valor
  | NOT valor
  | valor BOOLEAN_AND valor
  | valor BOOLEAN_OR valor
  '''

def p_while_v1(p):
  'while : WHILE LPAREN valor operador_comparacion valor RPAREN COLON cuerpo'
  
def p_while_v2(p):
  'while : WHILE LPAREN valor operador_comparacion valor RPAREN LKEY TAB_VERTICAL cuerpo RKEY'

def p_array(p):
  'array : LBRACKET valor RBRACKET'
  
def p_funciones(p):
  'funciones : valor LPAREN valor RPAREN LKEY cuerpo RKEY'
  
#Bryan Segovia
def p_tipo_operador(p):
  '''tipo_operador : ADDITION 
  | SUBTRACTION 
  | MULTIPLICATION 
  | DIVISION 
  | MODULO 
  | EXPONENTIATION'''


#Bryan Segovia Ej: $a++ $a=$a**3,  etc
def p_forma_operacion(p):
  '''forma_operacion : VARIABLE OPERADOR_INCREMENTO 
  | OPERADOR_INCREMENTO VARIABLE 
  | VARIABLE OPERADOR_DECREMENTO 
  | OPERADOR_DECREMENTO VARIABLE 
  | VARIABLE EQUAL VARIABLE tipo_operador INTEGER'''


#Bryan Segovia
def p_for(p):
  'for : FOR LPAREN VARIABLE EQUAL INTEGER ENDLINE VARIABLE operador_comparacion INTEGER ENDLINE forma_operacion RPAREN LKEY cuerpo RKEY'  
  

def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
 # Build the parser
parser = yacc.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)
