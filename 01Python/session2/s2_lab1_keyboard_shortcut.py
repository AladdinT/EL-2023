# pip install keyboard
import keyboard
import subprocess
import os 

def on_triggered():
    # Replace with your desied subprocess
    if os.name == 'posix':
        subprocess.run(['nautilus' , '/home/aladin/Downloads/'])
    elif os.name == 'nt':
        subprocess.run(['explorer.exe' , 'C:\\Users\\ahmad\\Downloads\\'])

def listen_for_shortcut():
    # Set the desired shortcut key combination
    shortcut = "ctrl + alt + k"

    # Register the callback function for the shortcut
    keyboard.add_hotkey(shortcut, on_triggered)
    
    # Countinously listen for keyboard events
    keyboard.wait()
    

listen_for_shortcut()