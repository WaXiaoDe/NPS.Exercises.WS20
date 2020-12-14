import numpy as np
import math
import Assistant_Functions as af
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm, colors


def PositionFinding(point,origin,grid_length):
    x,y = point
    o1,o2 = origin
    n1 = math.floor((x-o1)/grid_length)
    n2 = math.floor((y-o2)/grid_length)
    n1 = o1 + (n1)*grid_length#(n1+0.5)*grid_length
    n2 = o1 + (n2)*grid_length #(n2+0.5)*grid_length
    return (n1,n2)

def Histrogram(data,grid_length,origin=(0,0),plot=False):

    # Preparation
    name = 'Exercise2.2_'+data+'-30000'
    point_list = af.read_data_without_label(name +'.csv')
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
        newcolors = cmap(np.linspace(0, 1, 300))[:256]
        newcmp = colors.ListedColormap(newcolors)
        a = ax.scatter(position_list_X, position_list_Y, marker='s',cmap=newcmp.reversed(), c=value_list,s=(grid_length*size*72*0.58/lrange)**2,alpha=0.85)
        plt.title("Histrogram for A2.2({}),  n = {}, s = {}".format(data,sample_size,grid_length))
        plt.colorbar(a)
        #plt.savefig(name + "-s"+str(grid_length)+'.eps',dpi = fig.dpi)
        plt.show()
    
    def h_D_s(x):
        p = PositionFinding(x,origin, grid_length)
        if p in point_in_grid.keys():
            return point_in_grid[p]
        else:
            return 0

    return h_D_s



def range_data(data):
    X = []
    Y = []
    for p in data:
        X.append(p[0])
        Y.append(p[1])
    return [math.ceil(max(X)),math.floor(min(X)),math.ceil(max(Y)),math.floor(min(Y))]

def grid_generate(origin, s, range_list):
    x_range = range_list[0]-range_list[1]
    y_range = range_list[2]-range_list[3]
    X = []
    Y = []
    for i in range(round(x_range/s)+1):
        X.append(i/round(x_range/s)*x_range+range_list[1])
    for i in range(round(y_range)+1):
        Y.append(i/round(y_range)*y_range+range_list[3])
    points = []
    for x in X:
        for y in Y:
            points.append([x,y])
    print('points',len(points))
    return points



def approx_L1(h,hh, D, s, origin):
    data_range = range_data(D)
    points = grid_generate(origin,s,data_range)
    summe = 0
    for p in points:
        summe += abs(h(p)-hh(p))*s*s
    return summe 


def h_2_2_ii(coord):
    if coord[0]**2 + coord[1]**2 < 1:
        return 1/math.pi
    else:
        return 0
    
##############################################################################

# Parameters
origin = (0,0)
grid_length = 0.01
#data_name = 'i'
data_name = 'ii'

#print(Histrogram(data,grid_length,origin,plot=False))





hh = Histrogram(data_name,grid_length,origin,plot=False)
data = af.read_data_without_label('Exercise2.2_ii-30000.csv')
output_list=[]
R = []
S = [1,0.5,0.25,0.1,0.075,0.05,0.025,0.01,0.0075,0.005,0.0025,0.001,0.00075,0.0005,0.00025,0.0001,0.000075,0.00005,0.000025,0.00001]
for s in S:
    r = approx_L1(h_2_2_ii,hh, data, s, origin)
    output_list.append([s,r])
    print(s,r)
    R.append(r)
af.writeCsv('ii_approx_L1_result.csv',output_list)



