import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.core.function_base import linspace
plt.style.use('seaborn-ticks')

c_s = 299792458

x = np.loadtxt('build/data.txt', usecols=(0), unpack=True)
y = np.loadtxt('build/data.txt', usecols=(1), unpack=True)

#plt.plot(x, y)
plt.plot(x, y/(math.exp(2)/(math.pi**2 * c_s)))

# plt.yscale("log")
plt.xlabel(r'$\theta^\prime, deg$')
plt.ylabel(r'$d^2W / d\omega d\Omega, e^2 / \pi^2c$')
plt.title('Vavilov-Cherenkov Radiation')
plt.show()
