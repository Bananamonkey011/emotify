from flask import Flask, render_template, Response
import cv2
import numpy as np
import cvlib as cv


app=Flask(__name__)
video_capture = cv2.VideoCapture(0)
# Load a sample picture and learn how to recognize it.
# 

#method to start the live video feed
def gen_frames():  
    while True:
        #reading the frame and a success bool from the video capture
        success, frame = video_capture.read()
        if not success:
            break
        else:
            # Run facial detection on the current frame
            faces, confidences = cv.detect_face(frame)
            # Iterating through all the detected faces
            for face in faces:
                (startX,startY) = face[0],face[1]
                (endX,endY) = face[2],face[3]

                distX = abs(startX-endX)
                distY = abs(startY-endY)

                diff = abs(distX-distY)


                if distX > distY:
                    startY -= diff//2
                    endY += diff//2
                else:
                    startX -= diff//2
                    endX += diff//2

                # draw rectangle over face
                cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)

            #cropping just the face out of the frame
            face = frame[startX: endX, startY: endY]

            #
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#default route when the landing page is opened
@app.route('/')
def index():
    return "<p>Hello, World!</p>"

#go to /video_feed in the url to get to the live video face detection page.
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__=='__main__':
    app.run(debug=True)