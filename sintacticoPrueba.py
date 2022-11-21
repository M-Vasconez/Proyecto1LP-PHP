from lexico import tokens
import ply.yacc as yacc

def p_cuerpo(p):
  '''cuerpo : salida 
  | asignacion 
  | funcion
  | estructuras_control
  | bucles'''

def p_salida(p):
  "salida : ECHO valor ENDLINE"

def p_salida_print(p):
  "salida : PRINT LPAREN valor RPAREN"

def p_valor(p):
  '''valor : ARGUMENTO 
  | INTEGER 
  | FLOAT 
  | BOOLEAN
  | STRING
  | VARIABLE'''

def p_funcion(p):
  'funcion : FUNCTION ARGUMENTO LPAREN VARIABLE RPAREN LKEY ARGUMENTO RKEY'

def p_asignacion(p):
  'asignacion : VARIABLE operador_asignacion valor ENDLINE'

def p_operador_asignacion(p):
  '''operador_asignacion : EQUAL
  | PLUS_EQUAL
  | CONCAT_EQUAL'''

def p_estructuras_control(p):
  '''estructuras_control : if
  | else'''
  
def p_bucle(p):
  'bucles : while'
  

def p_if(p):
  'if : IF LPAREN expresion_logica RPAREN LKEY cuerpo RKEY '

def p_else(p):
  'else : if ELSE LKEY cuerpo RKEY'

def p_expresion_logica(p):
  #cambiar AND y OR por operador logico y de comparacion
  '''expresion_logica : BOOLEAN
  | valor AND valor
  | valor OR valor
  '''

def p_while(p):
  'while : WHILE LPAREN expresion_logica RPAREN COLON'

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
