import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""Simple plot"""

x = np.arange(0.0, 2.0, 0.01)
y = np.sin(2 * np.pi * x)

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set(xlabel='variable x', ylabel='sin x ', title='The graph of sine function in the interval [0,2]')

plt.show()

"""Filled Polygon"""

x = [0,1,1,0,-1,0]
y = [0,0,1,1,0.5,0]

plt.axis('equal')
plt.fill(x,y)
plt.show()