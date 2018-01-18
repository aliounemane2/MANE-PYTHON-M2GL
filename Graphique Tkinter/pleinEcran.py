from tkinter import *
import sys
Root=Tk()
RTitle=Root.title("Windows")
RWidth=Root.winfo_screenwidth()
RHeight=Root.winfo_screenheight()
Root.geometry(("%dx%d")%(RWidth,RHeight))
class StatusBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)
    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()
    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
status=StatusBar(Root)
status.pack(side=BOTTOM, fill=X)
Root.mainloop()

