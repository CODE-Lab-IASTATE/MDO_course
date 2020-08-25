#Tutorials for optimization in python
#2D
#Gradient free algorithms
#Nelder-Mead simplex algorithm
#Powell algorithm

#Import libraries
from scipy import optimize

#Objective function
def f(x):   # The rosenbrock function
    return .5*(1 - x[0])**2 + (x[1] - x[0]**2)**2

#Run the optimizer
#Try powell algorithm as well
result = optimize.minimize(f, [2, -1], method="Nelder-Mead")
#check if the solver was successful
print(result.success)
#return the minimum
x_min = result.x

print("True minimum:",[1,1])
print("Minimum found by the optimizer:",x_min)
print("Value of the objective function at the minimum:",f([1,1]))
print("Minimum objective function value found:",f(x_min))
