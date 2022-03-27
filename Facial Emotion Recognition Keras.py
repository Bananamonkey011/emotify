import cv2
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import os

img = cv2.imread("happy_girl")

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

model = Sequential()

model.add(Conv2D(32, kernel_size=(3,3), activation = 'relu', input_shape = (48,48,1)))

print("INCOMPLETE. FINISH KERAS MODEL")
