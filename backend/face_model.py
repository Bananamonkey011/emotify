import cv2
import base64
import matplotlib.pyplot as plt
from deepface import DeepFace #pip install DeepFace


#"/9j/4AAQSkZJRgABAQAAAQABAAD/4gIoSUNDX1BST0ZJTEUAAQEAAAIYAAAAAAQwAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAAHRyWFlaAAABZAAAABRnWFlaAAABeAAAABRiWFlaAAABjAAAABRyVFJDAAABoAAAAChnVFJDAAABoAAAAChiVFJDAAABoAAAACh3dHB0AAAByAAAABRjcHJ0AAAB3AAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAFgAAAAcAHMAUgBHAEIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhZWiAAAAAAAABvogAAOPUAAAOQWFlaIAAAAAAAAGKZAAC3hQAAGNpYWVogAAAAAAAAJKAAAA+EAAC2z3BhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABYWVogAAAAAAAA9tYAAQAAAADTLW1sdWMAAAAAAAAAAQAAAAxlblVTAAAAIAAAABwARwBvAG8AZwBsAGUAIABJAG4AYwAuACAAMgAwADEANv/bAEMAQy4yOjIqQzo2OktHQ09kpmxkXFxkzJKaeabx1P767dTp5f//////////5en////////////////////////////bAEMBR0tLZFdkxGxsxP//6f/////////////////////////////////////////////////////////////////////AABEIAa8B2wMBIgACEQEDEQH/xAAZAAEBAQEBAQAAAAAAAAAAAAAAAQIDBAX/xAAwEAEBAAIBAwMEAQMDBAMAAAAAAQIRAxIhMUFRYQQiMnGBEzNCI1KhFGKCkURy8P/EABcBAQEBAQAAAAAAAAAAAAAAAAABAgP/xAAYEQEBAQEBAAAAAAAAAAAAAAAAARFBMf/aAAwDAQACEQMRAD8A9uzbGzbDWN7Ns7Ng1s2zs2DWzbOzYNbNs7Ng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"


def readEmotion(imgSrc):
    
    
    firstComma = imgSrc.find(",")
    imgSrc = imgSrc[firstComma + 1:]

    print("Image src:")
    print(imgSrc)
        

    imagedata = base64.b64decode( imgSrc )
    print( "Image data:")
    print(imagedata )    
    



    filename = "input.jpg" 
    with open(filename, 'wb') as f:
        f.write(imagedata)

     

    # cv2.imshow("Image", img)

    #he he he hah clash royale time

    try:
        img = cv2.imread('input.jpg')
        prediction = DeepFace.analyze(img) # painfully slow on first run but very accurate
    except:
        return ("Neutral", "https://open.spotify.com/playlist/37i9dQZF1DXaqCgtv7ZR3L") 

    print(prediction['dominant_emotion'])

    if prediction['dominant_emotion'] == "angry" or prediction['dominant_emotion'] == "digust":
        return ("Angry", "https://open.spotify.com/playlist/71Xpaq3Hbpxz6w9yDmIsaH")
    elif prediction['dominant_emotion'] == "fear":
        return ("Fear", "https://open.spotify.com/playlist/19nbalrVKn6nltR7sI2AHR")
    elif prediction['dominant_emotion'] == "happy" or prediction['dominant_emotion'] == "surprise":
        return ("Happy", "https://open.spotify.com/playlist/1llkez7kiZtBeOw5UjFlJq")
    elif prediction['dominant_emotion'] == "sad":
        return ("Sad", "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1")
    elif prediction['dominant_emotion'] == "neutral": 
        return ("Neutral", "https://open.spotify.com/playlist/37i9dQZF1DXaqCgtv7ZR3L")
    else:
        return ("Default", "https://open.spotify.com/playlist/1llkez7kiZtBeOw5UjFlJq")