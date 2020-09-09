#matplotlib tutorials
#Convergence plot of the optimizer

#Import the libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

#Upper and lower bounds of the design variables
#Used for both plotting and when bounds are specified in the optimizer
lb = np.array([-2.5, -1.5])
ub = np.array([2.5, 3.5])
bounds = [(lb[0],ub[0]), (lb[1],ub[1])]

#Objective function
def f(x):   # The rosenbrock function
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

#Gradient of objective function
def jacobian(x):
    return np.array((-2*(1 - x[0]) - 400*x[0]*(x[1] - x[0]**2), 200*(x[1] - x[0]**2)))

#Starting point of the optimizer
x0 = np.array([-2,1])

#Store the intermediate iteration values
store = [x0]
def storage(x):
    return store.append(x)

result = optimize.minimize(f, x0, method='BFGS', jac=jacobian, callback = storage,
                           options={'ftol': 1e-9, 'disp': True})


store = np.array(store) #Convert to numpy array 


fig1, ax1 = plt.subplots(figsize=(7,5))  # Create figure and axes
ax1.plot(range(len(store)), f(store.T))  # Plot data
ax1.set_yscale('log')
ax1.set_xlabel('Iteration index', fontsize = 15)  # x-label
ax1.set_ylabel('Objective function', fontsize = 15)  # y-label
ax1.set_title("Convergence of the objective function", fontsize = 15)  # title
ax1.legend()  # legend
fig1.savefig('obj_func.pdf')

#Calculate the norm of the difference between consecutive design variables 
diff = np.diff(store,axis=0) #Difference between row values
norm = np.linalg.norm(diff,axis=1) #Norm of the difference
norm = np.append(np.linalg.norm(store[0]),norm) #Add the norm of the initial design

fig2, ax2 = plt.subplots(figsize=(7,5))  # Create figure and axes
ax2.plot(range(len(store)), norm)  # Plot data
ax2.set_yscale('log')
ax2.set_xlabel('Iteration index', fontsize = 15)  # x-label
ax2.set_ylabel('||$x^{(i)}$ - $x^{(i-1)}$||', fontsize = 15)  # y-label
ax2.set_title("Change in argument x", fontsize = 15)  # title
ax2.legend()  # legend
fig2.savefig('dv.pdf')