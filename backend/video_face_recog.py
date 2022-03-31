import cv2
import matplotlib.pyplot as plt
import cvlib as cv

#live video feed
video_capture = cv2.VideoCapture(0)


while True:

    #fetching the current frame
    ret, frame = video_capture.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces, confidences = cv.detect_face(frame)

    for face in faces:
        (startX,startY) = face[0],face[1]
        (endX,endY) = face[2],face[3]
        # draw rectangle over face
        cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)

    #just the face (feed into NN)
    face = frame[startX: endX, startY: endY]

    #saving to a file    
    # cv2.imwrite( "./_0.png" , face)

    #show the current frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()