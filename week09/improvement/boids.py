"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.

This code simulates the swarming behaviour of bird-like objects ("boids").
"""

import random
x_min = -450
x_max = 50
y_min = 300
y_max = 600
x_velocity_min = 0
x_velocity_max = 10
y_velocity_min = -20
y_velocity_max = 20

#picks a random number inside distribution with bounds (x_min, x_max)
boids_x = [random.uniform(x_min, x_max)]
boids_y = [random.uniform(y_min, y_max)]

boid_x_velocities = [random.uniform(x_velocity_min, x_velocity_max)]
boid_y_velocities = [random.uniform(y_velocity_min, y_velocity_max)]

boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)


def update_boids(boids):
    multiplier = 0.01
    multiplier_velocity = 0.125
    xs, ys, xvs, yvs = boids
    
    # Fly towards the middle
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i] = xvs[i] + (xs[j] - xs[i]) * multiplier / len(xs)
            yvs[i] = yvs[i] + (ys[j] - ys[i]) * multiplier / len(xs)

    # Fly away from nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j] - xs[i])**2 + (ys[j] - ys[i])**2 < 100:
                xvs[i] = xvs[i] + (xs[i] - xs[j])
                yvs[i] = yvs[i] +( ys[i] - ys[j])

    # Try to match speed with nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j] - xs[i])**2 + (ys[j] - ys[i])**2 < 10000:
                xvs[i] = xvs[i] + (xvs[j] - xvs[i]) * multiplier_velocity / len(xs)
                yvs[i] = yvs[i]+(yvs[j]-yvs[i]) * multiplier_velocity / len(xs)

    # Move according to velocities
    for i in range(len(xs)):
        xs[i] = xs[i] + xvs[i]
        ys[i] = ys[i] + yvs[i]
