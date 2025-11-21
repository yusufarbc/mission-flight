import cv2
import numpy as np
from math import *

class circle_cv:
    def __init__(self, min_red, max_red, image):
        self.min_red = min_red
        self.max_red = max_red
        self.image = image
        
    def preprocess(self):
        hsv_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        
        return hsv_img
    
    def detect_circle(self, hsv_img):
        mask = cv2.inRange(hsv_img, self.min_red, self.max_red)
        
        return mask
    
    def mask_to_bbox(self, mask):
        mask = mask.astype(np.uint8)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        x = 0
        y = 0
        h = 0
        w = 0

        for contour in contours:
            tmp_x, tmp_y, tmp_w, tmp_h = cv2.boundingRect(contour)
            if tmp_w * tmp_h > w * h:
                x = tmp_x
                y = tmp_y
                w = tmp_w
                h = tmp_h

        return x, y, x+w, y+h

if __name__ == "__main__":
    frame = cv2.imread("hedef.png")
             
    min_red = np.array([158, 103, 55])
    max_red = np.array([180, 255, 255]) 
        
    detect_circle = circle_cv(min_red, max_red, frame)

    hsv_img = detect_circle.preprocess()
    mask = detect_circle.detect_circle(hsv_img)
    x1, y1, x2, y2 = detect_circle.mask_to_bbox(mask)
        
    #darienin merkezi
    x,y = x1+(x2-x1)//2, y1+(y2-y1)

    #görüntü matrisinin merkezi
    fx = 1296
    fy = 972

    #ihanın koordintları
    ihaX=0
    ihaY=0
    height = 5

    #görüş alanının hesaplanması
    X = 2*height*tan(26.75*(pi/180))
    Y = 2*height*tan(20.70*(pi/180))

    #oranların hesaplanması
    oranX = X / 2592
    oranY = Y / 1944

    #konum farklarının bulunması
    distanceX = x - fx 
    distanceY = y - fy

    #hedefin koordinatlarının hesaplanması
    targetX = ihaX + oranX*distanceX
    targetY = ihaY + oranY*distanceY

    print(targetX)
    print(targetY)
