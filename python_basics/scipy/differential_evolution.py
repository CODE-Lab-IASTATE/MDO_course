#Tutorials for optimization in python
#2D
#Differential evolution algorithm
#Global optimizer

#Import libraries
from scipy import optimize

#Objective function
def f(x):   # The rosenbrock function
    return .5*(1 - x[0])**2 + (x[1] - x[0]**2)**2

#Upper and lower bounds of each variable
bounds = optimize.Bounds([0, -0.5], [1.0, 2.0])

#Run the optimizer
result = optimize.differential_evolution(f, bounds) 

print(result)
#return the minimum
x_min = result.x

print("True minimum:",[1,1])
print("Minimum found by the optimizer:",x_min)
print("Value of the objective function at the minimum:",f([1,1]))
print("Minimum objective function value found:",f(x_min))