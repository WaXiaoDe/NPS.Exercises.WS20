import numpy as np
import matplotlib.pyplot as plt
import B4_assistant_functions as af
import random
    


# This function generates the desired normal distribution data and 
# it can also plot or output the data. 
# distrX is a list of two elements [ list of mean values, covariance matrix]
def MixingThreeNormalDistr( size , distr1, distr2, distr3 , plot = False , output = False ): 

    data1 = np.random.multivariate_normal(distr1[0], distr1[1], size)
    data2 = np.random.multivariate_normal(distr2[0], distr2[1], size)
    data3 = np.random.multivariate_normal(distr3[0], distr3[1], size)

    data = []
    X = []
    Y = []
    for i in range(size):
        xCoord = data1[i][0]+data2[i][0]+data3[i][0]
        yCoord = data1[i][1]+data2[i][1]+data3[i][1]
        X.append(xCoord)
        Y.append(yCoord)
        data.append([xCoord,yCoord])

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
size = 10000

#EuclideanBall(size, plot = False , output=True)

distr1 = [ [ 0 , np.e ] , [ [1,0.5] , [0.5 , 2]  ]  ]
distr2 = [ [ np.pi , 1 ] , [ [np.log(3),0] , [0 , 5]  ]  ]
distr3 = [ [ -2 , 4 ] , [ [np.log(np.log(size)),2] , [2 , 6.6666]  ]  ]
MixingThreeNormalDistr( size , distr1, distr2, distr3 , plot = False , output = True )
