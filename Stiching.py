import imutils
import cv2
import os

Video_Camara = 0


class Stiching():

    def __init__(self):
        print("Welcom :D")

    def canny(self, img_blur):                
        return  cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
   
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
            imgMask = cv2.bitwise_and(img,img,mask=self.canny(img_gaussian))
            
            cv2.imshow("Stiching edge detection on a binary mask ",imgMask)               
            
    
        cv2.destroyAllWindows()                
        return

if __name__ == "__main__":
    ed = Stiching()   
    ed.runVideo()
    
