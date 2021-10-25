# Imports
import cv2 
import matplotlib.pyplot as plt
import numpy as np
import imutils
import os

Video_Camara = 0

# Credits of A-Kaze Algorithm https://stackoverflow.com/questions/62581171/how-to-implement-kaze-and-a-kaze-using-python-and-opencv

# Open and convert the input and training-set image from BGR to GRAYSCALE
image1 = cv2.imread('image3.png')
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

capWebcam = cv2.VideoCapture(Video_Camara)         

if capWebcam.isOpened() == False:               
    print ("error: capWebcam not accessed successfully\n")      
    os.system("pause")                                          

while cv2.waitKey(1) != 27 and capWebcam.isOpened():       
    
    blnFrameReadSuccessfully, image2 = capWebcam.read()   
    
    image2 = imutils.resize(image2, width = 300)   
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    if not blnFrameReadSuccessfully or image2 is None:     
        print ("error: frame not read from webcam\n")            
        os.system("pause")                                      
        break            
    #cv2.imshow("Actual Input", image1)               

    #cv2.imshow("Actual Input2", image2)               

    # Initiate A-KAZE descriptor
    AKAZE = cv2.AKAZE_create()
    
    # Find the keypoints and compute the descriptors for input and training-set image
    keypoints1, descriptors1 = AKAZE.detectAndCompute(image1, None)
    keypoints2, descriptors2 = AKAZE.detectAndCompute(image2, None)
    
    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    
    index_params = dict(algorithm = FLANN_INDEX_KDTREE,
                        trees = 5)
    
    search_params = dict(checks = 50)
    
    # Convert to float32
    descriptors1 = np.float32(descriptors1)
    descriptors2 = np.float32(descriptors2)
    
    # Create FLANN object
    FLANN = cv2.FlannBasedMatcher(indexParams = index_params,
                                 searchParams = search_params)
    
    # Matching descriptor vectors using FLANN Matcher
    matches = FLANN.knnMatch(queryDescriptors = descriptors1,
                             trainDescriptors = descriptors2,
                             k = 2)
    
    # Lowe's ratio test
    ratio_thresh = 0.6
    
    # "Good" matches
    good_matches = []
    
    # Filter matches
    for m, n in matches:
        if m.distance < ratio_thresh * n.distance:
            good_matches.append(m)
    
    # Draw only "good" matches
    output = cv2.drawMatches(img1 = image1,
                            keypoints1 = keypoints1,
                            img2 = image2,
                            keypoints2 = keypoints2,
                            matches1to2 = good_matches,
                            outImg = None,
                            flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    plt.imshow(output)
    plt.show()          



cv2.destroyAllWindows()                


