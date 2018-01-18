# -*-coding:utf-8 -*
from tkinter import *
from random import randrange
from tkinter import colorchooser
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
    if(n!=1):
        n=1
        x1, y1, x2, y2 = 10, 390, 390, 10
    global x1, y1, x2, y2, coul,n
    can.create_line(x1,y1,x2,y2,width=2,fill=coul)
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1-10
    n=1

def choix_couleur():
    global coul
    color=colorchooser.askcolor()
    color=str(color)
    color1=color.split("\'")
    color2=color1[1]
    coul=fen['bg']=color2

def tracer_ligne_h():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul,n
    if(n!=2):
        n=2
        x1, y1, x2, y2 = 10, 10, 10, 390
    can.create_line(x1,y1,x2,y2,width=2,fill=coul)
    # modification des coordonnées pour la ligne suivante :
    x1, x2 = x1+10, x2+10
    n=2

def effacer():
    "Tracé d'une ligne dans le canevas can1"
    #can.create_rectangle(0,0,400,400,fill='dark grey')
    can.delete(ALL)
    global x1, y1, x2, y2

    if(n==0):
        x1, y1, x2, y2 = 10, 390, 390, 10 # coordonnées de la ligne
    elif(n==2):
        x1, y1, x2, y2 = 10, 10, 10, 390

def changer_couleur():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]

fen = Tk()
fen.title("Titre de la fenêtre")

#x1, y1, x2, y2 = 10, 390, 390, 10 # coordonnées de la ligne
x1, y1, x2, y2 = 10, 10, 10, 390 # coordonnées de la ligne H
n=0
coul = 'dark green' # couleur de la ligne

can = Canvas(fen,bg='dark grey',height=400,width=400)
can.pack(side=LEFT)

bou1 = Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)

bou10 = Button(fen,text='Tracer une ligne',command=tracer_ligne)
bou10.pack()

bou2 = Button(fen,text='Tracer une ligne H',command=tracer_ligne_h)
bou2.pack()

bou3 = Button(fen,text='Autre couleur',command=changer_couleur)
bou3.pack()

bou30 = Button(fen,text='Choix couleur',command=choix_couleur)
bou30.pack()

bou4 = Button(fen,text='Effacer',command=effacer)
bou4.pack()

fen.mainloop() # démarrage du réceptionnaire d'événements
fen.destroy() # destruction (fermeture) de la fenêtre