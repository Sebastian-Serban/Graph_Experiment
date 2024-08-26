import matplotlib.pyplot as plt
import numpy as np
import math

min = -1000  
max = 1000
steps = 100000
x = np.linspace(min, max, steps)

# define the functions
y = (np.sin(x) ** 2)* (x**2)
z = np.sin(x)
w = x**2

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['right'].set_position('zero')
ax.spines['top'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.plot(x, y, 'r')
# plt.plot(x, z, 'b')
plt.plot(x, w, 'g')

plt.show()