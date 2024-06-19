import cv2
import numpy as np
'''
img = cv2.imread('free-nature-images.jpg')
 
if img is None:
 sys.exit("Could not read the image.")

cv2.imshow("Display window", img)
k = cv2.waitKey(0)

if k == ord("s"):
 cv2.imwrite("free-nature-images.jpg", img)
'''

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Could not access camera")
    exit()
while True:
    ret,frame= capture.read()
    if not ret:
        print("Frame not recieved.")
        break
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
# work from videos to start with then just capture in real time
# try doing this on another computer (not school affiliated to see if it is a network privelidges thring)


'''

training
haar cascade
https://medium.com/@abuabdul4dev/introduction-to-object-detection-algorithms-5a54e358b0b8
https://www.v7labs.com/blog/yolo-object-detection
https://www.v7labs.com/blog/recurrent-neural-networks-guide
https://arxiv.org/abs/1512.02325
use rcnn or yolo
Steps:
1. Start taking a video
2. Object detect everything in image

# decide if i want to do the ml thing and draw boxes or just say it
3. Draw a rectangle of a corresponding colour for each object w label
4. Print the matching shape name and draw a rectangle eclusively around matching objects in same colour


'''
