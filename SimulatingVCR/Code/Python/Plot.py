import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.core.function_base import linspace
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('seaborn-ticks')

c_s = 299792458

x = np.loadtxt('build/data.txt', usecols=(0), unpack=True)
y = np.loadtxt('build/data.txt', usecols=(1), unpack=True)

#plt.plot(x, y)
plt.plot(x, y/(math.exp(2)/(math.pi**2 * c_s)))

# plt.yscale("log")
plt.xlabel(r'$a, m$')
plt.ylabel(r'$d^2W / d\omega d\Omega, e^2 / \pi^2c$')
plt.title('Vavilov-Cherenkov Radiation')

plt.show()

'''
# 3D plot
x = np.loadtxt('build/data3D.txt', usecols=(0), unpack=True)
z = np.loadtxt('build/data3D.txt', usecols=(1), unpack=True)
y = np.loadtxt('build/data3D.txt', usecols=(2), unpack=True)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot_trisurf(x, y, z/(math.exp(2)/(math.pi**2 * c_s)))

# plt.yscale("log")
ax.set_xlabel(r'$\theta^\prime, deg$')
ax.set_zlabel(r'$d^2W / d\omega d\Omega, e^2 / \pi^2c$')
ax.set_ylabel(r'$a, m$')
ax.set_title('Vavilov-Cherenkov Radiation 3D plot')
'''
plt.show()
