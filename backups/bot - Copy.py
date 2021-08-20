# Gabriel Clark
# August 2021
# Window Resolution: 1920x1080 native, 1600x900 window
# TODO:
##    buy managers on earth
##    buy upgrades on earth
##    set buy max on earth
##    angel reset on earth
##    only buy angel upgrades and managers after angel reset
##    game loop driver
##    change planets
    
##    buy businesses on moon
##    buy managers on moon
##    set buy max on moon
##    buy upgrades on moon
##    angel reset on moon
    
##    buy businesses on mars
##    buy managers on mars
##    set buy max on moon
##    buy upgrades on mars
##    angel reset on mars

import PIL
from PIL import ImageGrab
import os
import time

import win32api, win32con

from PIL import ImageOps
from numpy import *

# Global Vars
x_pad = 0
y_pad = 0
sleeptime = 3
screen = ImageGrab.grab()

# ---------------------------------------------------------
# Coordinates Class
# ---------------------------------------------------------
class Cord:
    # businesses
    b_lemonaid = (716, 384)
    b_newspaper = (716, 516)
    b_car = (716, 648)
    b_pizza = (716, 780)
    b_donut = (716, 917)
    b_shrimp = (1301, 384)
    b_hockey = (1301, 516)
    b_movie = (1301, 648)
    b_bank = (1301, 780)
    b_oil = (1301, 917)

    # upgrades
    up_menu = (212, 536)

    # managers
    ma_menu = (212, 621)
    ma_buy = (776, 648)
    ma_angel = (1030, 320)
    ma_buy_confirm_no = (680, 620)
    ma_buy_confirm_yes = (1050, 620)
    ma_exit =(1650, 180)

    # investors
    in_menu = (212, 704)

# ---------------------------------------------------------
# Screen Stuff???
# ---------------------------------------------------------
def screenGrab():
##    time.sleep(3) # ------------------------DEBUGGING
    
    image = ImageGrab.grab()
    image.save(os.getcwd() + '\\images\\screen_' + str(int(time.time())) + '.png', 'PNG') # save image to .\screen_<current time>.png
    return image

# ---------------------------------------------------------
# Mouse Clicks
# ---------------------------------------------------------
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(sleeptime)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Click")

##def leftDown():
##    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
##    time.sleep(sleeptime)
####    print ("left down")
##
##def leftUp():
##    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##    time.sleep(sleeptime)
####    print ("left up")
    
# ---------------------------------------------------------
# Mouse Position
# ---------------------------------------------------------
def setMousePos(cord):
    win32api.SetCursorPos(cord)

##def getCords():
##    x,y = win32api.GetCursorPos()
####    x = x - x_pad
####    y = y - y_pad
##    print (x,y)
    
# ---------------------------------------------------------
# Game Functions
# ---------------------------------------------------------
def buyBusinesses():    
    global screen
    screen = screenGrab()

    # lemonaide stand
    if screen.getpixel(Cord.b_lemonaid) == (238, 141, 72):
        print ('can buy lemonaid')
        setMousePos(Cord.b_lemonaid)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy lemonaid')
    
    # newspaper delivery
    if screen.getpixel(Cord.b_newspaper) == (238, 141, 72):
        print ('can buy newspaper')
        setMousePos(Cord.b_newspaper)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy newspaper')
    
    # car wash
    if screen.getpixel(Cord.b_car) == (238, 141, 72):
        print ('can buy car')
        setMousePos(Cord.b_car)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy car')
    
    # pizza delivery
    if screen.getpixel(Cord.b_pizza) == (238, 141, 72):
        print ('can buy pizza')
        setMousePos(Cord.b_pizza)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy pizza')
    
    # donut shop
    if screen.getpixel(Cord.b_donut) == (238, 141, 72):
        print ('can buy donut')
        setMousePos(Cord.b_donut)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy donut')
    
    # shrimp boat
    if screen.getpixel(Cord.b_shrimp) == (238, 141, 72):
        print ('can buy shrimp')
        setMousePos(Cord.b_shrimp)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy shrimp')
    
    # hockey team
    if screen.getpixel(Cord.b_hockey) == (238, 141, 72):
        print ('can buy hockey')
        setMousePos(Cord.b_hockey)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy hockey')
    
    # movie studio
    if screen.getpixel(Cord.b_movie) == (238, 141, 72):
        print ('can buy movie')
        setMousePos(Cord.b_movie)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy movie')
    
    # bank (just bank)
    if screen.getpixel(Cord.b_bank) == (238, 141, 72):
        print ('can buy bank')
        setMousePos(Cord.b_bank)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy bank')
    
    # oil company
    if screen.getpixel(Cord.b_oil) == (238, 141, 72):
        print ('can buy oil')
        setMousePos(Cord.b_oil)
        leftClick()
        time.sleep(sleeptime)
    else:
        print ('cannot buy oil')

def buyManagers():
    screen = screenGrab()

    print('ma_menu color: ' + str(screen.getpixel(Cord.ma_menu)))   # -----------------DEBUGGING
    if screen.getpixel(Cord.ma_menu) == (220, 124, 47) or True:             # if the managers menu icon is orange... ------------------------DEBUGGING
        print('there are managers to buy')
        setMousePos(Cord.ma_menu)                                   # hover over the managers menu icon
        leftClick()                                                 # click the managers menu icon
        time.sleep(sleeptime)                                       # wait for the screen to update

        screen = screenGrab()                                       # get the new state of the screen
        setMousePos(Cord.ma_buy)                                    # hover over the manager buy icon
        print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy))) # ----------------DEBUGGING
        while screen.getpixel(Cord.ma_buy) == (238, 141, 72):       # while the first cash manager in the list's buy icon is blue...
            leftClick()                                             # click on the first cash manager in the list's buy icon
            print('bought a cash manager!')
            time.sleep(sleeptime)                                   # wait for the screen to update
            screen = screenGrab()                                   # grab the new state of the screen, and repeat
            print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy))) # ----------------DEBUGGING
        print('no more cash managers to buy')                       # now there are no more cash managers left to buy
            
        setMousePos(Cord.ma_angel)                                  # hover over the angel managers icon
        leftClick()                                                 # click on the angel managers icon
        screen = screenGrab()                                       # grab the new state of the screen
        print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy))) # --------------------DEBUGGING
        while screen.getpixel(Cord.ma_buy) == (238, 141, 72):       # while the first angel manager in the list's buy icon is blue...
            leftClick()                                             # click on the first angel manager in the list's buy icon
            print('bought an angel manager!')
            time.sleep(sleeptime)                                   # wait for the screen to update
            screen = screenGrab()                                   # grab the new state of the screen
            print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy))) # ----------------DEBUGGING

            print('ma_buy_confirm_no color: ' + str(screen.getpixel(Cord.ma_buy_confirm_no)))   # --------------------DEBUGGING
            if screen.getpixel(Cord.ma_buy_confirm_no) == (224, 100, 100):  # if the game asks us to confirm our purchase...
                setMousePos(Cord.ma_buy_confirm_no)                         # hover over the 'No' button
                leftClick()                                                 # click on the 'No' button
                print('clicked no!')
                break                                                       # stop purchasing angel managers
        print('no more angel managers to buy')                              # now there are no more angel managers left to buy
        
        setMousePos(Cord.ma_exit) # hover over the managers menu exit icon
        leftClick() # click on the managers menu exit icon
        print('exited the managers screen!')
        
    else:
        print ('there are no managers to buy')
# ---------------------------------------------------------

def main():
    # gives enough time to get the fullscreen game open
##    print ('7')
##    time.sleep(1)
##    print ('6')
##    time.sleep(1)
##    print ('5')
##    time.sleep(1)
##    print ('4')
##    time.sleep(1)
##    print ('3')
##    time.sleep(1)
##    print ('2')
##    time.sleep(1)
##    print ('1')
##    time.sleep(1)
##    print ('0!')
    
    #buyBusinesses()
    #buyManagers()
    pass

if __name__ == '__main__':
    main()
