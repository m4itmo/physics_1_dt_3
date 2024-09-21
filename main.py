import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fps = 60
t_max = 10

r = np.float64(input('Enter radius  : '))
v = np.float64(input('Enter velocity: '))

omega = v / r

t = np.linspace(0, t_max, t_max * fps)

x = v * t - r * np.sin(omega * t)
y = r - r * np.cos(omega * t)

theta = np.linspace(0, 2 * np.pi, t_max * fps)
circle_x = r * np.cos(theta)
circle_y = r * np.sin(theta) + r

fig, ax = plt.subplots()
ax.set_xlim(0, max(x))
ax.set_ylim(0, 2 * r * 1.1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_aspect('equal', 'box')

line, = ax.plot([], [], 'b-', lw=2)
point, = ax.plot([], [], 'r.')

wheel, = ax.plot([], [], 'g-', lw=1)


def init():
    line.set_data([], [])
    point.set_data([], [])
    wheel.set_data([], [])
    return line, point, wheel


def update(frame):
    line.set_data(x[:frame], y[:frame])
    point.set_data([x[frame]], [y[frame]])

    wheel.set_data(v * t[frame] + circle_x, circle_y)

    return line, point, wheel


ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1000 / fps)

plt.show()
