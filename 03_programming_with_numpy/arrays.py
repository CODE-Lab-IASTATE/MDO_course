#Numpy tutorials
#Arrays

#Import the numpy library
import numpy as np


a = np.array([1, 2, 3])
#print the values of 'a'                  
print(a)  
#returns the type of 'a'
print(type(a))          
#returns the shape of 'a'  
print(a.shape)           
#prints the value of 'a' 
print(a[0], a[1], a[2]) 
# Change an element of the array
a[0] = 5
#print the values of 'a'                  
print(a)  

#reshape a
a = a.reshape(-1,1)
#returns the shape of 'a'  
print(a.shape) 
#Note (3,) means it is a 1d matrix
#(3,1) means it is a 2d matrix
#In python this matters

a = a.reshape(1,-1)
#returns the shape of 'a'  
print(a.shape) 

#.reshape(1,-1) refers to the following
#the first index refers to number of columns, in this case 1
#second index is number of rows, -1 tells numpy to fiugre the length out

#Array of zeros
b = np.zeros(3)
print(b)

#Array of ones
c = np.ones(3)
print(c)