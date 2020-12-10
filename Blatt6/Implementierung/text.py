import numpy as np
import Assistant_Functions as af
import matplotlib.pyplot as plt 
import math
import Exercise_2_2 as dg
import matplotlib
from matplotlib import cm, colors



kernel_function_name = 'moving_window'
kernel_function_name = 'triangular'
kernel_function_name = 'epanechnikov'
#kernel_function_name = 'gaussian'
norm_name = 'euclidean'

'''
data = af.read_data_without_label('Test_n_2000_s_0.01_'+ kernel_function_name + '_' + norm_name +'.csv')

s = 0
n = 0
for p in data:
    s += p[0]
    if p[0]!=0:
        n +=1

print(s/math.pi/n,n)
'''

test_data = af.grid_for_2_2(50)
X = []
Y = []
hist = []

data = af.read_data_without_label('Kernel_result_2.2_s_0.01_epanechnikov_euclidean.csv')
for i in range(len(test_data)):
    hist.append(data[i][0])
    X.append(test_data[i][0])
    Y.append(test_data[i][1])
    print(X[i],Y[i],hist[i])

s = 0.01

fig, ax = plt.subplots()
fig.set_size_inches(8, 6.4)

norm = matplotlib.colors.Normalize(vmin=0, vmax=2)
cmap = cm.get_cmap('ocean', 256)
newcolors = cmap(np.linspace(0, 1, 300))[:256]
newcmp = colors.ListedColormap(newcolors)
a = ax.scatter(X, Y, norm = norm, marker='s', cmap=cmap.reversed(), c=hist ,alpha=0.85)
plt.title("Kernel result for 2.2 s={} {} {}".format(s, kernel_function_name ,norm_name))
plt.colorbar(a)
plt.savefig('Kernel_result_2.2_s_'+str(s)+'_'+kernel_function_name+'_'+norm_name+'.eps')
plt.show()