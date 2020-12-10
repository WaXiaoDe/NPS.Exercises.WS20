import numpy as np
import Assistant_Functions as af
import matplotlib.pyplot as plt 
import math
import Exercise_2_2 as dg
import matplotlib
from matplotlib import cm, colors




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






################   Execution area    ################
s = 1
'''
kernel_function_name = 'epanechnikov'
norm_name = 'euclidean'
kernel_result_for_2_2_ii( s, kernel_function_name , norm_name, plot=True, output=True )
'''

kernel_functions = ['moving_window', 'triangular', 'epanechnikov', 'gaussian',]
norms = ['euclidean','supremum']

for kernel_funtion in kernel_functions:
    for norm in norms:
        kernel_result_for_2_2_ii( s, kernel_funtion , norm, plot=True, output=True )
