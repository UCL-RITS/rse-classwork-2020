"""This code implements the k-means clustering algorithm for 2 dimensions."""

from math import *
from random import *

lines = open('samples.csv', 'r').readlines()
points = []           # list to hold coordinates of points
for line in lines:
  values = map(float, line.strip().split(','))
  points.append(tuple(values))

k=3
means = [random.choice(points)] * k

alloc=[None]*len(points)
n=0
while n<10:
  for i in range(len(points)):
    p=points[i]
    d=[None] * k                                     # distance
    d[0]=sqrt((p[0]-means[0][0])**2 + (p[1]-means[0][1])**2)
    d[1]=sqrt((p[0]-means[1][0])**2 + (p[1]-means[1][1])**2)
    d[2]=sqrt((p[0]-means[2][0])**2 + (p[1]-means[2][1])**2)
    alloc[i]=d.index(min(d))
  for i in range(k):
    alloc_points=[p for j, p in enumerate(points) if alloc[j] == i]
    new_mean=(sum([a[0] for a in alloc_points]) / len(alloc_points), sum([a[1] for a in alloc_points]) / len(alloc_points))
    means[i]=new_mean
  n=n+1

for i in range(3):
  alloc_points=[p for j, p in enumerate(points) if alloc[j] == i]
  print("Cluster " + str(i) + " is centred at " + str(means[i]) + " and has " + str(len(alloc_points)) + " points.")