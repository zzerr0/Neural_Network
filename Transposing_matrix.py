




#converting a list into 1d numpy array
#performing a dot product on two matrices

import numpy as np

a = [ 1, 2, 3 ]
b = [ 2, 3, 4 ]

#converting a list into row vector
a = np.array([a])
#converting and transposing the list into column vector
b = np.array( [b] ).T

print(" Row vector is ", a )
print(" Column Vector is \n", b )

#performing the dot product

output = np.dot( a, b )

print("Resultant matrix is of shape", output.shape)

print( output )
