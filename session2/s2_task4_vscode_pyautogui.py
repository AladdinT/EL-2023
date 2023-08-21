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


extensions = ["clangd" , "c++ testmate", "c++ helper", "cmake" , "cmake tools"]
already_installed = False

# install each extension
for app in extensions:
    print("Searching for : " + app)

    # Show Extensions and search for app
    time.sleep(3)
    pag.hotkey("ctrl", "shift", "x")
    pag.keyDown('backspace')
    time.sleep(1)
    pag.keyUp('backspace')
    pag.write(app)
    time.sleep(3)

    # Locate app icon then click on it
    icon_location = None
    while(icon_location == None):
        icon_location = pag.locateOnScreen( 'icons/' + app +'_logo.png' ,  confidence=0.8)
    icon_point = pag.center(icon_location)
    pag.moveTo(icon_point, duration=0.5)
    pag.click(icon_point)
    
    # See if it is install-able
    button_location = None
    button_location = pag.locateOnScreen( 'icons/install_button.png' ,  confidence=0.8 , minSearchTime=10)
    
    if button_location == None:
        print( app + " Already installed" )
        pag.moveTo(1555, 217, duration=0.5)
        pag.click()
    else:
        print( app + " is being installed" )
        button_point = pag.center(button_location)
        pag.moveTo(icon_point, duration=0.5)
        pag.click(button_point)
    
print("-"*10 + " COMPLETED " + '-'*10)


    
    
    


