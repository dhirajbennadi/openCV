import cv2 as cv
import argparse
from time import sleep

def drawOnImage(frame, width, height):
    #cv.namedWindow("EMVIA A1 Q5 Window 1", cv.WINDOW_AUTOSIZE)
    cv.imshow('EMVIA A1 Q5 Window 1' , frame)
    borderoutput = cv.copyMakeBorder(frame, 4, 4, 4, 4, cv.BORDER_CONSTANT, value=[255, 0, 0])
    #cv.imwrite(frame,borderoutput)
    newWidth = int( width // 2)
    newHeight = int(height // 2)
    #print("Width = {} Height = {}".format(newWidth, newHeight))
    cv.drawMarker(borderoutput, (newWidth, newHeight), (0,255,255), cv.MARKER_CROSS , 1, 1, 1)
    
    newImage = cv.resize(borderoutput, (320,240))
    cv.imshow('EMVIA A1 Q5 Window 2' , newImage)
    #cv.imshow('EMVIA A1 Q5 Window 2' , frame)

parser = argparse.ArgumentParser(description='EMVIA Assignment 1 Q5')

parser.add_argument('--camera' , help='Camera Device Number', type=int, default=0)

args = parser.parse_args()

cameraDeviceNumber = args.camera

cap = cv.VideoCapture(cameraDeviceNumber)
#cv.namedWindow("EMVIA A1 Q5", cv.WINDOW_AUTOSIZE)

while True:
    ret, frame = cap.read()
    width  = cap.get(3)   # float `width`
    height = cap.get(4)  # float `height`
    #print("Width = {} Height = {}".format(width,height))
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    drawOnImage(frame, width, height)
    
    #cap.set(3,320)
    #cap.set(4,240)
    #cv.imshow('EMVIA A1 Q5 Window 1' , frame)
    
    #cv.imshow('EMVIA A1 Q5' , frame)
    if cv.waitKey(10) == ord('q'):
        break
    #sleep(1)