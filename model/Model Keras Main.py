import cv2
import matplotlib.pyplot as plt
import keras.optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import os

img = cv2.imread("happy_girl") #TEST IMAGE

######### IF MODEL EXISTS ONCE SAVE FILE MADE

model = load_model(model_file_10epochs.hs)

#################### MODEL OUTPUTS RESULTS

result = model.predict(img)
label = np.argmax(result, axis=1)[0]
print(result)
print(label)
