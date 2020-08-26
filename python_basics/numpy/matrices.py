#Numpy tutorials
#Matrices

#Import the numpy library
import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#print the values of 'a'                  
print(a) 
#returns the shape of 'a'  
print(a.shape) 
#prints the 1st row values
print(a[0, :])

#transpose the matrix
b = np.transpose(a)
#print the values of 'b'                  
print(b) 
#returns the shape of 'b'  
print(b.shape) 

#reshape into different size
c = a.reshape(2,-1)
print(c)
