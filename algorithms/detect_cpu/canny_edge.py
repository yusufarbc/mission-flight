import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

def autoCanny(blur, sigma=0.33):
    median = np.median(blur)
    lower=int(max(0,(1.0-sigma)*median))
    upper=int(min(255,(1.0-sigma)*median))
    canny=cv.Canny(blur,lower,upper)
    return canny

while True:
    ret,capture =cam.read()
    gray = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(3,3),0)    
    canny = autoCanny(blur)
    cv.imshow('Original',capture)
    cv.imshow('canny',canny) 
 
    if cv.waitKey(30)==27:
        break

    
cam.release()
 
cv.destroyAllWindows()