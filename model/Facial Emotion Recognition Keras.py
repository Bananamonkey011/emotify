import cv2
import matplotlib.pyplot as plt
import keras.optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import numpy as np
import os


########## DIRECTORY FOR DATA && SEPARATION OF TRAIN AND TEST DATA

train_dir = os.path.join(os.getcwd(), "FER_Data", "train")
test_dir = os.path.join(os.getcwd(), "FER_Data", "test")

train_data_gen = ImageDataGenerator(rescale = 1./255,
                                    rotation_range = 30,
                                    shear_range = 0.3,
                                    zoom_range = 0.3,
                                    horizontal_flip = True,
                                    fill_mode = 'nearest')

test_data_gen = ImageDataGenerator(rescale = 1./255)

train_gen = train_data_gen.flow_from_directory(train_dir,
                                                    color_mode='grayscale',
                                                    target_size = (48,48),
                                                    batch_size=32,
                                                    class_mode='categorical',
                                                    shuffle=True)

test_gen = train_data_gen.flow_from_directory(test_dir,
                                                    color_mode='grayscale',
                                                    target_size = (48,48),
                                                    batch_size=32,
                                                    class_mode='categorical',
                                                    shuffle=True)

class_labels=['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

img, label = train_gen.__next__()


################### MODEL CREATION

model = Sequential()

model.add(Conv2D(32, kernel_size=(3,3), activation = 'relu', input_shape = (48,48,1)))
model.add(Conv2D(64, kernel_size=(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))

# model.add(Conv2D(64, kernel_size=(3,3), activation = 'relu'))
# model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Dropout(0.1))

model.add(Conv2D(128, kernel_size=(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))

model.add(Conv2D(256, kernel_size=(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))

model.add(Flatten())
model.add(Dense(512, activation = 'relu'))
model.add(Dropout(0.2))

model.add(Dense(7, kernel_initializer='uniform', activation = 'softmax'))

opt = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer = opt, loss = 'categorical_crossentropy', metrics = ['accuracy'])

#print(model.summary())
#################### TRAINING MODEL

num_epochs = 15 #IDEALLY 100
num_train_img = 0
num_test_img = 0

for root,dir,files in os.walk(train_dir):
    num_train_img += len(files)

for root,dir,files in os.walk(test_dir):
    num_test_img += len(files)

history = model.fit(train_gen,
                    steps_per_epoch = num_train_img//32,
                    epochs=num_epochs,
                    validation_data = test_gen,
                    validation_steps = num_test_img//32)

model.save(os.path.join(os.getcwd(),"model_file_1epochs.h5"))



          
