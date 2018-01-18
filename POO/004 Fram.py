# -*-coding:utf-8 -*
from tkinter import *
from tkinter.messagebox import *

def fonction():

    """
        -- showinfo
        -- showerror
        -- showwarning
    """
    #showinfo("Info","Femêtre showinfo")
fen = Tk()
fen.title("Titre de la fenêtre")
##fen.geometry("400x300")
##cadre = Frame(fen, width =400, height =250,borderwidth=1,bg="green")
##cadre.pack(fill=BOTH)
##
##bout = Button(cadre)
##bout['text']='Show'
##bout['command']  = fonction
##bout.pack()
##
##mess=Label(cadre,text="Texte du message")
##mess.pack(side ="top", fill =X)

frame_1 = Frame(fen,width=400, height=200, bg="blue")
frame_1.pack(side=LEFT)
frame_2 = Frame(fen,width=200, height=200, bg="red")
frame_2.pack(side=LEFT)
##frame_3 = Frame(fen,width=200, height=200, bg="green")
##frame_3.pack()
##frame_4 = Frame(frame_1,width=100, height=100, bg="yellow")
##frame_4.pack(side=LEFT)
##Label(frame_1, text="Frame 1").pack(padx=10, pady=10)
##Label(frame_2, text="Frame 2").pack(padx=10, pady=10)
##Label(frame_3, text="Frame 3",bg="white").pack(padx=10, pady=10)
##Label(frame_4, text="Frame 4",bg="white").pack(padx=10, pady=10)

##l = LabelFrame(fen, text="Titre de la frame", padx=20, pady=20)
##l.pack(fill="both")
##
##Label(l, text="A l'intérieure de la frame").pack()


fen.mainloop()
#fen.destroy() # destruction (fermeture) de la fenêtre