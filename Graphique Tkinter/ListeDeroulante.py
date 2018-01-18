import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)

        self.title("Tkinter et ttk")
        self.geometry('320x320+100+100')

        # widget tkinter :
        self.frame = tk.Frame(self).grid(row=0, column=0)

        # widget spécifique ttk :

        self.combo_value = tk.StringVar()
        self.combo = ttk.Combobox(self.frame,textvariable=self.combo_value)
        self.combo['values'] = ('X', 'Y', 'Z')
        self.combo.current(1)
        self.combo.grid(row=0, column=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
    app.quit()