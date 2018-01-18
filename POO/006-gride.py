from tkinter import *
fen=Tk()
fen.title("Teste")
#fen.geometry("200x200")

for ligne in range(5):
    for colonne in range(5):
        Button(fen, text='%s-%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)

Button(fen, text='10-1', borderwidth=1).grid(row=10, column=1)
Button(fen, text='L1-C552', borderwidth=1).grid(row=1, column=2)
Button(fen, text='L2-C3', borderwidth=1).grid(row=20, column=13)
Button(fen, text='L2-C4', borderwidth=1).grid(row=12, column=14)
Button(fen, text='L3-C3', borderwidth=1).grid(row=3, column=3)
Button(fen, text='8-3', borderwidth=1).grid(row=8, column=3)

fen.mainloop()