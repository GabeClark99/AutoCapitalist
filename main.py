"""
Gabriel Clark
August 2021
Window Resolution: 1920x1080 native, 1600x900 window

TODO:
test new version of ga.manualRunBusinesses() actually runs businesses

investor reset
-test post-investor-reset menu close
-buy angel upgrades and angel managers after investor reset

detect whether or not the upgrades quick buy icon exists

change planets

move over to ms.clickPos()

OCR for game data
-get businesses revenue_current
-calculate revenue per second (rps)

add more game data
-angel upgrades confirm menu coordinates and colors
-earth revenue upgrades # this is only needed if you calculate revenue based on revenue_initial. you can just OCR the current revenue per cycle
-moon businesses
-mars businesses

buy megabucks

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
import mousestuff as ms
import time


def main():
    
    # ga.buyBusinesses()
    #buyCashManagers()
    #buyCashUpgrades()
    #setBuyMax()
    # ga.manualRunBusinesses()
    # pass
    ga.runLoop()
    # getBusinessCount(gd.newspaper)
    # screen = screenGrab((0, 0, 0, 0))
    # print(str(screen.getpixel(gd.investors.cord_buy)))

    # gd.setBusinessesCount()
    # gd.setTimeMultipliers()

    # ss.popupCheck()

    # ga.openMenu("investors")
    # ga.buyManagers()
    # ga.investorReset()
    # ss.popupCheck()


if __name__ == '__main__':
    main()