import cv2
import matplotlib.pyplot as plt
import cvlib as cv


#Test Images:
# 'couple.jpeg'
# 'test1.jpg'
# 'test2.jpg'


image_path = 'test2.jpg'

#reading in the image
im = cv2.imread(image_path)


faces, confidences = cv.detect_face(im)

#iterating through all the detected faces and drawing the bounding boxes
for face in faces:
    (startX,startY) = face[0],face[1]
    (endX,endY) = face[2],face[3]
    # draw rectangle over face
    cv2.rectangle(im, (startX,startY), (endX,endY), (0,255,0), 2)


plt.imshow(im)
plt.show()