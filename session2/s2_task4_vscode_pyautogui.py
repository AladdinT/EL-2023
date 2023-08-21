'''
Session 2
Task 4:
    Using PyAutoGUI 
    - To open vscode 
    - install clangd from extension
    - install c++ testmate  from extension
    - install c++ helper  from extension
    - install cmake  from extension
    - install cmake tools  from extension 
'''
#  pip install pyautogui
import pyautogui as pag
import time

pag.PAUSE = 1
# pag.click('icons/clangd_logo.png')
time.sleep(5)
# Start vscode
pag.press("win")
pag.write("vscode")
pag.press("return")

# Wait for it to open then Show Extensions
pag.hotkey("ctrl", "shift", "x")

extensions = ["clangd" , "c++ testmate", "c++ helper", "cmake" , "cmake tools"]

# install each extension
for app in extensions:
    pag.hotkey("ctrl", "shift", "x")
    pag.write(app)
    time.sleep(3)
    icon_location = None
    while(icon_location == None):
        icon_location = pag.locateOnScreen( 'icons\\' + app +'_logo.png' ,  confidence=0.6)
    icon_point = pag.center(icon_location)
    pag.moveTo(icon_point, duration=0.5)
    pag.click(icon_point)
    
    installation = None
    while(installation == None):
        button_location = pag.locateOnScreen( 'icons\\install_button.png' ,  confidence=0.4)
    button_point = pag.center(button_location)
    pag.moveTo(icon_point, duration=0.5)
    pag.click(button_point)
   


    
    
    


