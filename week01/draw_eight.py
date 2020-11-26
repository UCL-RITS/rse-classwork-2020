import math

import numpy as np
import matplotlib.pyplot as plt 

def make_figure():
    theta = np.arange(0, 4 * math.pi, 0.1)
    eight = plt.figure()
    axes = eight.add_axes([0, 0, 1, 1])
    axes.plot(0.5 * np.sin(theta), np.cos(theta / 2))
    return eight

import draw_eight
image = draw_eight.make_figure()