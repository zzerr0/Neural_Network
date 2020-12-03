

#neural network with 3 layers of neurons 

import numpy as np;


inputs = [ 1.0, 2.0, 3.0, 2.5 ]
#no. of inputs given to  a Neuron

weights = [ [ 0.2, 0.8, -0.5, 1 ], 
            [ 0.5, -0.9, 0.26, -0.5 ], 
            [ -0.26, -0.27, 0.17, 0.87 ] ]
#each list of weight is for a particular neuron

biases = [ 2.0, 3.0, 0.5]
#one bias for each neuron

layer_output = np.dot( weights, inputs ) + biases

print(layer_output)
