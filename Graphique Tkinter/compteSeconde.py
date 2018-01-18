import tkinter as tk

counter = 0
##def counter_label(label):
##  counter = 0
##  def count():
##    global counter
##    counter += 1
##    label.config(text=str(counter))
##    label.after(1000, count)
##  count()

def compter():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, compter)
    #count()

root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()

button1 = tk.Button(root, text='Star', width=25, command=compter)
button1.pack()

button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
compter()
root.mainloop()