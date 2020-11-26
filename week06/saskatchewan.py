import matplotlib.pyplot as plt 
from matplotlib.path import Path
import matplotlib.patches as patches

def show_fields(field1, field2):
    def vertices(left, bottom, right, top):
        verts = [(left, bottom),
                (left, top),
                (right, top),
                (right, bottom),
                (left, bottom)]
        return verts

    codes = [Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY]
    path1 = Path(vertices(*field1), codes)
    path2 = Path(vertices(*field2), codes)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch1 = patches.PathPatch(path1, facecolor='orange', lw=2)
    patch2 = patches.PathPatch(path2, facecolor='blue', lw=2)
    ax.add_patch(patch1)
    ax.add_patch(patch2)
    ax.set_xlim(0,5)
    ax.set_ylim(0,5)

#show_fields((1.,1.,4.,4.), (2.,2.,3.,3.))
show_fields((1.,1.,4.,4.), (2.,2.,4.5,4.5))

def overlap(field1, field2):
    left1, bottom1, top1, right1 = field1
    left2, bottom2, top2, right2 = field2

    overlap_left = max(left1, left2)
    overlap_bottom = max(bottom1, bottom2)
    overlap_right = min(right1, right2)
    overlap_top = min(top1, top2)

    overlap_height = max(0, (overlap_top-overlap_bottom))
    overlap_width = max(0, (overlap_right-overlap_left))

    return overlap_height*overlap_width