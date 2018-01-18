from tkinter import *
fen=Tk()
fen.title("Teste")
fen.geometry("200x200")

photo = PhotoImage(file="img/image.png")

canvas = Canvas(fen,width=350, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

fen.mainloop()