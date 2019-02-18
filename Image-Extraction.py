import cv2
import math

videoFile = "E:/Purdue-University/Thesis/DeepLearningforNaturalDisasters/Video-Image-Extraction/Video1/"
imagesFolder = "E:/Purdue-University/Thesis/DeepLearningforNaturalDisasters/Video-Image-Extraction/Video1/"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imagesFolder +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print "Done!"
