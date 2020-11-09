import numpy as np
import B1_assistant_functions as af

# Define the indicator function in the conditional distribution at x from X=[0,1)^2    
def ind_func(i,j,m,x):    
    if ( i/m <= x[0] and x[0]<(i+1)/m ) and ( j/m<=x[1] and x[1]< (j+1)/m ):
        return 1
    else:
        return 0

# Define the conditional distribution P(y=1|x) for x from X   
def reg_cond_dist_at_y_is_1(m,b,x):
    s = 0
    for i in range(m):
        for j in range(m):
            s = s + ((-1)**(i+j))*ind_func(i,j,m,x)
    return 0.5+(0.5-b)*s

# Define the distribution function for y at x from X
def dist_Y(t,m,b,x):
    if t < -1:
        return 0
    elif t<1:
        return 1-reg_cond_dist_at_y_is_1(m,b,x)
    else:
        return 1

# Define a function that generates respective y for given probability p under dist_Y(-1,m,b,x)
def y_generator(m,b,x):
    p = np.random.uniform(size=(1,1))
    if p <= dist_Y(-1,m,b,x):
        return -1
    else:
        return 1

# Define the function that generates the desired data set
def data_generator(n,b,m):
    Y = []
    x_set = np.random.uniform(size=(n,2))
    for x in x_set:
        Y.append(y_generator(m,b,x))
    return [x_set,Y]


# Define a function for train data output
def data_output(m,b,n,X,Y):
    newformat_data = []
    for i in range(len(Y)):
        newformat_data.append([Y[i],X[i][0],X[i][1]])
    af.writeCsv('chess-'+str(m)+'-'+str(b)+'-'+str(n)+'.csv', newformat_data)

# 

################################################################################################

# Execution area: 
m = 4
n = 10000
b = 0.1
X,Y = data_generator(n,b,m)


af.plot_data(X,Y)
data_output(m,b,n,X,Y)






