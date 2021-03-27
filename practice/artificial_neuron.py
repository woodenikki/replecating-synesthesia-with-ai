import math

def sigmoid(x):
    y = 1.0/(1 + math.exp(-x))
    return y

def activate(input, weight):
    # perform net input
    h = 0
    for x, w in zip(inputs, weight):
        h += x*w


    # perform the activation
    return sigmoid(h)

if __name__ == "__main__":
    inputs = [.5, .3, .2]
    weights = [.4, .7, .2]
    output = activate(inputs, weights)
    print(output)