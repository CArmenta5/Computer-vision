import imutils
import cv2
import os
import numpy as np

#references https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv

Video_Camara = 0


class SegmentRGB():

    def __init__(self):
        print()
        
    def segmentRedMask(self, hsv):
        # lower boundary RED color range values; Hue (0 - 10) 
        l_r1 = np.array([0, 100, 20])
        u_r1 = np.array([10, 255, 255])
        # upper boundary RED color range values; Hue (160 - 180)
        l_r2 = np.array([160,100,20])
        u_r2 = np.array([179,255,255])
        
        l_maskR = cv2.inRange(hsv, l_r1, u_r1)
        u_maskR = cv2.inRange(hsv, l_r2, u_r2)
        
        return l_maskR + u_maskR;
       
    def segmentGreenMask(self, hsv):     
        l_g = np.array([45 , 50, 71])
        u_g = np.array([75, 255, 255])
                   
        return cv2.inRange(hsv, l_g, u_g)
   
    def segmentBlueMask(self, hsv):
        l_b = np.array([100,50,50])
        u_b = np.array([130,255,255])

        return cv2.inRange(hsv, l_b, u_b)

   
    def runVideo(self):
        capWebcam = cv2.VideoCapture(Video_Camara)         
    
        if capWebcam.isOpened() == False:               
            print ("error: capWebcam not accessed successfully\n")      
            os.system("pause")                                          
            return                                                      
    
        while cv2.waitKey(1) != 27 and capWebcam.isOpened():        
            blnFrameReadSuccessfully, image = capWebcam.read()   
            
            image = imutils.resize(image, width = 300)   
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            if not blnFrameReadSuccessfully or image is None:     
                print ("error: frame not read from webcam\n")            
                os.system("pause")                                      
                break            
                   
            kernel = np.ones((5,5), np.uint8)
            
                      
            resR = cv2.bitwise_and(image, image, mask = self.segmentRedMask(hsv))
            img_erosionR = cv2.dilate(resR, kernel, iterations=1)
            closingR = cv2.erode(img_erosionR, kernel, iterations=1)
            
            resG = cv2.bitwise_and(image, image, mask = self.segmentGreenMask(hsv))
            img_erosionG = cv2.dilate(resG, kernel, iterations=1)
            closingG = cv2.erode(img_erosionG, kernel, iterations=1)
            
            resB = cv2.bitwise_and(image, image, mask = self.segmentBlueMask(hsv))
            img_erosionB = cv2.dilate(resB, kernel, iterations=1)
            closingB = cv2.erode(img_erosionB, kernel, iterations=1)
    
            cv2.imshow("Actual Input", image)               
            cv2.imshow("Segment Red", closingR)               
            cv2.imshow("Segment Green", closingG)               
            cv2.imshow("Segment Blue", closingB)               
    
        cv2.destroyAllWindows()                
        return

if __name__ == "__main__":
    ed = SegmentRGB()   
    ed.runVideo()







