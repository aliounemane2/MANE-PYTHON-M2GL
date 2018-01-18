# -*-coding:utf-8 -*
from tkinter import *
def pointeur(event):
	chaine.configure(text = "X =" + str(event.x) +\
	", Y =" + str(event.y))

fen = Tk()
cadre = Frame(fen, width =200, height =150, bg="red")

cadre.bind("<Button-1>", pointeur)

cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()