import cmath 
import numpy as np

x = cmath.rect(1,cmath.pi/6)
l = [x.real,x.imag]


t = [2,3,5]
t = t+l

print(x.real)
print((x**2).real)