from tkinter import *
from tkinter.filedialog import *
fen=Tk()
fen.title("Teste")
fen.geometry("200x200")

filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
fichier = open(filename, "r")
content = fichier.read()
fichier.close()

Label(fen, text=content).pack(padx=10, pady=10)

fen.mainloop()