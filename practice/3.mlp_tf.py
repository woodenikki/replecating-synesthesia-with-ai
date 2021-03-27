# implement a neural net using TenserFlow


import numpy as np
import tensorflow as tf

from random import random
from sklearn.model_selection import train_test_split

def generate_dataset(num_samples, test_size):

    # create a dataset to train a n etwork for the sum operation
    x = np.array([[random() / 2 for _ in range(2)] for _ in range(num_samples)])   # array([0.1, 0.2], [0.3, 0.4]) ; inputs
    y = np.array([[i[0] + i[1]] for i in x])                          # array([0.3], [0.7]) ; sums (answers)

    # split dataset into test and training sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    return x_train, x_test, y_train, y_test

if __name__ == "__main__":
    x_train, x_test, y_train, y_test = generate_dataset(5000, 0.3)
    # print("x_test: \n {}".format(x_test))
    # print("y_test: \n {}".format(y_test))

        
    # build model: 2 input neurons > 5 hidden layers > 1 output layer
    model = tf.keras.Sequential([ # Keras is a tf library
        tf.keras.layers.Dense(5, input_dim=2, activation="sigmoid"),    # hidden
        tf.keras.layers.Dense(1, activation="sigmoid")                  # output
    ])

    # compile model
    optimiser = tf.keras.optimizers.SGD(learning_rate=0.1)               # SGD = Stochastic Gradient Descent optimizer
    model.compile(optimizer=optimiser, loss="MSE")

    # train model
    model.fit(x_train, y_train, epochs=100)

    # evaluate model
    print("\nModel evaluation: ")
    model.evaluate(x_test, y_test, verbose=1)

    # make predictions
    data = np.array([[0.1, 0.2], [0.2, 0.2]])
    predictions = model.predict(data)

    print("\nPredictions:")
    for d, p in zip(data, predictions):
        print("{} + {} = {}".format(d[0], d[1], p[0]))