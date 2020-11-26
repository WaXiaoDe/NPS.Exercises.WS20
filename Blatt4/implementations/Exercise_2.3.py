import numpy as np
import math
import B4_assistant_functions as af
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm 


def PositionFinding(point,origin,grid_length):
    x,y = point
    o1,o2 = origin
    n1 = math.floor((x-o1)/grid_length)
    n2 = math.floor((y-o2)/grid_length)
    n1 = o1 + (n1+0.5)*grid_length
    n2 = o1 + (n2+0.5)*grid_length
    return (n1,n2)

def Histrogram(data,grid_length,origin=(0,0),plot=False):

    # Preparation
    name = 'Exercise2.2_'+data+'-10000'
    point_list = af.read_csv(name +'.csv')
    point_in_grid = {}
    sample_size = len(point_list)

    # Locating the points
    for p in point_list:
        position = PositionFinding(p,origin,grid_length)
        if position in point_in_grid:
            point_in_grid[position] += 1
        else:
            point_in_grid[position] = 1

    # regulerization
    position_list_X = []
    position_list_Y = []
    value_list = []
    for position in point_in_grid:
        point_in_grid[position] /=  sample_size * (grid_length**2)
        position_list_X.append(position[0])
        position_list_Y.append(position[1])
        value_list.append(point_in_grid[position])

    if plot:
        size = 9
        fig, ax = plt.subplots()
        fig.set_size_inches(size, size)
        xmin = min(position_list_X)
        xmax = max(position_list_X)
        ymin = min(position_list_Y)
        ymax = max(position_list_Y)
        lmin = min(xmin,ymin)
        lmax = max(xmax,ymax)*1.01
        lmin -= abs(0.1*lmin)
        lmax += 0.1*lmax
        lrange = lmax-lmin
        plt.xlim(lmin,lmax)
        plt.ylim(lmin,lmax)
        cmap = cm.get_cmap('ocean', 256)
        a = ax.scatter(position_list_X, position_list_Y, marker='s',cmap=cmap.reversed(), c=value_list,s=(grid_length*size*72*0.58/lrange)**2,alpha=0.85)
        plt.title("Histrogram for A2.2({}),  n = {}, s = {}".format(data,sample_size,grid_length))
        plt.colorbar(a)
        #plt.savefig(name + "-s"+str(grid_length)+'.eps',dpi = fig.dpi)
        plt.show()
    return point_in_grid


##############################################################################

# Parameters
origin = (0,0)
grid_length = 5
data = 'i'
#grid_length = 0.04
#data = 'ii'


Histrogram(data,grid_length,origin,plot=True)








