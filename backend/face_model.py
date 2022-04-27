import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace #pip install DeepFace

def readEmotion():
    img = cv2.imread('happy_girl.jpg') 
    cv2.imshow("Image", img)
    prediction = DeepFace.analyze(img) # painfully slow on first run but very accurate
    return prediction

