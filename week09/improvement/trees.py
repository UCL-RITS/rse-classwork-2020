"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt


'''

1. Create a function 
2. Define variables: levels (5), branch (d), length (s), index (j), n list_branches, direction (0.1), coefficient (0.6)
3. Inputs: levels, direction, length, branches
4. Outputs: plot and save image
'''


def create_tree_plot(levels, direction, length, branches, coefficient):

    plt.plot([0,0],[0,1])
    for i in range(levels): # 5 levels in the tree
        list_branches=[]
        for j in range(len(branches)):
            list_branches.append([branches[j][0]+length*sin(branches[j][2]-direction), \
                branches[j][1]+length*cos(branches[j][2]-direction), branches[j][2]-direction]) # branch left
            list_branches.append([branches[j][0]+length*sin(branches[j][2]+direction), \
                branches[j][1]+length*cos(branches[j][2]+direction), branches[j][2]+direction]) # branch right
            
            plt.plot([branches[j][0], list_branches[-2][0]],[branches[j][1], list_branches[-2][1]])
            plt.plot([branches[j][0], list_branches[-1][0]],[branches[j][1], list_branches[-1][1]])
        
        branches = list_branches
        length*=coefficient
    plt.savefig('tree.png')

if __name__ == "__main__":

    create_tree_plot(levels = 5, direction = 0.1, length = 1, branches = [[0,1,0]], coefficient = 0.6)

    
