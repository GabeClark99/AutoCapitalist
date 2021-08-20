import time
from mousestuff import *
from screenstuff import *
from gamedata import *

# Global Vars
# -------------------------------
sleep_samemenu = 0.01 #0.01
sleep_newmenu = 0.50 #0.50
# -------------------------------

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