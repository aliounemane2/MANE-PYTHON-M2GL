from tkinter import *
fen=Tk()
fen.title("Teste")
fen.geometry("200x200")

def clavier(event):
    touche = event.keysym
    lab["text"]=touche

canvas = Canvas(fen, width=500, height=500)

canvas.focus_set()

canvas.bind("<Key>", clavier)
canvas.pack()

lab=Label(canvas)
labelfont = ('times', 20, 'bold')
lab['font']=labelfont
lab.pack()
fen.mainloop()