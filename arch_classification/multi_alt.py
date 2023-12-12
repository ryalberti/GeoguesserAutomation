# for training a multilabel (multi input, multi output) image classifier 
# https://vijayabhaskar96.medium.com/multi-label-image-classification-tutorial-with-keras-imagedatagenerator-cd541f8eaf24 

from keras.models import Sequential
# imports 
from keras_preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D
from keras import regularizers, optimizers
from keras import Input, Model
import pandas as pd
import numpy as np
import os 

# set directories 
dir_path = os.getcwd() # get current directory , \GeoguesserAutomation\arch_classification
db_path = dir_path+"\\database" # \GeoguesserAutomation\arch_classification\database
train_path = db_path + "\\train" # \GeoguesserAutomation\arch_classification\database\train
test_path = db_path+"\\test"
verify_path = db_path + "\\verify"
csv_train_path = db_path + "\\arch_train_labels.csv"
csv_test_path = db_path + "\\arch_test_labels.csv"
class_path = db_path + "\\classes.txt"

f = open(class_path,"r")
fp = f.read()
fps = fp.split(",")
class_list = [] # should hold a list of all classes 
for class_obj in fps:
    class_list.append(class_obj)

df = pd.read_csv(csv_train_path)
df["labels"]=df["labels"].apply(lambda x:x.split(",")) # this wont matter bc i didn't format it like this, but I'll leave it for posterity's sake 

datagen=ImageDataGenerator(rescale=1./255.)
test_datagen=ImageDataGenerator(rescale=1./255.)

train_generator=datagen.flow_from_dataframe(
    dataframe=df[:1800],
    directory=train_path,
    x_col="Filenames",
    y_col="labels",
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode="categorical",
    classes=class_list,
    target_size=(100,100))

valid_generator=test_datagen.flow_from_dataframe(
    dataframe=df[1800:1900],
    directory=train_path,
    x_col="Filenames",
    y_col="labels",
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode="categorical",
    classes=class_list,
    target_size=(100,100))

test_generator=test_datagen.flow_from_dataframe(
    dataframe=df[1900:],
    directory=verify_path,
    x_col="Filenames",
    batch_size=1,
    seed=42,
    shuffle=False,
    class_mode=None,
    target_size=(100,100))


model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=(100,100,3)))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='sigmoid'))
model.compile(optimizers.rmsprop(lr=0.0001, decay=1e-6),loss="binary_crossentropy",metrics=["accuracy"])

STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
STEP_SIZE_VALID=valid_generator.n//valid_generator.batch_size
STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
model.fit_generator(generator=train_generator,
                    steps_per_epoch=STEP_SIZE_TRAIN,
                    validation_data=valid_generator,
                    validation_steps=STEP_SIZE_VALID,
                    epochs=10
)

test_generator.reset()
pred=model.predict_generator(test_generator,
steps=STEP_SIZE_TEST,
verbose=1)

pred_bool = (pred >0.5)