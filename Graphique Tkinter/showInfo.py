from tkinter import *

from tkinter import messagebox

root = Tk()

root.title("test")
root.geometry("300x300")

app = Frame(root)
app.grid()
button1 = Button(app, text = " exit " , width=2, command=root.destroy)
button1.grid(padx=110, pady=80)

def dialog():
    var = messagebox.showinfo("test" , "hoi, dit is een test als je dit leest is het gelukt")

button2 = Button(app, text = " sHOW " , width=4, command=dialog)
button2.grid()


root.mainloop()