import time
import pyautogui as rh

class coordinate:
    emptyMessage = (173, 700)

def click():
    rh.click(coordinate.emptyMessage)

def typechat():
    rh.typewrite('only python is real ')
    rh.typewrite('\n')
    time.sleep(1)
    rh.typewrite('send by Onnesok')
    rh.typewrite('\n')

def send():
    print('text send')

while True:
    coordinate()
    click()
    typechat()
    send()
    time.sleep(2)