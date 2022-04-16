import cv2
import matplotlib.pyplot as plt
import keras.optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import os
import numpy as np

img = cv2.imread('happy_girl_2.jpg', 0) #TEST IMAGE 1
img_2 = cv2.imread('angry_boy.jpg'.0) #TEST IMAGE 2
img_3 = cv2.imread('surprised_boy.jpg', 0) #TEST IMAGE 3
img_4 = cv2.imread('sad_girl.jpg', 0) #TEST IMAGE 4

######### IF MODEL EXISTS ONCE SAVE FILE MADE

model = load_model('model_file_15epochs.hs')

#################### MODEL TESTING WITH EACH IMAGE
def test1():
    resized = cv2.resize(img, (48,48))
    normalize = resized/255.0
    reshape = np.reshape(normalize, (1, 48, 48, 1))
    result = model.predict(reshape)
    label = np.argmax(result, axis=1)[0]
    assert result == "happy"
    print(result)
    print(label)

def test2():
    img = img_2
    resized = cv2.resize(img, (48,48))
    normalize = resized/255.0
    reshape = np.reshape(normalize, (1, 48, 48, 1))
    result = model.predict(reshape)
    label = np.argmax(result, axis=1)[0]
    assert result == "angry"
    print(result)
    print(label)
    
def test3():
    img = img_3
    resized = cv2.resize(img, (48,48))
    normalize = resized/255.0
    reshape = np.reshape(normalize, (1, 48, 48, 1))
    result = model.predict(reshape)
    label = np.argmax(result, axis=1)[0]
    assert result == "surprised"
    print(result)
    print(label)

def test4():
    img = img_4
    resized = cv2.resize(img, (48,48))
    normalize = resized/255.0
    reshape = np.reshape(normalize, (1, 48, 48, 1))
    result = model.predict(reshape)
    label = np.argmax(result, axis=1)[0]
    assert result == "sad"
    print(result)
    print(label)

