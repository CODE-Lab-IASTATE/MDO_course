#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:27:23 2020

@author: jethro
"""

# rosenbrock_demo.py
#
#Python 2.7.3
#Matplotlib 1.1.1rc

#Code also works fine with Anaconda3 / matplotlib version 1.4.0!
#Code also works fine with CPython 3.4.2 + Scipy-stack-14.8.27.win32-py3.4 from
#   Christoph Gohlke's unofficial libraries:
#    http://www.lfd.uci.edu/~gohlke/pythonlibs/

#Works fine with Python3 on Ubuntu 14.04 after adding SciPy stack:
# sudo apt-get install python3-numpy python3-scipy python3-matplotlib



#This function is not used, but illustrates the Rosenbrock function with
# 2 parameters. The actual Rosenbrock function is embedded in the code below
# using array operations so that it is calculated over a meshgrid of many
# points to produce an array of many Z values.
#Rosenbrock function of 2 variables:
def rosenbrock(x,y):
      return (1-x)**2 + 100* ((y-x**2))**2

    
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plot
import numpy as np

fig = plot.figure()
ax = fig.gca(projection='3d')

s = 0.05   # Try s=1, 0.25, 0.1, or 0.05
X = np.arange(-2, 2.+s, s)   #Could use linspace instead if dividing
Y = np.arange(-2, 3.+s, s)   #evenly instead of stepping...
    
#Create the mesh grid(s) for all X/Y combos.
X, Y = np.meshgrid(X, Y)

#Rosenbrock function w/ two parameters using numpy Arrays
Z = (1.-X)**2 + 100.*(Y-X*X)**2

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
         linewidth=0, antialiased=False)  #Try coolwarm vs jet

 
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

#Displays the figure, handles user interface, returns when user closes window
plot.show()