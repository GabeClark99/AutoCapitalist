# Gabriel Clark
# August 2021
# Window Resolution: 1920x1080 native, 1600x900 window
# TODO:
##    OCR for game data
##    -get number of businesses
##    -calculate cash per second
##    --get cash per cycle
##    --calculate speed from number of this business as well as total businesses

##    check for and close popups, like events and deals
##    angel reset on earth
##    only buy angel upgrades and managers after angel reset
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

import cv2
import pytesseract
import numpy

# Global Vars
x_pad = 0
y_pad = 0
sleep_samemenu = 0.01 #0.01
sleep_newmenu = 0.50 #0.50
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# ---------------------------------------------------------
# Classes
# ---------------------------------------------------------
class Cord:
    # businesses
    b_lemonaid_buy = (716, 380)
    b_newspaper_buy = (716, 510)
    b_car_buy = (716, 640)
    b_pizza_buy = (716, 780)
    b_donut_buy = (716, 910)
    b_shrimp_buy = (1301, 380)
    b_hockey_buy = (1301, 510)
    b_movie_buy = (1301, 640)
    b_bank_buy = (1301, 775)
    b_oil_buy = (1301, 910)

    b_lemonaid_run = (544, 284)
    b_newspaper_run = (541, 422)
    b_car_run = (538, 551)
    b_pizza_run = (538, 684)
    b_donut_run = (542, 821)
    b_shrimp_run = (1129, 291)
    b_hockey_run = (1113, 419)
    b_movie_run = (1114, 548)
    b_bank_run = (1114, 682)
    b_oil_run = (1114, 820) # ----------------------------NEED TO CONFIRM

    # buy incriment button
    in_max = (1630, 140)

    # upgrades
    up_menu = (212, 536)
    up_buy = (778, 641)
    up_exit = (1660, 180)

    # managers
    ma_menu = (212, 621)
    ma_buy = (776, 648)
    ma_angel = (1030, 320)
    ma_buy_confirm_no = (680, 620)
    ma_buy_confirm_yes = (1050, 620)
    ma_exit =(1650, 180)

    # investors
    iv_menu = (212, 704)

class Color:
    b_running_blue = (76, 102, 115)
    b_idle_blue = (115, 149, 167)

    in_max_white = (240, 233, 226)

    up_menu_orange = (220, 124, 47)
    up_menu_gray = (116, 106, 98)
    up_buy_orange = (241, 140, 76)
    up_buy_gray = (171, 171, 171)
    
    ma_menu_orange = (220, 124, 47)
    ma_menu_gray = (116, 106, 98)
    ma_buy_blue = (143, 188, 211)
    ma_buy_gray = (171, 171, 171)

# ---------------------------------------------------------
# Screen Stuff
# ---------------------------------------------------------
def screenGrab():
##    time.sleep(3) # ------------------------DEBUGGING
    
    image = ImageGrab.grab()
##    image.save(os.getcwd() + '\\images\\screen_' + str(int(time.time())) + '.png', 'PNG') # save image to .\screen_<current time>.png -------------------DEBUGGING
    return image

def imgToText(imagePath):
    image = cv2.imread(imagePath)

    grayImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    grayImage, binaryImage = cv2.threshold(grayImage, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    invertedBinaryImage = cv2.bitwise_not(binaryImage)
##    cv2.imshow('image', invertedBinaryImage)    

    kernel = numpy.ones((2,1), numpy.uint8)
    erodedImage = cv2.erode(invertedBinaryImage, kernel, iterations=1)
    dilatedImage = cv2.dilate(erodedImage, kernel, iterations=1)

    outstring = pytesseract.image_to_string(dilatedImage)
    print('text: ' + outstring)

# ---------------------------------------------------------
# Mouse Clicks
# ---------------------------------------------------------
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##    print ("Click") # ------------------------DEBUGGING

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
    setMousePos(Cord.b_lemonaid_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # newspaper delivery
    setMousePos(Cord.b_newspaper_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # car wash
    setMousePos(Cord.b_car_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # pizza delivery
    setMousePos(Cord.b_pizza_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # donut shop
    setMousePos(Cord.b_donut_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # shrimp boat
    setMousePos(Cord.b_shrimp_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # hockey team
    setMousePos(Cord.b_hockey_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # movie studio
    setMousePos(Cord.b_movie_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # bank (just bank)
    setMousePos(Cord.b_bank_buy)
    leftClick()
    time.sleep(sleep_samemenu)
    
    # oil company
    setMousePos(Cord.b_oil_buy)
    leftClick()
    time.sleep(sleep_samemenu)

def buyManagers():
    screen = screenGrab()

##    print('ma_menu color: ' + str(screen.getpixel(Cord.ma_menu)))   
    if screen.getpixel(Cord.ma_menu) == Color.ma_menu_orange:      # if the managers menu icon is orange...
        print('THERE ARE MANAGERS TO BUY')
        setMousePos(Cord.ma_menu)                                   # hover over the managers menu icon
        leftClick()                                                 # click the managers menu icon
        time.sleep(sleep_newmenu)                                   # wait for the screen to update

        screen = screenGrab()                                       # get the new state of the screen
##        print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy)))
        while screen.getpixel(Cord.ma_buy) != Color.ma_buy_blue and screen.getpixel(Cord.ma_buy) != Color.ma_buy_gray: # while the screen isn't fully loaded...
            print('-the managers screen hasn\'t loaded yet') 
            time.sleep(sleep_newmenu)
            screen = screenGrab()
##            print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy)))   
        print('-the managers screen has loaded')
        
        setMousePos(Cord.ma_buy)                                    # hover over the manager buy icon
##        print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy))) 
        while screen.getpixel(Cord.ma_buy) == Color.ma_buy_blue:      # while the first cash manager in the list's buy icon is blue...
            leftClick()                                             # click on the first cash manager in the list's buy icon
            print('-bought a cash manager!')
            time.sleep(sleep_samemenu)                              # wait for the screen to update
            screen = screenGrab()                                   # grab the new state of the screen, and repeat
##            print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy))) 
        print('-no more cash managers to buy')                       # now there are no more cash managers left to buy
            
##        setMousePos(Cord.ma_angel)                                  # hover over the angel managers icon
##        leftClick()                                                 # click on the angel managers icon
##        
##        screen = screenGrab()                                       # grab the new state of the screen
##        setMousePos(Cord.ma_buy)
####        print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy))) 
##        while screen.getpixel(Cord.ma_buy) == (143, 188, 211):      # while the first angel manager in the list's buy icon is blue...
##            leftClick()                                             # click on the first angel manager in the list's buy icon
##            print('bought an angel manager!')
##            time.sleep(sleeptime)                                   # wait for the screen to update
##            screen = screenGrab()                                   # grab the new state of the screen
####            print('ma_buy color: ' + str(screen.getpixel(Cord.ma_buy))) 
##
####            print('ma_buy_confirm_no color: ' + str(screen.getpixel(Cord.ma_buy_confirm_no)))   
##            if screen.getpixel(Cord.ma_buy_confirm_no) == (224, 100, 100):  # if the game asks us to confirm our purchase...
##                setMousePos(Cord.ma_buy_confirm_no)                         # hover over the 'No' button
##                leftClick()                                                 # click on the 'No' button
##                print('clicked no!')
##                break                                                       # stop purchasing angel managers
##        print('no more angel managers to buy')                              # now there are no more angel managers left to buy
        
        setMousePos(Cord.ma_exit) # hover over the managers menu exit icon
        leftClick() # click on the managers menu exit icon
        time.sleep(sleep_newmenu)
        print('-exited the managers menu!')
        
##    else:
##        print ('there are no managers to buy')

def buyCashUpgrades():
    screen = screenGrab()   # get the current state of the screen
    
##    print('up_menu color: ' + str(screen.getpixel(Cord.up_menu)))
    if screen.getpixel(Cord.up_menu) == Color.up_menu_orange:       # if the upgrade menu button is orange... 
        print('THERE ARE UPGRADES TO BUY')
        setMousePos(Cord.up_menu)                                   # hover over the upgrades menu icon
        leftClick()                                                 # click the upgrades menu icon
        time.sleep(sleep_newmenu)                                   # wait for the screen to update

        screen = screenGrab()                                       # get the new state of the screen
##        print('up_buy color: ' + str(screen.getpixel(Cord.up_buy))) 
        while screen.getpixel(Cord.up_buy) != Color.up_buy_orange and screen.getpixel(Cord.up_buy) != Color.up_buy_gray: # while the screen isn't fully loaded...
            print('-the upgrades screen hasn\'t loaded yet') 
            time.sleep(sleep_newmenu)
            screen = screenGrab()
##            print('up_buy color: ' + str(screen.getpixel(Cord.up_buy)))
        print('-the upgrades screen has loaded')

        setMousePos(Cord.up_buy)                                    # hover over the cash upgrade buy button
##        print('up_buy color: ' + str(screen.getpixel(Cord.up_buy)))
        while screen.getpixel(Cord.up_buy) == Color.up_buy_orange:  # while the first cash upgrade's buy icon is orange...
            leftClick()                                             # click on the first cash upgrade's buy button
            print('-bought a cash upgrade!')
            time.sleep(sleep_samemenu)                              # wait for the screen to update
            screen = screenGrab()                                   # grab the state of the screen post-upgrade
##            print('up_buy color: ' + str(screen.getpixel(Cord.up_buy)))
        print('-no more cash upgrades to buy')

        setMousePos(Cord.up_exit)   # hover over the upgrades exit button
        leftClick()                 # click on the upgrades exit button
        time.sleep(sleep_newmenu)
        print('-exited the upgrades menu!')
##    else:
##        print('there are no upgrades to buy')

def setBuyMax():
    screen = screenGrab()       # get the current state of the screen
    setMousePos(Cord.in_max)    # hover over the increment button
    
##    print('in_max color: ' + str(screen.getpixel(Cord.in_max)))
    while screen.getpixel(Cord.in_max) != Color.in_max_white:  # while the increment button is not set to max...
        print('increment button is not set to max')
        leftClick()                                         # click the increment button
        time.sleep(sleep_samemenu)                               # wait for the screen to update
        screen = screenGrab()                               # get the updated screen
##        print('in_max color: ' + str(screen.getpixel(Cord.in_max)))
    print('increment button is set to max')

def manualRunBusinesses():
    screen = screenGrab() # get the current state of the screen
    
    if screen.getpixel(Cord.b_lemonaid_run) == Color.b_idle_blue:
        print('manually running lemonaid')
        setMousePos(Cord.b_lemonaid_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_newspaper_run) == Color.b_idle_blue:
        print('manually running newspaper')
        setMousePos(Cord.b_newspaper_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_car_run) == Color.b_idle_blue:
        print('manually running car')
        setMousePos(Cord.b_car_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_pizza_run) == Color.b_idle_blue:
        print('manually running pizza')
        setMousePos(Cord.b_pizza_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_donut_run) == Color.b_idle_blue:
        print('manually running donut')
        setMousePos(Cord.b_donut_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_shrimp_run) == Color.b_idle_blue:
        print('manually running shrimp')
        setMousePos(Cord.b_shrimp_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_hockey_run) == Color.b_idle_blue:
        print('manually running hockey')
        setMousePos(Cord.b_hockey_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_movie_run) == Color.b_idle_blue:
        print('manually running movie')
        setMousePos(Cord.b_movie_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_bank_run) == Color.b_idle_blue:
        print('manually running bank')
        setMousePos(Cord.b_bank_run)
        leftClick()
        time.sleep(sleep_samemenu)

    if screen.getpixel(Cord.b_oil_run) == Color.b_idle_blue:
        print('manually running oil')
        setMousePos(Cord.b_oil_run)
        leftClick()
        time.sleep(sleep_samemenu)

def runLoop():
    setBuyMax()
    leftClick() #----------------------TEMP. SET TO BUY X1
    x = 1
    while True:
        print('loop ' + str(x))
        manualRunBusinesses()
        buyCashUpgrades()
        buyManagers()
        buyBusinesses()
        x = x + 1
        if x % 100 == 0:
            print('SLEEPING FOR 2m')
            time.sleep(2*60)
# ---------------------------------------------------------

def main():
    
    #buyBusinesses()
    #buyManagers()
    #buyCashUpgrades()
    #setBuyMax()
    #manualRunBusinesses()
    pass

##    path = os.getcwd() + '\\images\\lem_cost_bottom.png'
##    imgToText(path)

if __name__ == '__main__':
    main()
