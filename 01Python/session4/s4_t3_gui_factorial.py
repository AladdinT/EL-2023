from tkinter import *

def calculate_factorial():
    
    n = int(entry.get())
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    result_label.config(text=f"Factorial: {factorial}")

root = Tk()
root.title("Factorial Calculator")

# widgets
label = Label(root, text="Enter an integer N:")
entry = Entry(root)
calculate_button = Button(root, text="Calculate Factorial", command=calculate_factorial)
result_label = Label(root, text="Factorial: result")

# widgets placement
label.grid(row=0 , column=0)
entry.grid(row=0 , column=1 , pady=15)
calculate_button.grid(row=1 , column=1 )
result_label.grid(row=1 , column=0 , pady = 15)

root.mainloop()