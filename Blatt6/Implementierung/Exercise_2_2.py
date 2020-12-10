import numpy as np
import matplotlib.pyplot as plt
import Assistant_Functions as af
import random
    


# This function generates the desired normal distribution data and 
# it can also plot or output the data. 
# distrX is a list of two elements [ list of mean values, covariance matrix]
def MixingThreeNormalDistr( size , distr1, distr2, distr3 , plot = False , output = False ): 

    component_size = int(size/3)
    data1 = np.random.multivariate_normal(distr1[0], distr1[1], component_size)
    data2 = np.random.multivariate_normal(distr2[0], distr2[1], component_size)
    data3 = np.random.multivariate_normal(distr3[0], distr3[1], component_size)

    data = np.vstack([data1,data2,data3])
    X = []
    Y = []
    for i in range(size):
        X.append(data[i][0])
        Y.append(data[i][1])

    if plot:
        plt.scatter(X,Y)
        plt.show()

    if output: 
        af.writeCsv("Exercise2.2_i-"+str(size)+".csv" , data)

    return data


def EuclideanBall(size, plot = False , output = False):

    data = []
    X = []
    Y = []

    while len(data)<size:
        xCoord,yCoord = np.random.random_sample(2)
        xCoord = xCoord*2-1
        yCoord = yCoord*2-1
        if xCoord**2+yCoord**2 < 1:
            X.append(xCoord)
            Y.append(yCoord)
            data.append([xCoord,yCoord])
        
    if plot:
        plt.scatter(X,Y)
        plt.show()

    if output: 
        af.writeCsv("Exercise2.2_ii-"+str(size)+".csv" , data)

    return data



##############################################################################

# Execution area: 
size = 2000

EuclideanBall(size, plot = False , output=True)

distr1 = [ [ 0 , np.e*3 ] , [ [5,0.5] , [0.5 , 2]  ]  ]
distr2 = [ [ np.pi , 1 ] , [ [np.log(3),1.8] , [1.8 , 5]  ]  ]
distr3 = [ [ -8 , -4 ] , [ [np.log(size),2] , [2 , 6.6666]  ]  ]
#MixingThreeNormalDistr( size , distr1, distr2, distr3 , plot = False , output = True )
