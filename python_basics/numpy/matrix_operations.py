#Numpy tutorials
#Matrix operations

#Import the numpy library
import numpy as np

a = np.random.randint(10, size = (3,3))
print(a)
print("\n")
b = np.random.randint(10, size = (3,3))
print(b)
print("\n")

#Add
c = np.add(a,b)
print(c)
c = a + b
print(c)
print("\n")

#subtract
d =np.subtract(a,b)
print(d)
d = a-b
print(d)
print("\n")

#multiply (element-wise)
e = np.multiply(a,b)
print(e)
e = a * b
print(e)

#Matrix multiplication
e = np.dot(a,b)
print(e)
print("\n")

#divide (element-wise)
f = np.divide(a,b)
print(f)
f = a / b
print(f)
print("\n")

#invert a matrix
g = np.linalg.inv(a)
print(g)
