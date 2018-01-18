from tkinter import *
from tkinter.filedialog import *
fen=Tk()
fen.title("Teste")
fen.geometry("200x200")

filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
photo = PhotoImage(file=filepath)
canvas = Canvas(fen, width=photo.width(), height=photo.height(), bg="yellow")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

fen.mainloop()