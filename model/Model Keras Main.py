import cv2
import matplotlib.pyplot as plt
import keras.optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import os
import numpy as np

img = cv2.imread('surprised_boy.jpg',0) #TEST IMAGE
resized = cv2.resize(img, (48,48))
normalize = resized/255.0
reshape = np.reshape(normalize, (1, 48, 48, 1))

######### IF MODEL EXISTS ONCE SAVE FILE MADE

model = load_model("model_file_1epochs.h5")

#################### MODEL OUTPUTS RESULTS
labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

result = model.predict(reshape)
print(result)

mval = -10000
ci = 0
mi= -10000

for i in result[0]:
    if i > mval:
        mval = i
        mi = ci
    ci = ci + 1

print(labels[mi])
