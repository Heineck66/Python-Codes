from tkinter import *

window = Tk()

l_b = Label(bg="blue", width=20, height=5)
l_b.grid(column=0, row=0)

l_g = Label(bg="green", width=20, height=5)
l_g.grid(column=1, row=1)

l_r = Label(bg="red", width=40, height=5)
l_r.grid(column=0, row=3, columnspan=2)


window.mainloop()
