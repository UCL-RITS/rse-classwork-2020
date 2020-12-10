"""
An improved implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.

This code simulates the swarming behaviour of bird-like objects ("boids").

Aspects of boid motion simulated:
1. Boids want to fly towards centre of flock
2. Boids want to fly away from nearby boids
3. Boids want to have similar velocity to nearby boids
"""

# import random for definining boids' initial states
import random

# set number of boids
num_boids = 50
xmin = -450
xmax = 50
ymin = 60
ymax = 300
xvmin = 0
xvmax = 10
yvmin = -20
yvmax = 20

# create boids within function using user-defined values
def create_boids(num_boids,xmin,xmax,ymin,ymax,xvmin,xvmax,yvmin,yvmax):
    # produce list of each variable
    boids_x=[random.uniform(xmin,xmax) for x in range(num_boids)]
    boids_y=[random.uniform(ymin,ymax) for x in range(num_boids)]
    boid_x_velocities=[random.uniform(xvmin,xvmax) for x in range(num_boids)]
    boid_y_velocities=[random.uniform(yxmin,yvmax) for x in range(num_boids)]
    # produce tuple of variable lists
    boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
    return boids

boids = create_boids(num_boids,xmin,xmax,ymin,ymax,xvmin,xvmax,yvmin,yvmax)

# define variables for updating
centre_scale = 0.01
local_vel_scale = 0.125
repel_thresh = 100
local_vel_thresh = 10000

def update_boids(boids, centre_scale, local_vel_scale, repel_thresh, local_vel_thresh):
    # define positions and velocities of boids
    # xs - list of boid x positions
    # ys - list of boid y positions
    # xvs - list of boid x velocities
    # yvs - list of boid y velocities
    xs,ys,xvs,yvs=boids
    # simulate different aspects of boid motion
    for i in range(len(xs)):
        # iterate over all other boids to define interactions
        for j in range(len(xs)):
            # Fly towards the middle (1)
            xvs[i]=xvs[i]+(xs[j]-xs[i])*centre_scale/len(xs)
            yvs[i]=yvs[i]+(ys[j]-ys[i])*centre_scale/len(xs)
            # Fly away from nearby boids (2)
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < repel_thresh:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
             # Try to match speed with nearby boids (3)
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < local_vel_thresh:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*local_vel_scale/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*local_vel_scale/len(xs)
        # Move according to velocities
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]