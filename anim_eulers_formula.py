import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

def f(x, y):
    return np.cos(x) + np.sin(y)

z = np.linspace(-10, 10, 1000)
x = np.cos(z)
y = np.sin(z)

pointsx = []
pointsy = []
pointsz = []

def animate(i):
    pointsx.append(x[i])
    pointsy.append(y[i])
    pointsz.append(i)

    ax.clear()
    ax.plot3D(pointsx, pointsy, pointsz)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([0, 1000])

anim = animation.FuncAnimation(fig, animate, frames=1000, interval=1, repeat=False)

plt.grid()
plt.show()
