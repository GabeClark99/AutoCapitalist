"""
Gabriel Clark
August 2021
Window Resolution: 1920x1080 native, 1600x900 window

TODO:
verify new version of ga.manualRunBusinesses() actually runs businesses
move over to ms.clickPos()

angel reset on earth
only buy angel upgrades and managers after angel reset
change planets

OCR for game data
-get buninesses revenue_current
-calculate revenue per second (rps)

add more game data
-earth revenue upgrades # this is only needed if you calculate revenue based on revenue_initial. you can just OCR the current revenue per cycle
-moon businesses
-mars businesses

buy businesses on moon
buy managers on moon
set buy max on moon
buy upgrades on moon
angel reset on moon

buy businesses on mars
buy managers on mars
set buy max on moon
buy upgrades on mars
angel reset on mars 
"""

from screenstuff import getBusinessCount, screenGrab
import screenstuff as ss
import gamedata as gd
import gameactions as ga
import time


def main():
    
    # ga.buyBusinesses()
    #buyManagers()
    #buyCashUpgrades()
    #setBuyMax()
    #manualRunBusinesses()
    # pass
    ga.runLoop()
    # getBusinessCount(gd.newspaper)
    # screen = screenGrab((0, 0, 0, 0))

    # gd.setBusinessesCount()
    # gd.setTimeMultipliers()

    # ss.popupCheck()
    

if __name__ == '__main__':
    main()