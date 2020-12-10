"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt
s=1
d=[[0,1,0]]
plt.plot([0,0],[0,1])
for branch_number in range(5):
    n=[]
    for j in range(len(d)):
        direction_and_j_vector=d[j]
        n.append([direction_and_j_vector[0]+s*sin(direction_and_j_vector[2]-0.1), direction_and_j_vector[1]+s*cos(direction_and_j_vector[2]-0.1), direction_and_j_vector[2]-0.1])
        n.append([direction_and_j_vector[0]+s*sin(direction_and_j_vector[2]+0.1), direction_and_j_vector[1]+s*cos(direction_and_j_vector[2]+0.1), direction_and_j_vector[2]+0.1])
        plt.plot([direction_and_j_vector[0], n[-2][0]],[direction_and_j_vector[1], n[-2][1]])
        plt.plot([direction_and_j_vector[0], n[-1][0]],[direction_and_j_vector[1], n[-1][1]])
    d=n
    s*=0.6
plt.savefig('tree.png')