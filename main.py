import numpy as np
import matplotlib.pyplot as plt

r = 1.0
v = 2.0

t = np.linspace(0, 2 * np.pi, 1000)

omega = v / r

x = r * (omega * t - np.sin(omega * t))
y = r * (1 - np.cos(omega * t))

plt.plot(x, y)
plt.title("Trajectory of a point on the wheel rim (cycloid)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('equal')
plt.show()
