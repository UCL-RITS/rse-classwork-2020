"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt


scale_factor=1 # scale factor of branch length
current_node=[[0,1,0]] # initial node location[0][1], inital angle[2]
plt.plot([0,0],[0,1]) # plotting the stem of the tree


for i in range(5):
    nodes=[]
    for j in range(len(d)):
        # works out the location of the next nodes
        nodes.append([current_node[j][0]+scale_factor*sin(current_node[j][2]-0.1), current_node[j][1]+scale_factor*cos(current_node[j][2]-0.1), current_node[j][2]-0.1])
        nodes.append([current_node[j][0]+scale_factor*sin(current_node[j][2]+0.1), current_node[j][1]+scale_factor*cos(current_node[j][2]+0.1), current_node[j][2]+0.1])
        # plots the branches from previous nodes to next nodes
        plt.plot([current_node[j][0], nodes[-2][0]],[current_node[j][1], nodes[-2][1]])
        plt.plot([current_node[j][0], nodes[-1][0]],[current_node[j][1], nodes[-1][1]])
    current_node=nodes
    scale_factor*=0.6


plt.savefig('tree.png')