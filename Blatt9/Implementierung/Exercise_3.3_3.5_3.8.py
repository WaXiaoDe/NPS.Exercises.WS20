import numpy as np
import math
import Assistant_Functions as af
import time


def PositionFinding(point,grid_length):
    
    position = []
    for i in range(len(point)):
        position.append( math.floor(point[i] /grid_length)*grid_length )
    return tuple(position)  

def histogram_least_square( data , grid_length ):

    point_in_grid = {}

     # Locating the points
    for p in data:
        position = PositionFinding(p[1],grid_length)
        if position in point_in_grid:
            point_in_grid[position][0] += 1
            point_in_grid[position][1] += p[0]
        else:
            point_in_grid[position] = [1,p[0]]

    def f_D_s(x):
        position = PositionFinding(x,grid_length)
        if position in point_in_grid:
            return point_in_grid[position][1]/point_in_grid[position][0] 
        else: 
            return 0 
         
    return f_D_s


def loss_choice(method,a):

    def L_class(y,t):
        if y*t >= 0:
            return 0
        else:
            return 1

    def L_ls(y,t):
        return (y-t)**2

    def L_alpha_class(y,t):
        if y == 1 and t<0:
            return 1-a
        elif y==-1 and t >= 0:
            return a
        else:
            return 0

    if method == 'ls':
        return L_ls 
    elif method == 'bc':
        return L_class 
    else: 
        return L_alpha_class 

def risk_calculation(name,s, method, a=0.5, printing=True):#
    train_data = af.read_binary_classified_data(name+'.train.csv')
    test_data = af.read_binary_classified_data(name+'.test.csv')

    L = loss_choice(method,a)

    time_1 = time.time()

    f_D_s = histogram_least_square( train_data, s )

    time_2 = time.time()

    R_D = 0
    for p in train_data:
        R_D +=  L(p[0],f_D_s(p[1]))
    R_D =  R_D / len(train_data)

    time_3 = time.time()

    R_D_p = 0
    for p in test_data:
        R_D_p += L(p[0],f_D_s(p[1]))
    R_D_p =  R_D_p / len(test_data)

    time_4 = time.time()

    time_f_D_s = time_2 - time_1
    time_R_D   = time_3 - time_2
    time_R_D_p = time_4 - time_3

    if printing:
        print("R_D(f) = {}".format(R_D))
        print("R_D'(f) = {}".format(R_D_p))
        print( "It takes {:.5f} seconds to calculate f_D_s.".format(time_f_D_s) )
        print( "It takes {:.5f} seconds to calculate R_D(f).".format(time_R_D) )
        print( "It takes {:.5f} seconds to calculate R_D'(f).".format(time_R_D_p) )

    return [R_D, R_D_p, time_f_D_s ,time_R_D ,time_R_D_p ]

def result_comparison(method,a=0.5):
    l = []
    ss = [2,1.5,1,0.8,0.6,0.4,0.2,0.1,0.08,0.06,0.04,0.02,0.01,0.008,0.006,0.004,0.002,0.001]
    for s in ss:
        temp = [s]
        r = risk_calculation('bank-marketing', s, method ) 
        for entry in r : 
            temp.append(round(entry,5))
        l.append(temp)
    af.writeCsv('results.'+method+'.csv',l)


#####     Execution Area     #####

#risk_calculation('bank-marketing', 2,'ls')
#result_comparison('bc')
result_comparison('a',0.25)

