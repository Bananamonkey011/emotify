from flask import Flask, render_template, Response
import cv2
import numpy as np
import cvlib as cv
from face_model import readEmotion

app=Flask(__name__)
video_capture = cv2.VideoCapture(0)
# Load a sample picture and learn how to recognize it.
# 

def gen_frames():  
    while True:
        success, frame = video_capture.read()  # read the camera frame
        if not success:
            break
        else:

            # Only process every other frame of video to save time
           
            faces, confidences = cv.detect_face(frame)


            # Find all the faces and face encodings in the current frame of video

            for face in faces:
                (startX,startY) = face[0],face[1]
                (endX,endY) = face[2],face[3]
                # draw rectangle over face
                cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)

            #just the face (feed into NN)
            face = frame[startX: endX, startY: endY]

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return "<p>Hello, World!</p>"
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/model')
def model():
    return readEmotion()


if __name__=='__main__':
    app.run(debug=True)
