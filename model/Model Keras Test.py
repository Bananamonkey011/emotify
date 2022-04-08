import cv2
import matplotlib.pyplot as plt
import keras.optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import os

img = cv2.imread("happy_girl") #TEST IMAGE 1
img_2 = cv2.imread("angry_boy") #TEST IMAGE 2
img_3 = cv2.imread("surprised_boy") #TEST IMAGE 3
img_4 = cv2.imread("sad_girl") #TEST IMAGE 4
img_5 = cv2.imread("melancholy_girl") #TEST IMAGE 5

######### IF MODEL EXISTS ONCE SAVE FILE MADE

model = load_model(model_file_10epochs.hs)

#################### MODEL TESTING WITH EACH IMAGE
def test1():
    result = model.predict(img)
    label = np.argmax(result, axis=1)[0]
    assert result == "happy"
    print(result)
    print(label)

def test2():
    result = model.predict(img_2)
    label = np.argmax(result, axis=1)[0]
    assert result == "angry"
    print(result)
    print(label)
    
def test3():
    result = model.predict(img_3)
    label = np.argmax(result, axis=1)[0]
    assert result == "surprised"
    print(result)
    print(label)

def test4():
    result = model.predict(img_3)
    label = np.argmax(result, axis=1)[0]
    assert result == "sad"
    print(result)
    print(label)

def test5():
    result = model.predict(img_3)
    label = np.argmax(result, axis=1)[0]
    assert result == "sad"
    print(result)
    print(label)
