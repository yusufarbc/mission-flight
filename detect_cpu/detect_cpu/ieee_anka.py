import os
import cv2
import time
from cv2 import inRange
import numpy as np 


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
    cap = cv2.VideoCapture("ieee_anka.mp4")
    
    new_frame_time = 0
    prev_frame_time = 0
    
    
    if (cap.isOpened()== False):
        print("Error opening video stream or file")

    while(cap.isOpened()):
        ret, frame = cap.read()
        
        new_frame_time = time.time()
                
        min_red = np.array([158, 103, 55])
        max_red = np.array([180, 255, 255])
        
        
        detect_circle = circle_cv(min_red, max_red, frame)

        hsv_img = detect_circle.preprocess()
        mask = detect_circle.detect_circle(hsv_img)
        x1, y1, x2, y2 = detect_circle.mask_to_bbox(mask)
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0), 2)
        cv2.circle(frame, (x1+(x2-x1)//2, y1+(y2-y1)//2), 1, (0,255,0), 2)
        
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        
        cv2.putText(frame, "FPS: {:.3f}".format(fps), (15, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)
         
        if ret == True:
            cv2.imshow('Ieee_anka',frame)
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
                
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
