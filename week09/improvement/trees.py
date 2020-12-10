"""This code produces a tree-like plot."""

from math import sin, cos, pi
from matplotlib import pyplot as plt

# This is the length of the first branches of the tree, and is scaled
# down for the following branches
base_length = 1

# Length of the initial vertical branch
trunk_length = 1

# How many times the tree should split
num_branches = 5

# First element is the x coordinate of the second element in the tree
# Second element is the y-height of the second element in the tree
# Angle of the second element in the tree (clockwise, relative to vertical)
tree_branch = [[0, trunk_length, 0]]

# Plot the initial vertical "trunk"
plt.plot([0,0],[0,trunk_length])

for _ in range(num_branches):
    tree = []
    for j in range(len(tree_branch)):
        tree.append([tree_branch[j][0]+base_length*sin(tree_branch[j][2]-0.1), tree_branch[j][1]+base_length*cos(tree_branch[j][2]-0.1), tree_branch[j][2]-0.1])
        tree.append([tree_branch[j][0]+base_length*sin(tree_branch[j][2]+0.1), tree_branch[j][1]+base_length*cos(tree_branch[j][2]+0.1), tree_branch[j][2]+0.1])
        plt.plot([tree_branch[j][0], tree[-2][0]],[tree_branch[j][1], tree[-2][1]])
        plt.plot([tree_branch[j][0], tree[-1][0]],[tree_branch[j][1], tree[-1][1]])
    tree_branch = tree
    base_length *= 0.6


plt.savefig('tree.png')