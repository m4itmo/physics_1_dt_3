import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

r = 1.0
v = 2.0
omega = v / r

t_max = 10
fps = 60
t = np.linspace(0, t_max, t_max * fps)

x = v * t - r * np.sin(omega * t)
y = r - r * np.cos(omega * t)

fig, ax = plt.subplots()
ax.set_xlim(0, max(x))
ax.set_ylim(0, 2 * r * 1.1)

line, = ax.plot([], [], 'b-', lw=2)
point, = ax.plot([], [], 'r.')


def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point


def update(frame):
    line.set_data(x[:frame], y[:frame])
    point.set_data([x[frame]], [y[frame]])
    return line, point


ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1000 / fps)

plt.show()
