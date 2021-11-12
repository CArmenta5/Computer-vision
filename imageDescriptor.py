# import the necessary packages
from helpers import pyramid
from helpers import sliding_window
import time
import cv2

import numpy as np


#importing required libraries
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog

import matplotlib.pyplot as plt
import imutils

"""References for HOG descriptor """
# https://www.thepythoncode.com/article/hog-feature-extraction-in-python#:~:text=The%20Histogram%20of%20Oriented%20Gradients,image%20or%20region%20of%20interest.

def HOG(nameImg):
    img = imread(nameImg)

    resized_img = resize(img, (128*4, 64*4))

    fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                    	cells_per_block=(2, 2), visualize=True, multichannel=True)
    plt.imsave("resized_img.jpg", resized_img)
    plt.imsave("hog_image.jpg"+str(cont)+".jpg", hog_image, cmap="gray")
    listLoad.append(ImgMatrix2Vector(hog_image))

def ImgMatrix2Vector(image):
    arr = np.array(image)
    shape = arr.shape
    flat_arr = arr.ravel()
    vector = np.matrix(flat_arr)
    vector[:,::10] = 128
    arr2 = np.asarray(vector).reshape(shape)
    
    return arr2

listLoad = []
    
image = cv2.imread('img.jpg')
(winW, winH) = (128, 128)
cont = 0

"""References in Sliding pyramid window"""
# https://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/
for resized in pyramid(image, scale=1.5):
    for (x, y, window) in sliding_window(resized, stepSize=32, windowSize=(winW, winH)):
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        clone = resized.copy()
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        dd = image[y:y+winH,x:x+winH]
        cv2.imwrite("Window"+str(cont)+".jpg",dd)
        cv2.imshow("cropped", dd)
        HOG("Window"+str(cont)+".jpg")
        cv2.imshow("Window", clone)
        cv2.waitKey(1)
        time.sleep(0.025)
        cont+=1