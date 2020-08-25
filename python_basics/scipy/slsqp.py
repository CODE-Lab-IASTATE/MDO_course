#Tutorials for optimization in python
#Multidimension 
#SLSQP: sequential least squares programming
#A quasi-newton algorithm
#Can handle bounds and constraints

#Import libraries
from scipy import optimize
import numpy as np

#Objective function
def f(x):   # The rosenbrock function
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

#Gradient of objective function
def jacobian(x):
    return np.array((-2*(1 - x[0]) - 400*x[0]*(x[1] - x[0]**2), 200*(x[1] - x[0]**2)))

#In gradiend-based optimization, the gradient of the constraints are also required
#If they are not provided to the optimizer, it is calculated using finite differences
#Upper and lower bounds of each variable
bounds = optimize.Bounds([0, -0.5], [1.0, 2.0])
#equality constraint
eq_cons = {'type': 'eq', 
           'fun' : lambda x: np.array([2*x[0] + x[1] - 1]), #Function
           'jac' : lambda x: np.array([2.0, 1.0])} #gradient (not necessary)

#inequality constraint
ineq_cons = {'type': 'ineq',
             'fun' : lambda x: np.array([1 - x[0] - 2*x[1], #Function
                                         1 - x[0]**2 - x[1],
                                         1 - x[0]**2 + x[1]]),
             'jac' : lambda x: np.array([[-1.0, -2.0], #gradient (not necessary)
                                         [-2*x[0], -1.0],
                                         [-2*x[0], 1.0]])}

#Starting point of the optimizer
x0 = np.array([2,-1])
#Run the optimizer
#lambda x defines x as a variable
#If the jac value is not provided, the optimizer will approximate it using finite differences
result = optimize.minimize(f, x0, method='SLSQP', jac=jacobian,
                           constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9, 'disp': True},
                           bounds=bounds)

#check if the solver was successful
print(result.success)
#return the minimum
x_min = result.x

print("True minimum:",[0.415,0.17])
print("Minimum found by the optimizer:",x_min)
print("Value of the objective function at the minimum:",f([0.415,0.17]))
print("Minimum objective function value found:",f(x_min))