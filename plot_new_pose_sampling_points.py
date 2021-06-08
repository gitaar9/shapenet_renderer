import matplotlib.pyplot as plt
import numpy as np
import math
from math import sin, cos

def normalize(vec):
    return vec / (np.linalg.norm(vec, axis=-1, keepdims=True) + 1e-9)

def plot_3d_coors(coords):
    ax.scatter(*list(zip(*coords)), marker='o')
    limit = radius
    ax.set_xlim3d(-limit, limit)
    ax.set_ylim3d(-limit, limit)
    ax.set_zlim3d(-limit, limit)



radius = 10
yaw = np.random.uniform(-math.pi, math.pi, 1000)
pitch = np.random.uniform(math.radians(0), math.radians(85), 1000)

x = np.sin(yaw) * np.cos(pitch)
y = np.sin(pitch)
z = np.cos(yaw) * np.cos(pitch)
x = np.expand_dims(x, axis=1)
y = np.expand_dims(y, axis=1)
z = np.expand_dims(z, axis=1)
coords = np.concatenate((x, y, z), axis=1) * radius


xyz = np.random.normal(size=(1000, 3))
xyz[:, 1] = np.abs(xyz[:, 1])
xyz = normalize(xyz) * radius

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plot_3d_coors(coords)
plot_3d_coors(xyz)
plt.show()
