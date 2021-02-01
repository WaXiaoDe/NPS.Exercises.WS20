import csv
import os
import matplotlib.pyplot as plt
import numpy as np 
import math

# This function creates the output csv file as required 
def writeCsv(name,data):
    # First, we generate a 'temp.csv' to store the resulting data
    with open('temp.csv', 'w', newline='\n') as output_file:
        writer = csv.writer(output_file, delimiter=',')
        for p in data:
            writer.writerow(p)
            #writer.writerow(point)
    output_file.close()
    
    # Then, we copy the content of 'temp.csv' to the target file and
    # replace every ',' with ', ' 
    with open('temp.csv') as infile, open(name, 'w') as outfile:
        for line in infile:
            line = line.replace(",", ", ")
            outfile.write(line)
    # Finally, the 'temp.csv' will be deleted
    os.remove('temp.csv')


# Define the function for graphical illustration for binary classified data
def plot_binary_classified_data(X,Y):
    snow_x = []
    snow_y = []
    black_x = []
    black_y = []
    for i in range(len(Y)):
        if Y[i] == 1:
            snow_x.append(X[i][0])
            snow_y.append(X[i][1])
        else: 
            black_x.append(X[i][0])
            black_y.append(X[i][1])
    plt.scatter(black_x,black_y,s=4,color="black")
    plt.scatter(snow_x,snow_y,s=4,color="silver")

    plt.show()


# Different functions for reading Data from a csv file:

def read_data_without_label(name):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    Path_csv = os.path.join(THIS_FOLDER, name)
    with open(Path_csv) as File:
        Data = csv.reader(File, delimiter=';')
        pointSet = []
        # convert string in float
        for point in Data:
            for i in range(len(point)):
                point[i] = point[i]
            pointSet.append(point)
    File.close()
    return pointSet

def read_binary_classified_data(name):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    Path_csv = os.path.join(THIS_FOLDER, name)
    with open(Path_csv) as File:
        Data = csv.reader(File, delimiter=',')
        pointSet = []
        for point in Data:
            for i in range(len(point)):
                point[i] = float(point[i])
            #pointSet.append([ point[0], np.array(point[1:]) ])
            pointSet.append([ point[0], point[1:]])
    File.close()
    return pointSet


# Defining different kernel functions: 

def v_unit_ball(d,norm_name):
    if norm_name == 'euclidean':
        return (np.pi**(d/2))/math.gamma(d/2+1)
    elif norm_name =='supremum':
        return 2**d

def moving_window_kernel(r):
    if r>=0 and r<1 :
        return 1
    else:
        return 0

def triangular_kernel(r):
    if r>=0 and r<=1 :
        return 1-r
    else:
        return 0

def epanechnikov_kernel(r):
    if r>=0 and r<=1 :
        return 1-r**2
    else:
        return 0

def gaussian_kernel(r):
    return np.exp(-1*r*r)

def norminated_kernel_functions(function_name,d,norm_name):
    functions = { 'moving_window': lambda x: moving_window_kernel(x)/v_unit_ball(d,norm_name) , \
                         'triangular': lambda x: (d+1)*triangular_kernel(x)/v_unit_ball(d,norm_name) , \
                         'epanechnikov': lambda x: (d+2)*epanechnikov_kernel(x)/(2*v_unit_ball(d,norm_name)) ,\
                         'gaussian': lambda x: 2*gaussian_kernel(x)/(math.gamma(d/2)*v_unit_ball(d,norm_name)*d) }
    return functions[function_name]


# Defining norm functions 

def dist(function_name):
    
    def distance_sq(p1,p2):
        #d = p1.dot(p1) - 2*np.dot(p1,p2) + np.dot(p2,p2)
        #d = sum([(a-b)**2 for a,b in zip(p1,p2)])
        d = 0
        for a,b in zip(p1,p2):
            d += (a-b)**2
        return d**0.5

    def distance_max(p1,p2):
        maxi = 0
        for a,b in zip(p1,p2):
            c = abs(a-b)
            if c > maxi:
                maxi = c
        return maxi

    if function_name == 'euclidean':
        return distance_sq
    elif function_name == 'supremum':
        return distance_max

# Generating a set of grid points in [-1.5,1.5]^2

def grid_for_2_2(n):
    X = []
    Y = []
    liste = []
    for i in range(n+1):
        X.append(i/n*2.1-1.05)
        Y.append(i/n*2.1-1.05)
    for x in X:
        for y in Y:
            liste.append([x,y])
    return liste

#print(grid_for_2_2(50))