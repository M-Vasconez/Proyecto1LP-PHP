from tkinter import *
main = Tk()
main.geometry("550x550")

t = Text(main, height=30, width=50)
t.place(x=0,y=0)
scrollbar = Scrollbar(main)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config( command = t.yview)

lexico = Button ( main, text="Analisis Lexico")
sintactico = Button (main, text="Analisis Sintactico")
semantico = Button (main,text="Analisis Semantico")

lexico.place(x=415, y=180)
sintactico.place(x=415, y=240)
semantico.place(x=415, y=300)

result = Text(main, height=30, width=50)
result.place(x=0,y=275)

main.mainloop()


