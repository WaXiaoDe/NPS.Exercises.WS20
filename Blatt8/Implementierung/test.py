import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import math
import numpy as np 

x = np.linspace(np.pi*-1,np.pi,100)

def P35(x):
    if -1*np.pi<x and x<=-1*np.pi/2:
        return 1
    elif x<=0:
        return 1+x**2
    elif x<=np.pi/2:
        return -1
    else:
        return 1-x**2

f=np.vectorize(P35)
'''
y = f(x)

plt.plot(x,y)
plt.show()
'''
s = 0
for j in range(1,100000):
    s += 6/j/j

print(s-np.pi**2)
