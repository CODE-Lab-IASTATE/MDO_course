#Tutorials for optimization in python
#1D (scalar value)

#Import the required libraries
from scipy import optimize
import numpy as np

#define the objective function
def f(x):
    return -np.exp(-(x - 0.7)**2)

#Run the optimizer
result = optimize.minimize_scalar(f)
#check if the solver was successful
result.success 
#return the minimum
x_min = result.x
print("Minimum found by the optimizer:",x_min)
print("True minimum:",0.7)
print("Objective function value at the minimum:",f(x_min))