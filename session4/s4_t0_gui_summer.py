""" 
Session 4:
    Quick task : Create a graphical application in Python Tkinter that asks
    the user to enter two integers and displays their sum 
"""

from tkinter import *

def calculate():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    
    if operation.get() == 1:
        result_label.config(text=f"Sum: {num1 + num2}")
    elif operation.get() == 2:
        result_label.config(text=f"Subtraction: {num1 - num2}")

root = Tk()
root.title("Simple Calculator")

label1 = Label(root , text = "Enter the value of M : " , padx=10)
label2 = Label(root , text = "Enter the value of N : " , padx = 10)
entry1 = Entry(root)
entry2 = Entry(root)

operation = IntVar()  # Variable to store the selected operation
sum_radio = Radiobutton(root, text="Sum", variable=operation, value=1 , pady = 5)
sub_radio = Radiobutton(root, text="Subtract", variable=operation, value=2 , pady = 5)

calculate_button = Button(root, text="Calculate", command=calculate , width= 30 , height=sum_radio.winfo_height()*2)
result_label = Label(root, text="Result will be shown here")

label1.grid(row=0 , column=0)
label2.grid(row=1 , column=0)
entry1.grid(row=0 , column=1)
entry2.grid(row=1 , column=1)
sum_radio.grid(row=3 , column=0)
sub_radio.place(x=40 , y=100)
calculate_button.grid(row=3 , column=1)
result_label.grid(row=2 , column=1)

sum_radio.select()
root.geometry("500x200+200+500")
root.mainloop()
