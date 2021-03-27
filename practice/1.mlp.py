import numpy as np

class MLP(object): # multilayer perception
    """Basic Multilayer Perceptron with forward propigation
    """
    def __init__(self, numInputs = 3, hiddenLayers = [3, 5], numOutputs = 2): # constructor hidden[number of hidden neurons on layer, num...]
        
        self.numInputs = numInputs
        self.hiddenLayers = hiddenLayers
        self.numOutputs = numOutputs

        layers = [numInputs] + self.hiddenLayers + [self.numOutputs]

        # initiate random weights
        self.weights = [] # list of as many items as num of weight matricies

        # create weight matrix for each pair of layers
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1]) #[rows, cols])
            self.weights.append(w)


    def forward_propagate(self, inputs): #computes inputs from left to right, gives us prediction.

        # the input layer activation is just the input itself
        activations = inputs

        # iterate through the network layers
        for w in self.weights:

            # calculate matrix multiplication between previous activation and weight matrix
            netInputs = np.dot(activations, w)

            # apply sigmoid activation function
            activations = self._sigmoid(netInputs)

        # return output layer activation
        return activations


    def _sigmoid(self, x):

        y = 1.0 / (1 + np.exp(-x))
        return y

    
if __name__ == "__main__":

    # create a Multilayer Perceptron
    mlp = MLP()

    # set random values for network's input
    inputs = np.random.rand(mlp.numInputs)

    # perform forward propagation
    output = mlp.forward_propagate(inputs)

    print("Network activation: {}".format(output))