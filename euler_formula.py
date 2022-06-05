import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

def f(x):
    n = np.e ** (x * 1j)
    return [n.real, n.imag] 

def g(x):
    n = 2 * (np.cos(x) + 1j*np.sin(x))
    return [n.real, n.imag]

z = np.linspace(-10, 10, 1000)
x = f(z)[0]
y = f(z)[1]
ax.plot3D(x, y, z, label="e^(ix)")

z = np.linspace(-10, 10, 1000)
x = g(z)[0]
y = g(z)[1]
ax.plot3D(x, y, z, label="2(cos(x) + isin(x))")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("I")

ax.legend()
plt.show()
