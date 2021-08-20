import PIL
from PIL import ImageGrab
import os
import time
import cv2
import pytesseract
import numpy

import gamedata as gd

# Global Vars
# -------------------------------
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# -------------------------------

# dumb stupid workaround because python doesn't have function overloading:
# if you want to capture the entire screen, give these bbox coordinates: (0, 0, 0, 0)
# normally it wouldn't even capture a single pixel, but there is a catch for this case
# to print the entire screen instead
def screenGrab(bbox):
##    time.sleep(3) # ------------------------DEBUGGING
    if bbox == (0, 0, 0, 0):        # if there was no bounding box given...
        image = ImageGrab.grab()        # grab the entire screen
    else:                               # if there was a bounding box given...
        image = ImageGrab.grab(bbox)    # grab the bounding box

    image.save(os.getcwd() + '\\images\\screen_' + str(int(time.time())) + '.png', 'PNG') #-------------------DEBUGGING
    return image

    
def bboxToText(bbox):
    # image = cv2.imread(imagePath)
    rgbImage = screenGrab(bbox).convert('RGB')  # grab the PIL image and convert it to RGB
    cv2Image = numpy.array(rgbImage)            # convert the RGB image to numpy array so cv2 can read it

    grayImage = cv2.cvtColor(cv2Image, cv2.COLOR_RGB2GRAY)
    grayImage, binaryImage = cv2.threshold(grayImage, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    invertedBinaryImage = cv2.bitwise_not(binaryImage)
##    cv2.imshow('image', invertedBinaryImage)    

    kernel = numpy.ones((2,1), numpy.uint8)
    erodedImage = cv2.erode(invertedBinaryImage, kernel, iterations=1)
    dilatedImage = cv2.dilate(erodedImage, kernel, iterations=1)

    outstring = pytesseract.image_to_string(dilatedImage)
    print('text: ' + outstring)

def getBusinessCount(business: gd.Business):
    bbox = business.count_bbox
    count_image = screenGrab(bbox)
