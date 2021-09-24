import imutils
import cv2
import os

Video_Camara = 0

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox ,QWidget, QVBoxLayout, QSlider)


class Window(QWidget):
    varAlpha = 1.5
  # Contrast control (1.0-3.0)
    varBeta = 0
 # Brightness control (0-100)
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        grid = QGridLayout()
        grid.addWidget(self.slideAlpha("Brightness"))
        grid.addWidget(self.slideBeta("Contrast"))
        self.setLayout(grid)
        self.setWindowTitle("Image Controlers")
        self.resize(400, 150)
        
    def slideAlpha(self, name):
        groupBox = QGroupBox(name)
        
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)
        slider.setRange(0, 30)
        slider.setSingleStep(1) #slider can slider

        slider.valueChanged.connect(self.changeValueAlpha)           

        vbox = QVBoxLayout()
        vbox.addWidget(slider)
        groupBox.setLayout(vbox)

        return groupBox
    
    def slideBeta(self, name):
        groupBox = QGroupBox(name)
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setRange(-127, 127)
        slider.setSingleStep(1) #slider can slider
        slider.valueChanged.connect(self.changeValueBeta)     
        
        vbox = QVBoxLayout()
        vbox.addWidget(slider)
        groupBox.setLayout(vbox)
        
        return groupBox
    
    def changeValueAlpha(self, value):
        print(self.varAlpha )
        self.varAlpha = round(value,2)
        
    def changeValueBeta(self, value):
        print(self.varBeta)
        self.varBeta = value
          
    def runVideo(self):
        capWebcam = cv2.VideoCapture(Video_Camara)         
    
        if capWebcam.isOpened() == False:               
            print ("error: capWebcam not accessed successfully\n")      
            os.system("pause")                                          
            return                                                      
    
        while cv2.waitKey(1) != 27 and capWebcam.isOpened():           
            blnFrameReadSuccessfully, imgOriginal = capWebcam.read()   
    
            imgOriginal = imutils.resize(imgOriginal, width = 300)   
    
            if not blnFrameReadSuccessfully or imgOriginal is None:     
                print ("error: frame not read from webcam\n")            
                os.system("pause")                                      
                break                                                     

            adjusted  = cv2.convertScaleAbs(imgOriginal,alpha = self.varAlpha, beta = self.varBeta)
            
            cv2.imshow("IMAGEN ORIGINAL", imgOriginal)               
            cv2.imshow("Adjusted", adjusted )       
    
        cv2.destroyAllWindows()                
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    clock.runVideo()
    
    sys.exit(app.exec_())
   
