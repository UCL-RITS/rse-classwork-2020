from matplotlib import pyplot as plt 

from math import sin, cos, pi
my_fig = plt.plot([sin(pi * x / 100.0) for x in range(100)])
