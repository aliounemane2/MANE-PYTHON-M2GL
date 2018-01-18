import tkinter as Tk

def AfficheLabel(txt):
    label.config(text = txt)

root = Tk.Tk()
label = Tk.Label(root, text = "Clic sur le bouton ")

label.grid(row = 0, column = 0, columnspan = 3)
svEntry = Tk.StringVar()
edit = Tk.Entry(root, textvariable = svEntry)
edit.grid(row = 1, columnspan = 3)

btn1 = Tk.Button(root, text = "Button1", command = lambda x=1:AfficheLabel(str(x)))
btn2 = Tk.Button(root, text = "Button2", command = lambda x=2:AfficheLabel(str(x)))
btn3 = Tk.Button(root, text = "Button3", command = lambda x=svEntry:AfficheLabel(x.get()))
btn1.grid(row = 2, column = 0)
btn2.grid(row = 2, column = 1)
btn3.grid(row = 2, column = 2)

root.mainloop()