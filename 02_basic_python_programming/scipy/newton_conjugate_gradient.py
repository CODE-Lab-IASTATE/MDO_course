#Tutorials for optimization in python
#2D
#Newton Conjugate gradient
#This is a modified Newton algorithm that uses the CG algorithm to approx invert the local hessian
#Requires both the gradient and hessian information

#Import libraries
from scipy import optimize
import numpy as np

#Objective function
def f(x):   # The rosenbrock function
    return .5*(1 - x[0])**2 + (x[1] - x[0]**2)**2

#Gradient of objective function
def jacobian(x):
    return np.array((-2*.5*(1 - x[0]) - 4*x[0]*(x[1] - x[0]**2), 2*(x[1] - x[0]**2)))

#Hessian of objective function
def hessian(x): # Computed with sympy
    return np.array(((1 - 4*x[1] + 12*x[0]**2, -4*x[0]), (-4*x[0], 2)))

#Run the optimizer
result = optimize.minimize(f, [2, -1], method="Newton-CG", jac=jacobian, hess=hessian)
#check if the solver was successful
result.success
#return the minimum
x_min = result.x
print("True minimum:",[1,1])
print("Minimum found by the optimizer:",x_min)
print("Value of the objective function at the minimum:",f([1,1]))
print("Minimum objective function value found:",f(x_min))