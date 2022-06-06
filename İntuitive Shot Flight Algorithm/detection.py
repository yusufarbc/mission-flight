import cv2
import numpy as np


class Detection():
    def __init__(self,uav,logger):
        self.min_red = np.array([158, 103, 55])
        self.max_red = np.array([180, 255, 255])
        self.control_flag = False
        self.uav = uav
        self.logger = logger
        self.target()

    def start(self):
        self.control_flag = True
        #self.control()

    def stop(self):
        self.control_flag = False
        cv2.imwrite("detection.png",self.frame)
        self.logger.log(f"targetX={self.targetX}, targetY={self.targetY}, targetWidth={self.targeWidth}, targetHeight={self.targetHeight}")
            
    def target(self):
        self.targetX = 0
        self.targetY = 0
        self.targeWidth = 0
        self.targetHeight = 0
        self.frame = []
        self.waypoint = 0
        #self.altitude = uav.getlocation
    
    def control(self):
        cap = cv2.VideoCapture(0)
        if (cap.isOpened()== False):
            print("Error opening video stream or file")
            self.logger.log("Error opening video stream or file")

        while(self.control_flag):
            ret, frame = cap.read()
            height, width = frame.shape[:2]

            start_row=int(height *.20)
            end_row=int(height*.80)

            frame=frame[start_row:end_row ,]
            x1, y1, x2, y2=self.detect(frame)
            print(f"x={x1}, y={y1}, w={x2-x1}, h={y2-y1}")
            self.logger.log(f"x={x1}, y={y1}, w={x2-x1}, h={y2-y1}")


            if((x2-x1)*(y2-y1)> (self.targetHeight*self.targeWidth)):
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0), 2)
                cv2.circle(frame, (x1+(x2-x1)//2, y1+(y2-y1)//2), 1, (0,255,0), 2)
                self.width = (x2-x1)
                self.height = (y2-y1)
                self.X = x1
                self.Y = y1
                self.frame = frame
                self.nextWP=self.uav.commands.next
                    
    def detect(self, image):
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_img, self.min_red, self.max_red)
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