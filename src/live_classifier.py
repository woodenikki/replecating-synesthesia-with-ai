# for testing only!


import json
import numpy as np

import keras
from keras import models
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
#Keras
import keras
from keras import models
from keras import layers

# path to json file that stores MFCCs and genre labels for each processed segment
DATA_PATH = "src\data.json"
num_classes = 11

def load_data(data_path):
    """Loads training dataset from json file.

        :param data_path (str): Path to json file containing data
        :return X (ndarray): Inputs
        :return y (ndarray): Targets
    """

    with open(data_path, "r") as fp:
        data = json.load(fp)

    # convert lists to numpy arrays
    X = np.array(data["mfcc"])
    y = np.array(data["labels"])

    print("Data succesfully loaded!")

    return  X, y

if __name__ == "__main__":

    # load data
    X, y = load_data(DATA_PATH)

    # create train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # creating a model
    model = keras.Sequential([

        # input layer
        keras.layers.Flatten(input_shape=(X.shape[1], X.shape[2])),

        # 1st dense layer
        keras.layers.Dense(512, activation='relu'),

        # 2nd dense layer
        keras.layers.Dense(256, activation='relu'),

        # 3rd dense layer
        keras.layers.Dense(64, activation='relu'),

        # output layer
        keras.layers.Dense(10, activation='softmax')
    ])

    optimiser = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
                
    history = model.fit(X_train,
                        y_train,
                        epochs=20,
                        batch_size=128)
                        
    # calculate accuracy
    test_loss, test_acc = model.evaluate(X_test,y_test)
    print('test_acc: ',test_acc)

    # predictions
    predictions = model.predict(X_test)
    np.argmax(predictions[0])

    # print("*****PRINTING X_test*****")
    # for x in X_test:
    #     print(x)

    # print("*****PRINTING y_train*****")
    # for x in y_train:
    #     print(x)

    # print("*****PRINTING y_test*****")
    # for x in y_test:
    #     print(x)


