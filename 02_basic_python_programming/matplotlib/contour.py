#matplotlib tutorials
#contour plot tutorial

#Import the libraries

import numpy as np
import matplotlib.pyplot as plt

def f(x,y): 
    return (1 - x)**2 + 100*(y - x**2)**2

#Upper and lower bounds of the design variables
lb = np.array([-2.5, -1.5])
ub = np.array([2.5, 3.5])
bounds = [(lb[0],ub[0]), (lb[1],ub[1])]


## plotting the surface
fig1 = plt.figure(figsize=(9,6),dpi=100)
u = np.linspace(lb[0],ub[0], 50)
v = np.linspace(lb[1],ub[1], 50)
xv, yv = np.meshgrid(u, v)

x1= xv.reshape(2500,1)
x2= yv.reshape(2500,1)
x=np.column_stack((x1,x2))
y = f(x1, x2)
    
z=y.reshape(50,50)

ax = plt.subplot(111)
ax.contour(xv, yv, z, 100, cmap = 'jet')
ax.set_title('contour');
csfont = {'fontname':'Times New Roman','fontsize':16}
ax.set_xlabel("x1", **csfont)
ax.set_ylabel("x2", **csfont)
fig1.savefig('contour.png')