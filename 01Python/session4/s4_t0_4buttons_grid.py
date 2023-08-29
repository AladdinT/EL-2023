'''
Session 4:
    Quick Task: form a "+" shape using buttons with different names
'''
from tkinter import *

root = Tk()

button1 = Button(root,  text="Button1" )
button2 = Button(root,  text="Button2" )
button3 = Button(root,  text="Button3" )
button4 = Button(root,  text="Button4" )

button1.grid(row=0 , column=1)
button2.grid(row=1 , column=0)
button3.grid(row=1 , column=2)
button4.grid(row=2 , column=1)


root.mainloop()
