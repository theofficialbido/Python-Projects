from tkinter import *
root = Tk()

myLabel1 = Label(root, text="Hello world - from Tkinter")
myLabel2 = Label(root, text="My name is Abdullah")
myLabel1.grid(row=1, column=0)
myLabel2.grid(row=0, column=1)

root.mainloop()
