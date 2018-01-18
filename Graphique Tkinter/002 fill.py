# -*-coding:utf-8 -*
from tkinter import *
fen = Tk()

"""
    fill
     fill à X permet de signaler que le widget prend toute la largeur disponible
     fill à X permet de signaler que le widget prend toute la longueur disponible
     fill à BOTH permet de signaler que le widget prend toute la largeur et la longueur disponible
"""
bouton=Button(fen)
bouton['text'] = "Boutton 1"
bouton['fg'] = "yellow"
bouton['bg'] = "green"
bouton.pack()

bouton=Button(fen)
bouton['text'] = "Boutton 2"
bouton['bg'] = "red"
bouton.pack(fill=X,side=BOTTOM)

"""
   Le paramètre side permet de caler un widget à gauche (LEFT) ou à droite (RIGHT) en haut(TOP)en bas (BOTTOM).
    Pour placer plusieurs widgets sur la même ligne, il suffit de tous les caler du même coté.
"""

bouton=Button(fen)
bouton['text'] = "Boutton 3"
bouton['fg'] = "yellow"
bouton['bg'] = "green"
bouton.pack(side=LEFT)

bouton=Button(fen)
bouton['text'] = "Boutton 4"
bouton['bg'] = "red"
bouton.pack(side=LEFT)

fen.mainloop()
fen.destroy() # destruction (fermeture) de la fenêtre
