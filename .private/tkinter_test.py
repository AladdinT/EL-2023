from tkinter import *

root  = Tk()

def p1_click():
    myLabel.config(text="OhNo")


# Labels


myLabel = Label(root , text="Hello World!")
myLabel2 = Label(root , text=" "*20)
myLabel3 = Label(root , text="I am Tohamy!")

# # Buttons
button00 = Button(root , text="x" , padx=50 , pady = 50 , command=p1_click)

myLabel.grid(row=1, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=1, column=3)
button00.grid(row=0 , column=0)


# root window conf
width = 1920 // 2
height = 1080 
x = 1920 // 2 
y = 0
root.geometry(f"{width}x{height}+{x}+{y}")
root.mainloop()
print("Tk terminated")