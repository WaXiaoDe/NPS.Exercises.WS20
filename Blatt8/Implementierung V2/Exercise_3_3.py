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
            point_in_grid[position][0] += p[0]
        else:
            point_in_grid[position] = [1,p[0]]

    def f_D_s(x):
        position = PositionFinding(x,grid_length)
        if position in point_in_grid:
            denominator = point_in_grid[position][0]
            numerator = point_in_grid[position][1]
            return numerator/denominator 
        else: 
            return 0 
         
    return f_D_s


def separatedata(data):
    i = 0
    lenght = len(data)
    datax = [0] * lenght
    datay = [0] * lenght
    while i < lenght:
        datax[i] = data[i][1]
        datay[i] = data[i][0]
        i = i + 1
    return [datax, datay]

def searchcell(x, s):
    x_np = np.array(x)
    x_1 = x_np/s
    x_2 = np.floor(x_1)
    x_3 = x_2*s
    cellmidle = x_3 + (s/2)
    return cellmidle

def sumdataincell(x,s,datax):
    amount = 0
    cellmidle = searchcell(x,s)
    datax_np = np.array(datax)
    for vec in datax_np:
        pos = vec - cellmidle
        if max((pos**2)**0.5) <= s:           #noch betrag nehmen von pos
            amount = amount + 1
    return amount

def sumlabelincell(x,s,datax,datay):
    index = 0
    value = 0
    dim = len(x)
    pos = [0] * dim
    posi = np.array(pos)
    datax_np = np.array(datax)
    datay_np = np.array(datay)
    cellmidle = np.array( searchcell(x,s) )
    lenght = len(datax)
    while index < lenght:
        posi = datax_np[index] - cellmidle
        if max((posi**2)**0.5) <= s:
            value = value + datay[index]
        index = index + 1
    return value

def histogram_least_squares_rule(datax,datay,s):
    
    def f_D_s(x):
        zaehler = sumlabelincell(x,s,datax,datay)
        nenner = sumdataincell(x,s,datax)
        if nenner == 0:
            return 0
        else:
            return zaehler/nenner
    
    return f_D_s


def exercise_3_3(name,s, printing=True):
    train_data = af.read_binary_classified_data(name+'.train.csv')
    test_data = af.read_binary_classified_data(name+'.test.csv')

    train_x , train_y = separatedata(train_data)
    test_x , test_y = separatedata(test_data)


    time_1 = time.time()

    f_D_s = histogram_least_squares_rule( train_x , train_y , s )

    time_2 = time.time()

    R_D = 0
    i = 1
    print("jetzt R_D")
    for p in train_data:
        print(i)
        R_D += ( p[0] - f_D_s(p[1]) )**2
        i += 1
    R_D =  R_D / len(train_data)

    time_3 = time.time()

    R_D_p = 0
    for p in test_data:
        R_D_p += ( p[0] - f_D_s(p[1]) )**2
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

    return [R_D,R_D_p, time_f_D_s ,time_R_D ,time_R_D_p ]
    

def result_comparison():
    l = []
    ss = [1,0.8,0.6,0.4,0.2,0.1,0.08,0.06,0.04,0.02,0.01,0.008,0.006,0.004,0.002,0.001]
    for s in ss:
        temp = [s]
        r = exercise_3_3('bank-marketing', s) 
        for entry in r : 
            temp.append(round(entry,5))
        l.append(temp)
    af.writeCsv('results.Exercise_3.3.csv',l)



#####     Execution Area     #####

#name = input("name: ")
#s = float( input("s: ") )

#exercise_3_3(name, s)

exercise_3_3('bank-marketing', 0.1)
