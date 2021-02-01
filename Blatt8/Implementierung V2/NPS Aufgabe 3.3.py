import numpy as np



def separatedata(data):
    i = 0
    lenght = len(data)
    datax = [0] * lenght
    datay = [0] * lenght
    while i <= lenght:
        datax[i] = data[i][1]
        datay[i] = data[i][0]
        i = i + 1

def searchcell(x, s):
    x_np = np.array(x)
    x_1 = x_np/s
    x_2 = np.floor(x_1)
    x_3 = x_2*s
    cellmidle = x_3 + (s/2)
    return cellmidle

def sumdataincell(x,s,datax):
    amount = 0
    cellmidle = searchcell(x,s)
    datax_np = np.array(datax)
    for vec in datax_np:
        pos = vec - cellmidle
        if max((pos**2)**0.5) <= s:           #noch betrag nehmen von pos
            amount = amount + 1
    return amount

def sumlabelincell(x,s,datax,datay):
    index = 0
    value = 0
    dim = len(x)
    pos = [0] * dim
    posi = np.array(pos)
    datax_np = np.array(datax)
    datay_np = np.array(datay)
    cellmidle = searchcell(x,s)
    lenght = len(datax)
    while index <= lenght:
        posi[index] = datax_np[index] - cellmidle[index]
        if max((posi**2)**0.5) <= s:
            value = value + datay[index]
        index = index + 1
    return value

def histogram_least_squares_rule(datax,datay,x,s):
    zaehler = sumlabelincell(x,s,datax,datay)
    nenner = sumdataincell(x,s,datax)
    if nenner == 0:
        return 0
    else:
        return zaehler/nenner
