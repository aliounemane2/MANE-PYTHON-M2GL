# -*-coding:utf-8 -*
from tkinter import *
import sys
fen = Tk()
fen.title("Menu")
fen.geometry("400x200")

def aff_menu1():
    lab['text']='Menu 1 !'

def quiter():
    fen.destroy()

def ouvrir():
    pass

def afficher():
    pass

lab = Label(fen)
lab['text']='Bonjour Ma !'
lab['fg']='green'
lab.pack()

my_menu=Menu(fen)
#my_sous_menu=Menu(my_menu)

my_sous_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="MenuCascade",menu=my_sous_menu)

my_sous_menu.add_command(label="Afficher",command=afficher)

my_sous_menu_ouv=Menu(my_sous_menu,tearoff=0)
my_sous_menu.add_cascade(label="Ouvrir",menu=my_sous_menu_ouv)
my_sous_menu_ouv.add_command(label="Nouveau",command=quiter)
my_sous_menu_ouv.add_command(label="Encien",command=quiter)
my_sous_menu.add_separator()
my_sous_menu.add_command(label="Quiter",command=quiter)

my_menu.add_command(label="menu 1",command=aff_menu1)

fen.config(menu=my_menu)

fen.mainloop()