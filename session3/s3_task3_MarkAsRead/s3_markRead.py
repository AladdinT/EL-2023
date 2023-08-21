'''
Session 5
Task 1: 
    Mark all emails as read using pyautogui
'''
import pyautogui as pag
from time import sleep

pag.PAUSE = 1 

pag.press('win')
sleep(1)
pag.press(['c','h','r','o','m','e'])
pag.press('return')
sleep(3)
pag.hotkey('ctrl + t')
pag.write('gmail.com', interval=0.1)
pag.press('return')

pointxy = None
while pointxy is None :
    pointxy = pag.locateOnScreen('promotions.png', confidence = 0.5)
pag.moveTo(pointxy[0]+50, pointxy[1]+30 , duration=0.5)
pag.click()

pointxy = None
while pointxy is None :
    pointxy = pag.locateOnScreen('selectall.png', confidence = 0.8)
pag.moveTo(pointxy[0]+20, pointxy[1]+20 , duration=0.5)
pag.click()

pointxy = None
while pointxy is None :
    pointxy = pag.locateOnScreen('markasread.png', confidence = 0.9)
pag.moveTo(pointxy[0]+20, pointxy[1]+20 , duration=0.5)
pag.click()

sleep(10)
pag.hotkey('ctrl','w')
