'''
Session 4:
    Create a graphical application that represents an led controller
'''
from tkinter import *

def on_led_on_pressed():
    label.config(text="Les is ON")
    led_canvas.create_oval(20, 20, 120 , 120 , outline="red" , fill="red" )
    print("Led is on")

def on_led_off_pressed():
    led_canvas.create_oval(20, 20, 120 , 120 , outline="white" , fill="white" )
    label.config(text="Led is OFF")
    print("Led is off")

root = Tk()

led_canvas = Canvas(root , width=120 , height=120 , selectforeground="red" , borderwidth=3)
led_canvas.create_oval(20, 20, 120 , 120 , outline="white" , fill="white" )
on_button = Button(root , width=50 , height=5 , text="Led ON" , command=on_led_on_pressed , highlightbackground="red")
off_button = Button(root , width=50 , height=5 , text="Led OFF" , command=on_led_off_pressed , highlightbackground="black" )
label = Label(root , text = "led status" , width=50 , height = 5 , font=15 )

led_canvas.pack()
label.pack()
on_button.pack()
off_button.pack()

root.geometry("500x500+900+250")
root.mainloop()


