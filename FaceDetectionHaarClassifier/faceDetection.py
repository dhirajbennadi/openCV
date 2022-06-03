from __future__ import print_function
import cv2 as cv
import argparse
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    count1 = 0
    count2 = 0
    for (x,y,w,h) in faces:
        count1 += 1
        #print('Face Rectangle {} {} {} {}'.format(x,y,w,h))
        center = (x + w//2, y + h//2)
        #print('Face Center {}'.format(center))
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        print('Eyes Count = {}'.format(len(eyes)))
        print('Eyes Values = {}'.format(eyes))
        for (x2,y2,w2,h2) in eyes:
            count2 += 1
            #print('Eye Rectangle {} {} {} {}'.format(x2,y2,w2,h2))
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
        #print('Face Count {} , Eye Count =  {}'.format(count1,count2))
    
    cv.imshow('Capture - Face detection', frame)
    

'''
How to pass input values
py .\faceDetection.py --face_cascade haarcascade_frontalface_alt.xml --eyes_cascade haarcascade_eye_tree_eyeglasses.xml --camera 0
'''

parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')


parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera Device number.', type=int, default=0)
#parser.add_argument('--dummy', help='Dummy Number.', type=int, default=0)
args = parser.parse_args()

face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

#print('Dummy Number {} '.format(args.dummy))

#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
    

while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    #cv.imshow(frame)
    if cv.waitKey(10) == ord('q'):
        break