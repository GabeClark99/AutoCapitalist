import time

from cv2 import sampsonDistance
import mousestuff as ms
import screenstuff as ss
import gamedata as gd

# Global Vars
# -------------------------------
sleep_samemenu = 0.01 #0.01
sleep_newmenu = 0.50 #0.50
# -------------------------------

# ---------------------------------------------------------
# Global Functions
# ---------------------------------------------------------
def buyBusinesses():    
    for cur_business in gd.businessList:        # for every business, click on their buy button
        ms.clickPos(cur_business.cord_buy)
        time.sleep(sleep_samemenu)

def buyManagers():
    screen = ss.screenGrab((0, 0, 0, 0))

##    print('ma_menu color: ' + str(screen.getpixel(gd.managers.cord_open)))   
    if screen.getpixel(gd.managers.cord_open) == gd.managers.color_open_on:      # if the managers menu icon is orange...
        print('THERE ARE MANAGERS TO BUY')
        ms.setMousePos(gd.managers.cord_open)                                   # hover over the managers menu icon
        ms.leftClick()                                                 # click the managers menu icon
        time.sleep(sleep_newmenu)                                   # wait for the screen to update

        screen = ss.screenGrab((0, 0, 0, 0))                                       # get the new state of the screen
##        print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy)))
        while screen.getpixel(gd.managers.cord_buy) != gd.managers.color_buy_on and screen.getpixel(gd.managers.cord_buy) != gd.managers.color_buy_off: # while the screen isn't fully loaded...
            print('-the managers screen hasn\'t loaded yet') 
            time.sleep(sleep_newmenu)
            screen = ss.screenGrab((0, 0, 0, 0))
##            print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy)))   
        print('-the managers screen has loaded')
        
        ms.setMousePos(gd.managers.cord_buy)                                    # hover over the manager buy icon
##        print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy))) 
        while screen.getpixel(gd.managers.cord_buy) == gd.managers.color_buy_on:      # while the first cash manager in the list's buy icon is blue...
            ms.leftClick()                                             # click on the first cash manager in the list's buy icon
            print('-bought a cash manager!')
            time.sleep(sleep_samemenu)                              # wait for the screen to update
            screen = ss.screenGrab((0, 0, 0, 0))                                   # grab the new state of the screen, and repeat
##            print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy))) 
        print('-no more cash managers to buy')                       # now there are no more cash managers left to buy
            
##        ms.setMousePos(gd.managers.cord_submenu)                                  # hover over the angel managers icon
##        ms.leftClick()                                                 # click on the angel managers icon
##        
##        screen = screenGrab((0, 0, 0, 0))                                       # grab the new state of the screen
##        ms.setMousePos(gd.managers.cord_buy)
####        print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy))) 
##        while screen.getpixel(gd.managers.cord_buy) == (143, 188, 211):      # while the first angel manager in the list's buy icon is blue...
##            ms.leftClick()                                             # click on the first angel manager in the list's buy icon
##            print('bought an angel manager!')
##            time.sleep(sleeptime)                                   # wait for the screen to update
##            screen = screenGrab((0, 0, 0, 0))                                   # grab the new state of the screen
####            print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy))) 
##
####            print('ma_buy_confirm_no color: ' + str(screen.getpixel(gd.managers.cord_buy_confirm_no)))   
##            if screen.getpixel(gd.managers.cord_buy_confirm_no) == (224, 100, 100):  # if the game asks us to confirm our purchase...
##                ms.setMousePos(gd.managers.cord_buy_confirm_no)                         # hover over the 'No' button
##                ms.leftClick()                                                 # click on the 'No' button
##                print('clicked no!')
##                break                                                       # stop purchasing angel managers
##        print('no more angel managers to buy')                              # now there are no more angel managers left to buy
        
        ms.setMousePos(gd.managers.cord_exit) # hover over the managers menu exit icon
        ms.leftClick() # click on the managers menu exit icon
        time.sleep(sleep_newmenu)
        print('-exited the managers menu!')
        
##    else:
##        print ('there are no managers to buy')

def buyCashUpgrades():
    screen = ss.screenGrab((0, 0, 0, 0))   # get the current state of the screen
    
##    print('up_menu color: ' + str(screen.getpixel(gd.upgrades.cord_open)))
    if screen.getpixel(gd.upgrades.cord_open) == gd.upgrades.color_open_on:       # if the upgrade menu button is orange... 
        print('THERE ARE UPGRADES TO BUY')
        ms.setMousePos(gd.upgrades.cord_open)                                   # hover over the upgrades menu icon
        ms.leftClick()                                                 # click the upgrades menu icon
        time.sleep(sleep_newmenu)                                   # wait for the screen to update

        screen = ss.screenGrab((0, 0, 0, 0))                                       # get the new state of the screen
##        print('up_buy color: ' + str(screen.getpixel(gd.upgrades.cord_buy))) 
        while screen.getpixel(gd.upgrades.cord_buy) != gd.upgrades.color_buy_on and screen.getpixel(gd.upgrades.cord_buy) != gd.upgrades.color_buy_off: # while the screen isn't fully loaded...
            print('-the upgrades screen hasn\'t loaded yet') 
            time.sleep(sleep_newmenu)
            screen = ss.screenGrab((0, 0, 0, 0))
##            print('up_buy color: ' + str(screen.getpixel(gd.upgrades.cord_buy)))
        print('-the upgrades screen has loaded')

        ms.setMousePos(gd.upgrades.cord_buy)                                    # hover over the cash upgrade buy button
##        print('up_buy color: ' + str(screen.getpixel(gd.upgrades.cord_buy)))
        while screen.getpixel(gd.upgrades.cord_buy) == gd.upgrades.color_buy_on:  # while the first cash upgrade's buy icon is orange...
            ms.leftClick()                                             # click on the first cash upgrade's buy button
            print('-bought a cash upgrade!')
            time.sleep(sleep_samemenu)                              # wait for the screen to update
            screen = ss.screenGrab((0, 0, 0, 0))                                   # grab the state of the screen post-upgrade
##            print('up_buy color: ' + str(screen.getpixel(gd.upgrades.cord_buy)))
        print('-no more cash upgrades to buy')

        ms.setMousePos(gd.upgrades.cord_exit)   # hover over the upgrades exit button
        ms.leftClick()                 # click on the upgrades exit button
        time.sleep(sleep_newmenu)
        print('-exited the upgrades menu!')
##    else:
##        print('there are no upgrades to buy')

def setBuyMax():
    screen = ss.screenGrab((0, 0, 0, 0))       # get the current state of the screen
    ms.setMousePos(gd.increment_max_cord)    # hover over the increment button
    
##    print('increment_max_cord color: ' + str(screen.getpixel(gd.increment_max_cord)))
    while screen.getpixel(gd.increment_max_cord) != gd.increment_max_color_enabled:  # while the increment button is not set to max...
        print('increment button is not set to max')
        ms.leftClick()                                         # click the increment button
        time.sleep(sleep_samemenu)                               # wait for the screen to update
        screen = ss.screenGrab((0, 0, 0, 0))                               # get the updated screen
##        print('increment_max_cord color: ' + str(screen.getpixel(gd.increment_max_cord)))
    print('increment button is set to max')

def manualRunBusinesses():
    screen = ss.screenGrab((0, 0, 0, 0)) # get the current state of the screen
    
    for cur_business in gd.businessList:
        if screen.getpixel(cur_business.cord_run) == cur_business.color_idle:
            print('manually running ' + cur_business.name)
            ms.clickPos(cur_business.cord_run)
            time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.lemonaide.cord_run) == gd.lemonaide.color_idle:
    #     print('manually running lemonaid')
    #     ms.setMousePos(gd.lemonaide.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.newspaper.cord_run) == gd.newspaper.color_idle:
    #     print('manually running newspaper')
    #     ms.setMousePos(gd.newspaper.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.car.cord_run) == gd.car.color_idle:
    #     print('manually running car')
    #     ms.setMousePos(gd.car.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.pizza.cord_run) == gd.pizza.color_idle:
    #     print('manually running pizza')
    #     ms.setMousePos(gd.pizza.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.donut.cord_run) == gd.donut.color_idle:
    #     print('manually running donut')
    #     ms.setMousePos(gd.donut.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.shrimp.cord_run) == gd.shrimp.color_idle:
    #     print('manually running shrimp')
    #     ms.setMousePos(gd.shrimp.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.hockey.cord_run) == gd.hockey.color_idle:
    #     print('manually running hockey')
    #     ms.setMousePos(gd.hockey.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.movie.cord_run) == gd.movie.color_idle:
    #     print('manually running movie')
    #     ms.setMousePos(gd.movie.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.bank.cord_run) == gd.bank.color_idle:
    #     print('manually running bank')
    #     ms.setMousePos(gd.bank.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

    # if screen.getpixel(gd.oil.cord_run) == gd.oil.color_idle:
    #     print('manually running oil')
    #     ms.setMousePos(gd.oil.cord_run)
    #     ms.leftClick()
    #     time.sleep(sleep_samemenu)

def closePopup():
    ms.clickPos(gd.popup_insider_cord_exit) # verified insider will draw over hot
    time.sleep(sleep_newmenu)
    ms.clickPos(gd.popup_hot_cord_exit)     # UNVERIFIED if hot will draw over moon
    time.sleep(sleep_newmenu)
    ms.clickPos(gd.popup_moon_cord_exit)    # UNVERIFIED if moon will draw over hot or insider
    time.sleep(sleep_newmenu)

def runLoop():
    setBuyMax()
    ms.leftClick() #----------------------TEMP. SET TO BUY X1
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