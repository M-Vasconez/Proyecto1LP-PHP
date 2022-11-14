from lexicoSegovia import tokens
import ply.yacc as yacc

def p_cuerpo(p):
  '''cuerpo : salida 
  | asignacion 
  | funcion'''

def p_salida(p):
  "salida : ECHO COMILLA_DOBLE valor COMILLA_DOBLE ENDLINE"

def p_salida_print(p):
  "salida : PRINT LPAREN valor RPAREN"

def p_valor(p):
  '''valor : ARGUMENTO 
  | INTEGER 
  | FLOAT 
  | BOOLEAN'''

def p_asignacion(p):
  'asignacion : VARIABLE EQUAL valor ENDLINE'

def p_funcion(p):
  'funcion : FUNCTION ARGUMENTO LPAREN VARIABLE RPAREN LKEY ARGUMENTO RKEY'

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

'''import sintactico

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  sintactico.validaRegla(s)

Ejemplos que por ahora puede validar
a=20
variable=30.2
imprimir(var)
imprimir(20.3)
'''

'''
Para practicar implemente las siguientes reglas:
a=30+23
var=20-310*292/23
cond=20>variable
if var>10: imprimir(True)
'''
