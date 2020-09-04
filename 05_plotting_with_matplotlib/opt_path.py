#matplotlib tutorials
#contour plot tutorial showing the path taken by the optimizer

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

## plotting the surface
fig1 = plt.figure(figsize=(9,6),dpi=100)
u = np.linspace(lb[0],ub[0], 50)
v = np.linspace(lb[1],ub[1], 50)
xv, yv = np.meshgrid(u, v)

x1= xv.reshape(2500,1)
x2= yv.reshape(2500,1)
x=np.column_stack((x1,x2))
y = f(x.T)  
z=y.reshape(50,50)

ax = plt.subplot(111)
ax.contour(xv, yv, z, 100, cmap = 'jet')
ax.plot(store[:, 0], store[:, 1], '-o', color = 'black') #Plot path
ax.set_title('contour');
csfont = {'fontname':'Times New Roman','fontsize':16}
ax.set_xlabel("x1", **csfont)
ax.set_ylabel("x2", **csfont)
fig1.savefig('opt_path.pdf')