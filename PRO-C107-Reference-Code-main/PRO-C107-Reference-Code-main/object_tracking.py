import cv2 
import time
import math
goal1=530
goal2=300
video=cv2.VideoCapture('PRO-C107-Reference-Code-main/bb3.mp4')
tracker=cv2.TrackerCSRT_create()
ret,image=video.read()
bbox=cv2.selectROI('traking',image,False)
tracker.init(image,bbox)
def drawbox(image,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
def trackingobject(image,bbox):
       x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3]) 
       c1=x+int(w/2)
       c2=y+int(h/2)
       cv2.circle(image,(c1,c2),2,(255,0,0),3) 
       cv2.circle(image,(goal1,goal2),2,(255,0,0),3) 
       distance=math.sqrt(((c1-goal1)**2) + (c2-goal2)**2)
       if(distance<40):
        cv2.putText(image,"Goal achived",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)   
while True:
     ret,image=video.read()
     sucsess,bbox=tracker.update(image)
     if(sucsess==True):
        drawbox(image,bbox)
     trackingobject(image,bbox)
     cv2.imshow('resid',image)
     if(cv2.waitKey(1)==32):
        break