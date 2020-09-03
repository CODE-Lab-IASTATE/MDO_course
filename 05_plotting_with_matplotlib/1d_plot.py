#matplotlib tutorials

#Import the libraries
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()  # Create figure and axes
ax.plot(x, x, label='linear')  # Plot data
ax.plot(x, x**2, label='quadratic')  
ax.plot(x, x**3, label='cubic')  
ax.set_xlabel('x label')  # x-label
ax.set_ylabel('y label')  # y-label
ax.set_title("Simple Plot")  # itle
ax.legend()  # legend
fig.savefig('1d_plot.png')