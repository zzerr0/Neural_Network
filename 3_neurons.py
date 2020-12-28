


import numpy as np


inputs = [ 1, 2, 3, 4 ]
weights = [ 
            [ 0.2, 0.3, 0.4, 0.5], 
            [ 0.6, 0.7, 0.8, 0.9], 
            [ 0.10, 0.11, 0.12, 0.13] 
          ]
biases = [ 2, 3, 1.5 ]   
layer_output = [] 
biases = np.array( biases )    
inputs = np.array( inputs )
weights = np.array( weights )

print(inputs,"\n")
print(weights)
print("\n")


for neuron_weights, neuron_biases in zip( weights, biases) :
 
  print("Inside first for looop ")
  print(" neuron_weight = ", neuron_weights )
  print(" neuron_biases = ", neuron_biases )
  
  print("_______________________________")
 # neuron_output = 0
  for n_input, weight in zip( inputs, neuron_weights ):
   # neuron_output += n_input*weight
   print("Inside Second For loop ")
   print("n_input = ", n_input )
   print("weight = ", weight )
  #neuron_output += neuron_biases
  #layer_output.append( neuron_output )


print(" Output of 3 Neurons is \n")
print( layer_output )
