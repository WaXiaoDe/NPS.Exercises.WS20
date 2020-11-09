import numpy as np
import matplotlib.pyplot as plt
import B1_assistant_functions as af
    


# This function is a data generator with a modified
# n dimensional normal distribution 
def nDimModNormDistGenerator(dim, size = 10000 , mean = 0 , var = 1):
    # An assitant function that squeezes a point in R^n to [0,1]^n 
    # in a way such that R^n and [0,1]^n would be homeomorph. 
    def compress(p):
        dim = len(p)
        norme = np.dot(p,p)**0.5
        for i in range(dim):
            p[i] = p[i]/(1+norme)
            p[i] = p[i]/2 + 0.5
        return p
    # Generating normal distributed data points
    cov = np.identity(dim) * var
    mean = np.ones(dim) * mean
    data = np.random.multivariate_normal(mean, cov, size)
    # Compressing the data in the quader of same dimension homeomorphly
    for p in data:
        p = compress(p)

    return data

##############################################################################

# Execution area: 

for dim in range(1,6):
    data = nDimModNormDistGenerator(dim)
    af.writeCsv('CeylanWangZeng-'+str(dim)+'.train.csv', data)




