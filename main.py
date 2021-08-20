"""
Gabriel Clark
August 2021
Window Resolution: 1920x1080 native, 1600x900 window

TODO:
OCR for game data
-get businesses count
--gameactions.setBusinessesCount()
--calculate time_current from count
-get buninesses revenue_current

-calculate cash per second
--get cash per cycle
--calculate speed from number of this business as well as total businesses

add more game data
-earth revenue upgrades
-earth time upgrades
-moon businesses

check for and close popups, like events and deals
angel reset on earth
only buy angel upgrades and managers after angel reset
change planets

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
import gamedata as gd
import gameactions as ga
import time


def main():
    
    #buyBusinesses()
    #buyManagers()
    #buyCashUpgrades()
    #setBuyMax()
    #manualRunBusinesses()
    #pass
    # ga.runLoop()
    # getBusinessCount(gd.newspaper)
    ga.setBusinessesCount()

if __name__ == '__main__':
    main()