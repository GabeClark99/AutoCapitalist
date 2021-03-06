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
    gd.businessList.reverse()
    for cur_business in gd.businessList:        # for every business, click on their buy button
        ms.clickPos(cur_business.cord_buy)
        time.sleep(sleep_samemenu)

def openMenu(menu_name):
    if menu_name == "upgrades":
        ms.clickPos(gd.upgrades.cord_open)      # click on the button to open the upgrades menu
        time.sleep(sleep_newmenu)               # wait for the screen to change
        screen = ss.screenGrab((0,0,0,0))       # grab a snap of the entire screen

        while (screen.getpixel(gd.upgrades.cord_buy) != gd.upgrades.color_buy_on and 
        screen.getpixel(gd.upgrades.cord_buy) != gd.upgrades.color_buy_off): # while the screen isn't fully loaded...
            print('-the upgrades screen hasn\'t loaded yet')        #-------------DEBUGGING
            time.sleep(sleep_newmenu)
            screen = ss.screenGrab((0, 0, 0, 0))
            # print('gd.upgrades.cord_buy color: ' + str(screen.getpixel(gd.upgrades.cord_buy)))
        print('-the upgrades screen has loaded')            #-------------DEBUGGING
        time.sleep(sleep_newmenu)

    elif menu_name == "managers":
        ms.clickPos(gd.managers.cord_open)
        time.sleep(sleep_newmenu)
        screen = ss.screenGrab((0,0,0,0))

        while (screen.getpixel(gd.managers.cord_buy) != gd.managers.color_buy_on and 
        screen.getpixel(gd.managers.cord_buy) != gd.managers.color_buy_off): # while the screen isn't fully loaded...
            print('-the managers screen hasn\'t loaded yet')            #------------------DEBUGGING
            time.sleep(sleep_newmenu)
            screen = ss.screenGrab((0, 0, 0, 0))
            # print('gd.managers.cord_buy color: ' + str(screen.getpixel(gd.managers.cord_buy)))   
        print('-the managers screen has loaded')            #-----------DEBUGGING
        time.sleep(sleep_newmenu)

    elif menu_name == "investors":
        ms.clickPos(gd.investors.cord_open)
        time.sleep(sleep_newmenu)
        screen = ss.screenGrab((0,0,0,0))

        while (screen.getpixel(gd.investors.cord_buy) != gd.investors.color_buy_on): # the on and off colors for investors are the same regardless of angels
            print('-the investors screen hasn\'t loaded yet')            #------------------DEBUGGING
            time.sleep(sleep_newmenu)
            screen = ss.screenGrab((0, 0, 0, 0))
            # print('gd.investors.cord_buy color color: ' + str(screen.getpixel(gd.investors.cord_buy)))   
        print('-the investors screen has loaded')            #-----------DEBUGGING
        time.sleep(sleep_newmenu)


    else:
        print("-----ERROR (ss.checkMenuOpen): INVALID MENU NAME-----")

def buyCashManagers():
    screen = ss.screenGrab((0,0,0,0))

##    print('ma_menu color: ' + str(screen.getpixel(gd.managers.cord_open)))   
    if screen.getpixel(gd.managers.cord_open) == gd.managers.color_open_on:      # if the managers menu icon is orange... 
        print('THERE ARE MANAGERS TO BUY')
        openMenu("managers")
        screen = ss.screenGrab((0,0,0,0))
        
        ms.setMousePos(gd.managers.cord_buy)                                    # hover over the manager buy icon
        print('managers.cord_buy color: ' + str(screen.getpixel(gd.managers.cord_buy)))     #-----------DEBUGGING
        while screen.getpixel(gd.managers.cord_buy) == gd.managers.color_buy_on:      # while the first cash manager in the list's buy icon is blue...
            ms.leftClick()                                             # click on the first cash manager in the list's buy icon
            print('-bought a cash manager!')
            time.sleep(sleep_samemenu)                              # wait for the screen to update
            screen = ss.screenGrab((0, 0, 0, 0))                                   # grab the new state of the screen, and repeat
##            print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy))) 
        print('-no more cash managers to buy')                       # now there are no more cash managers left to buy
        
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
        openMenu("upgrades")
        screen = ss.screenGrab((0,0,0,0))

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

# performs reset for angel investors
# buys angel managers
# buys angel upgrades TODO
def investorReset():
    screen = ss.screenGrab((0,0,0,0))

    if screen.getpixel(gd.investors.cord_open) == gd.investors.color_open_on:
        # --------------------------------------------------------
        # Reset game and recieve angels
        # --------------------------------------------------------
        openMenu("investors")

        ms.clickPos(gd.investors.cord_buy)          
        time.sleep(sleep_newmenu)

        ms.clickPos(gd.investors.cord_confirm_yes)
        time.sleep(5)       # the congratulations splash lasts a while
        
        ms.clickPos(gd.investors.cord_exit)     # go back to main menu
        time.sleep(sleep_newmenu)

        # --------------------------------------------------------
        # Buy angel managers
        # --------------------------------------------------------
        openMenu("managers")                    # open managers menu
        ms.clickPos(gd.managers.cord_submenu)   # open angel managers submenu
        time.sleep(sleep_newmenu)
        screen = ss.screenGrab((0, 0, 0, 0))                                       # grab the new state of the screen
        ms.setMousePos(gd.managers.cord_buy)
        # print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy))) 
        while screen.getpixel(gd.managers.cord_buy) == gd.managers.color_buy_on:      # while the first angel manager in the list's buy icon is blue...
            ms.leftClick()                                             # click on the first angel manager in the list's buy icon
            print('clicked an angel manager!')
            time.sleep(sleep_newmenu)                                   # wait for the screen to update, could possibly open new menu for confirm
            screen = ss.screenGrab((0, 0, 0, 0))                                   # grab the new state of the screen
            # print('ma_buy color: ' + str(screen.getpixel(gd.managers.cord_buy))) 

            # print('managers.cord_confirm_no color: ' + str(screen.getpixel(gd.managers.cord_confirm_no)))   
            if screen.getpixel(gd.managers.cord_confirm_no) == gd.managers.color_confirm_no:  # if the game asks us to confirm our purchase...
                ms.setMousePos(gd.managers.cord_confirm_no)                         # hover over the 'No' button
                ms.leftClick()                                                 # click on the 'No' button
                print('clicked no!')                #------------DEBUGGING
                break                                                       # stop purchasing angel managers
        print('no more angel managers to buy')                              # now there are no more angel managers left to buy
    
        ms.clickPos(gd.managers.cord_exit)
        time.sleep(sleep_newmenu)
        print('-exited the managers menu!')

        # --------------------------------------------------------
        # Buy angel upgrades
        # --------------------------------------------------------
        openMenu("upgrades")
        ms.clickPos(gd.upgrades.cord_submenu)   # open angel upgrades submenu
        time.sleep(sleep_newmenu)

        screen = ss.screenGrab((0, 0, 0, 0))                                       # grab the new state of the screen
        ms.setMousePos(gd.upgrades.cord_buy)
        while screen.getpixel(gd.upgrades.cord_buy) == gd.upgrades.color_buy_on:      # while the first angel manager in the list's buy icon is blue...
            ms.leftClick()                                             # click on the first angel manager in the list's buy icon
            print('clicked an angel upgrade!')
            time.sleep(sleep_newmenu)                                   # wait for the screen to update, could possibly open new menu for confirm
            screen = ss.screenGrab((0, 0, 0, 0))                                   # grab the new state of the screen

            # -----------------NEED TO GET CONFIRM MENU CORDS AND COLORS---------------
            if screen.getpixel(gd.upgrades.cord_confirm_no) == gd.upgrades.color_confirm_no:  # if the game asks us to confirm our purchase...
                ms.setMousePos(gd.upgrades.cord_confirm_no)                         # hover over the 'No' button
                ms.leftClick()                                                 # click on the 'No' button
                print('clicked no!')                #------------DEBUGGING
                break                                                       # stop purchasing angel upgrades
            print('no more angel upgrades to buy')                              # now there are no more angel upgrades left to buy

            ms.clickPos(gd.upgrades.cord_exit)
            time.sleep(sleep_newmenu)
            print('-exited the upgrades menu!')

def runLoop():
    setBuyMax()
    ms.leftClick() #----------------------TEMP. SET TO BUY X1
    x = 1
    while True:
        print('loop ' + str(x))
        ss.popupCheck()
        investorReset() # needs testing for closing menus and buying angel upgrades (angel managers should be good)
        manualRunBusinesses()
        buyCashUpgrades()
        buyCashManagers()
        buyBusinesses()
        x = x + 1
        if x % 200 == 0:
            print('SLEEPING FOR 1m')
            time.sleep(1*60)
# ---------------------------------------------------------