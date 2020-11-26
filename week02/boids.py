import numpy as np

boid_count = 10

limits = np.array([2000, 2000])

positions = np.random.rand(2, boid_count) * limits[:, np.newaxis]
positions

positions.shape

limits[:, np.newaxis]
limits[:, np.newaxis].shape

np.random.rand(2, boid_count).shape

def new_flock(count, lower_limits, upper_limits):
    width = upper_limits - lower_limits
    return (lower_limits[:, np.newaxis] + np.random.rand(2, count) * width[:, np.newaxis])

positions = new_flock(boid_count, np.array([100, 900]), np.array([200, 1100]))

velocities = new_flock(boid_count, np.array([0, -20]), np.array([10, 20]))
velocities

from matplotlib import animation
from matplotlib import pyplot as plt 

# creating a plot
positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))

figure = plt.figure()
axes = plt.axes(xlim=(0, limits[0]), ylim=(0, limits[1]))
scatter = axes.scatter(positions[0, :], positions[1, :],
                       marker='o', edgecolor='k', lw=0.5)
scatter

def update_boids(positions, velocities):
    positions += velocities

def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets(positions.transpose())

anim = animation.FuncAnimation(figure, animate,
                                frames=50, interval=50)

positions = new_flock(100, np.array([100, 900]), np.array([200, 1100]))
velocities = new_flock(100, np.array([0, -20]), np.array([10, 20]))
anim.save('boids_1.mp4')

from IPython.display import HTML
HTML(anim.to_jshtml())
