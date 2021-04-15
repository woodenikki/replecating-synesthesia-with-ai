import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow.keras as keras

from sklearn import svm, datasets
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

DATASET_PATH = "src\data.json"

def load_data(data_path):
    """Loads training dataset from json file.

        :param data_path (str): Path to json file containing data
        :return inputs (ndarray): Inputs
        :return targets (ndarray): Targets
    """

    with open(data_path, "r") as fp:
        data = json.load(fp)

    # convert lists to numpy arrays
    inputs = np.array(data["mfcc"])
    targets = np.array(data["labels"])
    categories = np.array(data["mapping"])
    for i, x in enumerate(categories):
        y = x.split('\\')[2]
        categories[i] = y
    
    print("Data succesfully loaded!")

    print("Data succesfully loaded!")

    return  inputs, targets, categories

def plot_history(history):
    """Plots accuracy/loss for training/validation set as a function of the epochs

        :param history: Training history of model
    """
    fig, axs = plt.subplots(2) # 2 subplots

    # create accuracy subplot
    axs[0].plot(history.history["accuracy"], label="train accuracy")
    axs[0].plot(history.history["val_accuracy"], label="test accuracy")
    axs[0].set_ylabel("Accuracy")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy Evaluation")

    # create error subplot
    axs[1].plot(history.history["loss"], label="train error")
    axs[1].plot(history.history["val_loss"], label="test error")
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error Evaluation")

    plt.show()

if __name__ == "__main__":
    
    # load data
    inputs, targets, class_names = load_data(DATASET_PATH)
    num_classes = class_names.size
    # split the data into train and test sets
    inputs_train, inputs_test, targets_train, targets_test = train_test_split(inputs, targets, test_size=0.25) # 25% used for testing

    # build the network architecture (Tensorflow + Keras)
    model = keras.Sequential([
        # input layer
        keras.layers.Flatten(input_shape=(inputs.shape[1], inputs.shape[2])),

        # 1st hidden layer
        keras.layers.Dense(512, activation='relu', kernel_regularizer=keras.regularizers.l2(0.0005)),
        keras.layers.Dropout(0.1),                 

        # 2nd hidden layer
        keras.layers.Dense(256, activation="relu", kernel_regularizer=keras.regularizers.l2(0.0005)),
        keras.layers.Dropout(0.1),

        # 3rd hidden layer
        keras.layers.Dense(64, activation="relu", kernel_regularizer=keras.regularizers.l2(0.0005)),
        keras.layers.Dropout(0.1),

        # output
        keras.layers.Dense(num_classes, activation="softmax") # TODO: 11 color categories
    ])
    
    # compile network
    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=optimizer, loss="sparse_categorical_crossentropy", metrics=["accuracy"]) # loss (error) function for multiclassification
    model.summary()

    # train network
    history = model.fit(inputs_train, targets_train, validation_data=(inputs_test, targets_test), epochs=75, batch_size=32)

    # plot accuracy and error over the epochs
    plot_history(history)

    #plot confusion matrix
    y_pred = np.argmax(model.predict(inputs_test), axis=-1)
    y_test = targets_test

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(12, 12))
    ax = sns.heatmap(cm, cmap="rocket_r", fmt=".01f", annot_kws={'size':16}, annot=True, square=True,
                xticklabels=class_names, yticklabels=class_names)
    ax.set_ylabel('Actual', fontsize=20)
    ax.set_xlabel('Predicted', fontsize=20)
    plt.show()

    #save model uwu
    model.save("luminisity75.h5")