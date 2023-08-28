'''
Session 4:
    Quick Task: Write a program that asks the user to type a word
    and return him its reverse
'''
# Import the tkinter module
from tkinter import *

# Function to reverse the entered word and update the label
def b1_pressed():
    label2.configure(text=entry1.get()[::-1])

# Create the main window
root = Tk()

# Create widgets
entry1 = Entry(root, width=50)
label1 = Label(root, text="Enter a word", pady=30)
label2 = Label(root, text="", width=50)
button1 = Button(root, text="Reverse", command=b1_pressed, width=50)

# Place widgets using the grid layout manager
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=1)
button1.grid(row=2, column=1)

# Start the main event loop
root.mainloop()

