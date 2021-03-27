# Basic Multilayer Perceptron with forward and backward propogation, gradient descent, etc.

import numpy as np

from random import random

class MLP(object): # multilayer perception
    """A Multilayer Perceptron class.
    """

    def __init__(self, num_inputs = 3, hidden_layers = [3, 3], num_outputs = 2): # constructor hidden[number of hidden neurons on layer, num...]
        """Constructor for the MLP. Takes the number of inputs,
            a variable number of hidden layers, and number of outputs
        Args:
            num_inputs (int): Number of inputs
            hidden_layers (list): A list of ints for the hidden layers
            num_outputs (int): Number of outputs
        """
        self.num_inputs = num_inputs
        self.hidden_layers = hidden_layers
        self.num_outputs = num_outputs

        layers = [num_inputs] + self.hidden_layers + [self.num_outputs]

        # create generic representation of layers with random weights
        weights = [] # list of as many items as num of weight matricies

        # create weight matrix for each pair of layers
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i + 1]) #[rows, cols])
            weights.append(w)
        self.weights = weights

        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i]) # dummy activation array for each layer
            activations.append(a)
        self.activations = activations
        
        derivatives = []
        for i in range(len(layers) - 1):
            d = np.zeros((layers[i], layers[i+1]))
            derivatives.append(d)
        self.derivatives = derivatives





    def forward_propagate(self, inputs): #computes inputs from left to right, gives us prediction.
        """Computes forward propagation of the network based on input signals.
        Args:
            inputs (ndarray): Input signals
        Returns:
            activations (ndarray): Output values
        """

        # the input layer activation is just the input itself
        activations = inputs
        self.activations[0] = inputs


        # iterate through the network layers
        for i, w in enumerate(self.weights):
            # calculate matrix multiplication between previous activation and weight matrix
            net_inputs = np.dot(activations, w)

            # apply sigmoid activation function
            activations = self._sigmoid(net_inputs)

            # save the activations for backpropogation
            self.activations[i + 1] = activations

        # return output layer activation
        return activations

    def back_propagate(self, error, verbose=False):
        # 1. dE/dW_i = (y - a_[i+1) s'(h_[i+1])) a_i
        # 2. s' (h_[i+1]) = s(h_[i+1])(1 - s(h_[i+1]))
        # 3. s(h_[i+1]) = a_[i+1]
        # ↓
        # dE/dW_[i-1] = (y - a_[i+1]) s'(s_[i+1])) W_i s'(h_i) a_[i-1]

        for i in reversed(range(len(self.derivatives))):            # right to left
            activations = self.activations[i+1]   
            delta = error * self._sigmoid_derivative(activations)   # first part of 1                       # ndarray([0.1, 0.2]) --> ndarray([[0.1, 0.2]])   ; 2d array w/ single row
            delta_reshaped = delta.reshape(delta.shape[0], -1).T
            current_activations = self.activations[i]               # a_i
            current_activations_reshaped = current_activations.reshape(current_activations.shape[0], -1)    # ndarray([0.1, 0.2]) --> ndarray([[0.1], [0.2]]) ; 2d array

            self.derivatives[i] = np.dot(current_activations_reshaped, delta_reshaped)
            error = np.dot(delta, self.weights[i].T)
            

            if verbose:
                print("Derivatives for W{}: {}".format(i, self.derivatives[i]))
        return error


    def gradient_descent(self, learning_rate):
        for i in range(len(self.weights)):
            weights = self.weights[i]
            derivatives = self.derivatives[i]
            weights += derivatives * learning_rate

    def train(self, inputs, targets, epochs, learning_rate):
        # epoch: how many times to feed the whole data set to the NN.
        # More times = better predictions (hopefully)

        for i in range(epochs):
            sum_error = 0
            for j, (input, target) in enumerate(zip(inputs, targets)): # j is index of (input, target) within (inputs, targets). 
                # forward propagation
                output = self.forward_propagate(input)

                # calculate error
                error = target - output

                # back propagation
                self.back_propagate(error)

                # apply gradient descent
                self.gradient_descent(learning_rate)
                    
                sum_error += self._mse(target, output)

            # report error
            print("Error: {} at epoch {} ".format(sum_error / len(inputs), i))
                

    def _mse(self, target, output): #main squared error
        return np.average((target - output) **2)

    def _sigmoid_derivative(self, x):
        return x * (1.0 - x)

    def _sigmoid(self, x):
        """Sigmoid activation function
        Args:
            x (float): Value to be processed
        Returns:
            y (float): Output
        """

        y = 1.0 / (1 + np.exp(-x))
        return y

    
if __name__ == "__main__":

    # create a dataset to train a n etwork for the sum operation
    inputs = np.array([[random() / 2 for _ in range(2)] for _ in range(1000)])   # array([0.1, 0.2], [0.3, 0.4]) ; inputs
    targets = np.array([[i[0] + i[1]] for i in inputs])                          # array([0.3], [0.7]) ; sums (answers)

    # create a Multilayer Perceptron
    mlp = MLP(2, [5], 1)
    
    # train our mlp
    mlp.train(inputs, targets, 50, 0.1)

    # create dummy data
    input = np.array([0.3, 0.1])
    target = np.array(0.4)

    output = mlp.forward_propagate(input)
    print()
    print()
    print()

    print("Network believes that {} + {} is equal to {}".format(input[0], input[1], output))