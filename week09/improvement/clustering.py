"""This code implements the k-means clustering algorithm for 2 dimensions."""

from math import sqrt
from random import randrange

# PARAMETERS
k=3 # number clusters

# reading in (x,y) coords of the data points
lines = open('samples.csv', 'r').readlines()
points_coords=[]
for line in lines: points_coords.append(tuple(map(float, line.strip().split(',')))) # list of list of coords

# initialising means, k random points from data
means=[points_coords[randrange(len(points_coords))], points_coords[randrange(len(points_coords))], points_coords[randrange(len(points_coords))]]

alloc=[None]*len(points_coords)
n=0
while n<10:
  for i in range(len(points_coords)):
    point=points_coords[i]
    d=[None] * k
    # distances of a point to each cluster
    d[0]=sqrt((point[0]-means[0][0])**2 + (point[1]-means[0][1])**2)
    d[1]=sqrt((point[0]-means[1][0])**2 + (point[1]-means[1][1])**2)
    d[2]=sqrt((point[0]-means[2][0])**2 + (point[1]-means[2][1])**2)
    # allocate point to nearest cluster
    alloc[i]=d.index(min(d))
  for i in range(k):
    # get points in cluster i
    alloc_points_coords=[p for j, p in enumerate(points_coords) if alloc[j] == i]
    # mean (x,y) of cluster i
    new_mean=(sum([a[0] for a in alloc_points_coords]) / len(alloc_points_coords), sum([a[1] for a in alloc_points_coords]) / len(alloc_points_coords))
    means[i]=new_mean
  n=n+1

# print results
for i in range(k):
  alloc_points_coords=[p for j, p in enumerate(points_coords) if alloc[j] == i]
  print("Cluster " + str(i) + " is centred at " + str(m[i]) + " and has " + str(len(alloc_points_coords)) + " points.")