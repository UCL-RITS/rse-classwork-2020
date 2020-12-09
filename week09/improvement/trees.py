"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt
s=1
d=[[0,1,0]]
plt.plot([0,0],[0,1])
for i in range(5):
    n=[]
    for j in range(len(d)):
        n.append([d[j][0]+s*sin(d[j][2]-0.1), d[j][1]+s*cos(d[j][2]-0.1), d[j][2]-0.1])
        n.append([d[j][0]+s*sin(d[j][2]+0.1), d[j][1]+s*cos(d[j][2]+0.1), d[j][2]+0.1])
        plt.plot([d[j][0], n[-2][0]],[d[j][1], n[-2][1]])
        plt.plot([d[j][0], n[-1][0]],[d[j][1], n[-1][1]])
    d=n
    s*=0.6
plt.savefig('tree.png')