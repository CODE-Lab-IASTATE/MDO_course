#Tutorials for optimization in python
#2D
#BFGS
#Note that BFGS in scipy cannot handle bounds and contraints

#Import libraries
from scipy import optimize
import numpy as np

#Objective function
def f(x):   # The rosenbrock function
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

#Gradient of objective function
def jacobian(x):
    return np.array((-2*(1 - x[0]) - 400*x[0]*(x[1] - x[0]**2), 200*(x[1] - x[0]**2)))

#Starting point of the optimizer
x0 = np.array([2,-1])

#Run the optimizer
#lambda x defines x as a variable
#If the jac value is not provided, the optimizer will approximate it using finite differences
result = optimize.minimize(lambda x: f(x), x0, method="BFGS", jac = jacobian, options={'disp': True})
#check if the solver was successful
print(result.success)
#return the minimum
x_min = result.x

print("True minimum:",[1,1])
print("Minimum found by the optimizer:",x_min)
print("Value of the objective function at the minimum:",f([1,1]))
print("Minimum objective function value found:",f(x_min))

#Check error of gradient 
#Results norm of the differnce between the grad given and the grad computed numerically
x = np.array([1,-1]) #location to compare the gradient values
error_grad = optimize.check_grad(f, jacobian, x)
print("Error in the gradient values:",error_grad)