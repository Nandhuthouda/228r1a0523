from tkinter import *
from PIL import ImageTk

window = Tk()
background=ImageTk.PhotoImage(files="artbg.jpg")
blabel=Label(window,image=background)
blabel.grid()
frame=Frame(window)
frame.place(x=600,y=100)


window.mainloop()