import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace #pip install DeepFace
img = cv2.imread('happy_girl.jpg') 

cv2.imshow("Image", img)




prediction = DeepFace.analyze(img) # painfully slow on first run but very accurate
print(prediction['dominant_emotion'])

if prediction['dominant_emotion'] == "angry" or prediction['dominant_emotion'] == "digust":
    print("https://open.spotify.com/playlist/71Xpaq3Hbpxz6w9yDmIsaH")
elif prediction['dominant_emotion'] == "fear":
    print("https://open.spotify.com/playlist/19nbalrVKn6nltR7sI2AHR")
elif prediction['dominant_emotion'] == "happy" or prediction['dominant_emotion'] == "surprise":
    print("https://open.spotify.com/playlist/1llkez7kiZtBeOw5UjFlJq")
elif prediction['dominant_emotion'] == "sad":
    print("https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1")
elif prediction['dominant_emotion'] == "neutral": 
    print("https://open.spotify.com/playlist/37i9dQZF1DXaqCgtv7ZR3L")
else:
    print("https://open.spotify.com/playlist/1llkez7kiZtBeOw5UjFlJq")
