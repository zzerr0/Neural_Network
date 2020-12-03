

import numpy as np

inputs = np.array( [ 1.0, 2.0, 3.0, 2.5 ]); 
# above declaration is as a Numpy array
# we can also use a list as a inputs = [1.0, 2.0, 3.0, 2.5]

weights = np.array( [ 0.2, 0.8, -0.5, 1.0 ]);
bias = 2.0

#output = input*weight + bias
output = np.dot( inputs, weights ) + bias

print( output )
