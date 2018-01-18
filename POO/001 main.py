# -*-coding:utf-8 -*
# Importation de la bibliothèque tkinter
from tkinter import *
from tkinter.messagebox import *

# création de la fenêtre racine de notre interface
fen = Tk()
fen.title("Titre de la fenetre")
def recupe():
    #print("------------ ok ---------------")
    txt=recup_text.get()
    txt+='\n'+str(var_case.get())
    txt+='\n'+str(choix.get())
    txt+='\n'+str(liste.selection_get())
    txt+='\n'+str(liste.curselection())
    lab['text']=txt
# Création d'un widget Label
# -- Création en une seule ligne avec l'ensemble des paramettre
    #lab = Label(fen, text='Bonjour tout le monde !', fg='red')

lab = Label(fen)
lab['text']='Bonjour Ma !'
lab['fg']='green'
labelfont = ('times', 20, 'bold')
lab['font']=labelfont
#lab.config(font=labelfont)
lab.config(height=3, width=20)
#widget.pack(expand=YES, fill=BOTH)
#lab['bg']='red'
lab.pack()

# Création d'un widget Button
    #bout = Button(fen, text='Quitter', command = fen.destroy)

# Création d'un widget "Saisie deTexte "
recup_text= StringVar()
recup_text.set("Donnez une  valeur")
#lm_txt=Entry ( fen , textvariable = recup_text , width =10)
lm_txt=Entry (fen)
lm_txt['textvariable']=recup_text
lm_txt['width']=10
lm_txt.pack()

# Création d'un widget "Case à cocher "
var_case = IntVar ()
case = Checkbutton ( fen , text ="Question ", variable = var_case )
case . pack ()
# var_case .get () [0 ou 1]

# Création d'un widget "Bouton Radio "
choix = StringVar()
choix1 =Radiobutton(fen,text="Choix 1",variable=choix,value='1')
choix2 =Radiobutton(fen,text="Choix 2",variable=choix,value='2')
choix3 =Radiobutton(fen,text="Choix 3",variable=choix,value='3')
choix1.pack ()
choix2.pack ()
choix3.pack ()
# choix .get () [0 ou 1]

# Création d'un widget "Liste Déroulante "
liste=Listbox(fen)
liste.pack()
liste.insert(END,'Modou')
liste.insert(END,'Astou')
liste.insert(END,'Pathé')
liste.insert(END,'Demba')
# liste.curselection() renvoie l'objet selectionner

def updateLabel():
    pass

value = DoubleVar()
scale = Scale(fen, variable=value)
#scale=Scale(fen, variable=value,length=250, orient=HORIZONTAL, label ='Réglage :',troughcolor ='dark grey', sliderlength =20,showvalue =0, from_=-25, to=125, tickinterval =25)
scale.pack()

s = Spinbox(fen, from_=0, to=10)
s.pack()

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

Button(text='Action', command=callback).pack()

bout = Button(fen)
bout['text']='Valider'
bout['command']  = recupe
bout.pack()

bout = Button(fen)
bout['text']='Quitter'
bout['command']  = fen.destroy
bout.pack()

fen.mainloop()