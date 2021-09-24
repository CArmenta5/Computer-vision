import imutils
import cv2
import os
import numpy as np

Video_Camara = 0


class EdgeDetection():

    def __init__(self):
        print()
    def sobel(self, img_blur):
    
        x = cv2.Sobel(img_blur,cv2.CV_16S,1,0)  
        y = cv2.Sobel(img_blur,cv2.CV_16S,0,1)  
        absX = cv2.convertScaleAbs(x)   
        absY = cv2.convertScaleAbs(y)  
    
        return cv2.addWeighted(absX,0.5,absY,0.5,0)  
       
        print()
    def canny(self, img_blur):                
        return  cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
   
    def prewitt(self, img_blur):
        kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        img_prewittx = cv2.filter2D(img_blur, -1, kernelx)
        img_prewitty = cv2.filter2D(img_blur, -1, kernely)
        
        return img_prewittx + img_prewitty
   
    def runVideo(self):
        capWebcam = cv2.VideoCapture(Video_Camara)         
    
        if capWebcam.isOpened() == False:               
            print ("error: capWebcam not accessed successfully\n")      
            os.system("pause")                                          
            return                                                      
    
        while cv2.waitKey(1) != 27 and capWebcam.isOpened():        
            blnFrameReadSuccessfully, img = capWebcam.read()   
            img = imutils.resize(img, width = 300)   
    
            if not blnFrameReadSuccessfully or img is None:     
                print ("error: frame not read from webcam\n")            
                os.system("pause")                                      
                break                                                     
    
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
                
            cv2.imshow("Sobel Detection ", self.sobel(img_gaussian))               
            cv2.imshow("Canny Detection", self.canny(img_gaussian))               
            cv2.imshow("Prewitt Detection ", self.prewitt(img_gaussian))               

    
        cv2.destroyAllWindows()                
        return

if __name__ == "__main__":
    ed = EdgeDetection()   
    ed.runVideo()