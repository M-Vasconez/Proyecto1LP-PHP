from tkinter import *
from lexico import *
from sintactico import *
main = Tk()
main.geometry("550x550")

def test_lex():
    result.delete(1.0, END)
    lexer.input(t.get(1.0, "end-1c"))

    while True:
        tok = lexer.token()
        if not tok: 
            break      
        result.insert(END, tok)
        result.insert(END, '\n')

def test_sintax():
    while True:
        try:
            s = t.get(1.0, "end-1c")
        except EOFError:
            break
        if not s: continue
        resultado = validaRegla(s)
        result.insert(END, str(resultado))
        result.insert(END, '\n')
        if resultado ==None:
            break

t = Text(main, height=30, width=50)
t.place(x=0,y=0)
scrollbar = Scrollbar(main)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config( command = t.yview)

lexico = Button ( main, text="Analisis Lexico", command=test_lex)
sintactico = Button (main, text="Analisis Sintactico", command=test_sintax)
semantico = Button (main,text="Analisis Semantico")

lexico.place(x=415, y=180)
sintactico.place(x=415, y=240)
semantico.place(x=415, y=300)

result = Text(main, height=30, width=50)
result.place(x=0,y=275)

main.mainloop()


