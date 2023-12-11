# # Load EDA Pkgs
# import numpy as np
# from sklearn.datasets import make_multilabel_classification
# from sklearn.multioutput import MultiOutputClassifier
# from sklearn.linear_model import LogisticRegression


# x, y = make_multilabel_classification(n_classes=42, random_state=0)
# clf = MultiOutputClassifier(LogisticRegression()).fit(x, y)


from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D
from keras import regularizers, optimizers
import pandas as pd
import numpy as np

df = pd.read_csv("arch_labels.csv")
df["labels"]=df["labels"].apply(lambda x:x.split(",")) # this wont matter bc i didn't format it like this, but I'll leave it for posterity's sake 

datagen=ImageDataGenerator(rescale=1./255.)
test_datagen=ImageDataGenerator(rescale=1./255.)

train_generator=datagen.flow_from_dataframe(
    dataframe=df[:1800],
    directory="./miml_dataset/images",
    x_col="Filenames",
    y_col="labels",
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode="categorical",
    classes=labels_header,
    target_size=(100,100))

valid_generator=test_datagen.flow_from_dataframe(
    dataframe=df[1800:1900],
    directory="./miml_dataset/images",
    x_col="Filenames",
    y_col="labels",
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode="categorical",
    classes=labels_header,
    target_size=(100,100))

test_generator=test_datagen.flow_from_dataframe(
    dataframe=df[1900:],
    directory="./miml_dataset/images",
    x_col="Filenames",
    batch_size=1,
    seed=42,
    shuffle=False,
    class_mode=None,
    target_size=(100,100))