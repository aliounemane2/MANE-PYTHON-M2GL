# -*-coding:utf-8 -*
from tkinter import *
from random import randrange
"""
    Le widget canvas est un widget générique qui offre des possibilités génériques de
    tracé et permet de créer des widgets personnalisés. Le canvas présente une surface de
    dessin avec son propre système de coordonnées.
    Les éléments placés sur le canvas sont appelés canvas items et sont nommés :
        • arc       : une corde ;
        • image     : une image ;
        • line      : une ligne ;
        • oval      : un cercle ou une ellipse ;
        • polygon   : un polygone ;
        • rectangle : un rectangle ou un carré ;
        • text      : un texte ;
        • window : un widget quelconque.
    Chacun de ces éléments peut être créé par le biais de la méthode create_xx(), où xx
    est le nom de l’élément.
"""

def tracer_ligne():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2
    #can.create_line(x1,y1,x2,y2,width=2,fill='dark grey')
    can.delete(ALL)
    if(y1>10):
        y2, y1 = y2+10, y1-10
    elif(x2>10):
        x2, x1 = x2-10, x1+10
    else:
        x1, y1, x2, y2 = 10, 390, 390, 10
    c = randrange(8)
    coul = pal[c]
    can.create_line(x1,y1,x2,y2,width=2,fill=coul)
    fen.after(300,tracer_ligne)
    # modification des coordonnées pour la ligne suivante :


fen = Tk()
fen.title("Titre de la fenêtre")

pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
c = randrange(8) # => génère un nombre aléatoire de 0 à 7
coul = pal[c]


x1, y1, x2, y2 = 10, 390, 390, 10 # coordonnées de la ligne
coul = 'dark green' # couleur de la ligne

can = Canvas(fen,bg='dark grey',height=400,width=400)
can.pack(side=LEFT)

bou1 = Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)

bou2 = Button(fen,text='Tracer une ligne',command=tracer_ligne)
bou2.pack()


fen.mainloop() # démarrage du réceptionnaire d'événements
fen.destroy() # destruction (fermeture) de la fenêtre