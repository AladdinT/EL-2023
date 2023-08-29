from tkinter import * 

root = Tk()
canvas1 = Canvas(root, width=800 , height=800 , bg="red")

canvas1.pack(pady=20 , padx=20)

canvas1.create_line(20 , 20 , 80 , 80 , fill="black")
canvas1.create_oval(20,20,800,800)
root.mainloop()






""" import tkinter as tk
import math

def update_acceleration():
    # Simulated acceleration value (e.g., you can replace this with real data)
    acceleration += 5
    if acceleration > 100:
        acceleration = 0

    update_needle()
    root.after(1000, update_acceleration)

def update_needle():
    angle = -90 + acceleration * 1.8  # Mapping acceleration to an angle (180 degrees divided by 100)
    radians = math.radians(angle)
    x = dial_center[0] + needle_length * math.cos(radians)
    y = dial_center[1] - needle_length * math.sin(radians)

    canvas.coords(needle, dial_center[0], dial_center[1], x, y)
    update_needle_color()

def update_needle_color():
    if 0 <= acceleration <= 60:
        color = "green"
    elif 60 < acceleration <= 80:
        color = "orange"
    else:
        color = "red"

root = root
root.title("Analog Car Accelerometer")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

dial_center = (150, 150)
dial_radius = 100
needle_length = 80

dial = canvas.create_arc(
    dial_center[0] - dial_radius,
    dial_center[1] - dial_radius,
    dial_center[0] + dial_radius,
    dial_center[1] + dial_radius,
    start=180, extent=180,
    outline="black", width=2
)

needle = canvas.create_line(
    dial_center[0], dial_center[1],
    dial_center[0], dial_center[1] - needle_length,
    fill="red", width=3
)

acceleration = 0
update_needle()


canvas.itemconfig(needle, fill=color)
root.after(1000, update_acceleration)
 """