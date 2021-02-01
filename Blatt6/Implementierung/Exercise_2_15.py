import numpy as np
import Assistant_Functions as af
import matplotlib.pyplot as plt 
import math
import Exercise_2_2 as dg
import matplotlib
from matplotlib import cm, colors
import os

# Defining the kernel density estimator: 
def kernel(data, s, kernel_function_name , norm_name):
    distance = af.dist(norm_name)
    d = len(data[0])
    n = len(data)
    K = af.norminated_kernel_functions(kernel_function_name,d,norm_name)

    def h_D_K_s (x):
        summe = 0
        for p in data:
            summe += K( distance(x,p)/s )
        return (summe/n)/(s**d)
    return h_D_K_s

# Visualising results: 
def kernel_result_for_2_2_ii( s, kernel_function_name , norm_name, plot=False, output=False ):
    data = af.read_data_without_label('Exercise2.2_ii-10000.csv')
    test_data = af.grid_for_2_2(50)
    #print(test_data)
    h = kernel(data, s, kernel_function_name , norm_name)

    X = []
    Y = []
    hist = []
    output_data=[]
    for p in test_data:
        x = h(p)
        hist.append( x )
        print(x,p)
        X.append(p[0])
        Y.append(p[1])
        output_data.append([x])
    print(len(X),len(Y),len(hist))    

    if plot: 
        fig, ax = plt.subplots()
        fig.set_size_inches(8, 6.4)

        norm = matplotlib.colors.Normalize(vmin=0, vmax=2)
        cmap = cm.get_cmap('ocean', 256)
        a = ax.scatter(X, Y, norm = norm, marker='s', cmap=cmap.reversed(), c=hist)
        plt.title("Kernel result for 2.2 ii, s={}, {}, {}".format(s, kernel_function_name ,norm_name))
        plt.colorbar(a)
        plt.savefig('Kernel_result_2.2ii_s_'+str(s)+'_'+kernel_function_name+'_'+norm_name+'.eps')

    if output:
        af.writeCsv('Kernel_result_2.2_s_'+str(s)+'_'+kernel_function_name+'_'+norm_name+'.csv',output_data)

# Roughly computing the L1 norm of the estimated density

def rough_L1_A2_22(data):
    result = 0
    points = af.grid_for_2_2(50)
    for i in range(len(data)):
        if points[i][0]**2+points[i][1]**2 < 1:
            result += abs(data[i][0]-1/math.pi)*0.042*0.042
        else:
            result += data[i][0]
    return round(result,5)

def compute_store_rough_L1_A2_22():

    def name_mapping(file_name):
        result = []
        if file_name.find('moving')>-1:
            result.append('moving_window')
        else:
            result.append('gaussian')
        if file_name.find('eucl')>-1:
            result.append('euclidean')
        else:
            result.append('supremum')
        return result

    path = os.getcwd()+"//comparison. various s. gaussian vs moving window//"
    l = os.listdir(path)
    ll = []
    for file in l:
        if file.find('csv')>-1:
            ll.append(file)
    result = []
    for file in ll: 
        s = float(file[20:26][0:(file[20:26].find('_'))])
        kernel_type, norm_type = name_mapping(file)
        data = af.read_data_without_label(path+file)
        L1_norm = rough_L1_A2_22(data)
        result.append( [s,kernel_type,norm_type,L1_norm] )
    af.writeCsv('qualitative_comparison_results.csv',result)


################   Execution area    ################
'''
# Generating plots
kernel_functions = ['moving_window', 'triangular', 'epanechnikov', 'gaussian']
norms = ['euclidean','supremum']

for kernel_funtion in kernel_functions:
    for norm in norms:
        kernel_result_for_2_2_ii( s, kernel_funtion , norm, plot=True, output=True )
'''
'''

ss = [0.2, 0.1, 0.08, 0.06, 0.04, 0.03, 0.02, 0.01, 0.008 ]
sss = [0.006,0.004,0.002]
norms = ['euclidean','supremum']
for s in sss:
    for norm in norms:
        kernel_result_for_2_2_ii( s, 'moving_window' , norm, plot=True, output=True )
        kernel_result_for_2_2_ii( s, 'gaussian' , norm, plot=True, output=True )
'''

#compute_store_rough_L1_A2_22()

print(af.grid_for_2_2(50))