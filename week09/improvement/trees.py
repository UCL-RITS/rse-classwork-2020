"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt

# Make a class to hold each branch
class Branch():
    def __init__(self, x_coord, y_coord, base_angle):
        self.x = x_coord
        self.y = y_coord
        self.base_angle = base_angle

# Set the length of the first branch (from 0,0 to 0,trunk_length)
trunk_length = 1

# Set up a list holding the end of the first branch/trunk
# First element is the x coordinate of the centre of the tree
# The second element is the length of the intial trunk (the height where the branches start)
# Third element is angle of the branch (radians, relative to vertical)
tree=[Branch(0, trunk_length, 0)]

# This scales the successive branches of the tree down in length
scale_factor = 0.6

# This is the number of times that the tree branches after the initial trunk
num_branches = 5

# Add a plot for the "trunk" branch
plt.plot([0,0],[0,trunk_length])

# Make the successive branches
for _ in range(num_branches):
    # Store all the branches from the current "end" here
    branches = []
    # Loop over each branch in the tree and add the child nodes
    for j in range(len(tree)):
        # For two sub branches, we go at -0.1 radians and +0.1 radians from the parent/lower branch
        for subbranch_angle in [-0.1, 0.1]:
            # Create the new branch and store
            new_node = Branch(
                tree[j].x + trunk_length * sin(tree[j].base_angle + subbranch_angle),
                tree[j].y + trunk_length * cos(tree[j].base_angle + subbranch_angle),
                tree[j].base_angle + subbranch_angle
            )
            branches.append(new_node)
        # Plot the branches we just created
        plt.plot([tree[j].x, branches[-2].x], [tree[j].y, branches[-2].y])
        plt.plot([tree[j].x, branches[-1].x], [tree[j].y, branches[-1].y])
    # Store the branches for the next iteration
    tree=branches
    # Reduce the trunk length for the next branches
    trunk_length *= scale_factor

plt.savefig('tree.png')