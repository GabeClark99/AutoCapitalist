import os
import time
import win32api, win32con

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