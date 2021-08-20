import PIL
from PIL import ImageGrab
import os
import time
import cv2
import pytesseract
import numpy

import gamedata as gd
import gameactions as ga

# Global Vars
# -------------------------------
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# -------------------------------

# dumb stupid workaround because python doesn't have function overloading:
# if you want to capture the entire screen, give these bbox coordinates: (0, 0, 0, 0)
# normally it wouldn't even capture a single pixel, but there is a catch for this case
# to print the entire screen instead
def screenGrab(bbox):
##    time.sleep(3)             #
    if bbox == (0, 0, 0, 0):        # if there was no bounding box given...
        image = ImageGrab.grab()        # grab the entire screen
    else:                               # if there was a bounding box given...
        image = ImageGrab.grab(bbox)    # grab the bounding box

    # image.save(os.getcwd() + '\\images\\screen_' + str(int(time.time())) + '.png', 'PNG')         #
    return image

# WARNING: DOES NOT DO WELL WITH READING ONLY SIGNLE-DIGITS!!!
def bboxToText(bbox):
    # imagePath = os.getcwd() + '\\images\\test.png'            #
    # cv2Image = cv2.imread(imagePath)                  #
    rgbImage = screenGrab(bbox).convert('RGB')  # grab the PIL image and convert it to RGB
    cv2Image = numpy.array(rgbImage)            # convert the RGB image to numpy array so cv2 can read it

    grayImage = cv2.cvtColor(cv2Image, cv2.COLOR_RGB2GRAY)
    # cv2.imwrite('_grayImage.png', grayImage)          #
    grayImage, binaryImage = cv2.threshold(grayImage, 180, 255, cv2.THRESH_BINARY) # guide said to use "cv2.THRESH_BINARY | cv2.THRESH_OTSU", but it was ruining everything
    invertedBinaryImage = cv2.bitwise_not(binaryImage)
    # cv2.imwrite('_invertedBinaryImage.png', invertedBinaryImage)          #

    kernel = numpy.ones((2,1), numpy.uint8)
    erodedImage = cv2.erode(invertedBinaryImage, kernel, iterations=1)
    dilatedImage = cv2.dilate(erodedImage, kernel, iterations=1)
    # cv2.imwrite('_dilatedImage.png', dilatedImage)           #

    outstring = pytesseract.image_to_string(dilatedImage) #pytesseract.image_to_string(dilatedImage)
    # print('text: ' + outstring)           #
    return outstring

def getBusinessCount(business: gd.Business):
    bbox = business.count_bbox
    count_str = bboxToText(bbox)
    # print('count_str: ' + count_str)    #

# will also trigger on any menu being open
# should only call this function when all menus are closed
def popupCheck():
    screen = screenGrab((0,0,0,0))
    if screen.getpixel(gd.popupcheck_cord) != gd.popupcheck_color_nopopup:
        ga.closePopup()

