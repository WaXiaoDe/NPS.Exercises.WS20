import numpy as np
import math
import Assistant_Functions as af
import time
import random 
from sklearn.neighbors import KNeighborsClassifier
import os

def profit_single_case(y,t):
    if t == -1:
        return 0
    elif y==1:
        return 95
    else:
        return -5

def merge_functions(function_lists):    
    def output(x):
        r = 0
        for f in function_lists:
            r += f(x)
        if r>= 0:
            return 1
        else: 
            return -1
    return output 

def profit_outsource_case(y,t):
    if t == -1:
        return 0
    elif y==1 : 
        return 87
    else:
        return -3


##########     Least Square Histogram     ##########

def PositionFinding(point,grid_length):
    
    position = []
    for i in range(len(point)):
        position.append( math.floor(point[i] /grid_length)*grid_length )
    return tuple(position)  

def histogram_least_square( data , grid_length ):

    point_in_grid = {}

     # Locating the points
    for p in data:
        position = PositionFinding(p[1],grid_length)
        if position in point_in_grid:
            point_in_grid[position][0] += 1
            point_in_grid[position][1] += p[0]
        else:
            point_in_grid[position] = [1,p[0]]

    def f_D_s(x):
        position = PositionFinding(x,grid_length)
        if position in point_in_grid:
            return point_in_grid[position][1]/point_in_grid[position][0] 
        else: 
            return 0 
         
    return f_D_s

def profit_calculation_hist( data, f_D_s ):
    Profit = 0
    for p in data:
        #Profit +=  profit_single_case(p[0],f_D_s(p[1]))
        Profit +=  profit_outsource_case(p[0],f_D_s(p[1]))
    return Profit

def k_fold_cross_validation_hist( name , k , s ):
        
    whole_data = af.read_binary_classified_data(name)
    data_sets = []
    f_D_k = []
    for i in range(k):
        data_sets.append([])
    for p in whole_data:
        i = random.randint(0,k-1)
        data_sets[i].append(p)

    total_profit = 0
    for i in range(k):
        D_i = data_sets[i]
        D_i_p = []
        for j in range(k):
            if j != i:
                D_i_p = D_i_p + data_sets[j]
        f_D_i_p = histogram_least_square(D_i_p , s)
        f_D_k.append(f_D_i_p)
        total_profit += profit_calculation_hist(D_i , f_D_i_p )
    
    return total_profit/k , f_D_k

def k_fold_hist_comparison( name , s_list , k_list ):
    filename_train = os.getcwd() + '/bank-marketing/'+name + '.train.csv'
    filename_test = os.getcwd() + '/bank-marketing/'+name + '.test.csv'
    result  = []
    for k in k_list:
        print('k ',k)
        for s in s_list:
            print('s ',s)
            profit_train , f_D_k_list = k_fold_cross_validation_hist(filename_train , k , s)
            f_D_k = merge_functions(f_D_k_list)
            profit_test = profit_calculation_hist(af.read_binary_classified_data(filename_test) , f_D_k)
            print(k,s,profit_train,profit_test)
            result.append([k,s,profit_train,profit_test])
    af.writeCsv(name+'.k_fold_hist_comparison.csv',result)


##########     kNN     ##########

def predict_test_data_KNN(train_X, train_Y, test_data, k0):
    predict_label = []
    neigh = KNeighborsClassifier(n_neighbors=k0)
    neigh.fit(train_X, train_Y)
    for point in test_data:
        predict_label.append(neigh.predict([point])[0])
    def f_D_k(x):
        return(neigh.predict([x])[0])
    return predict_label,f_D_k


def k_fold_cross_validation_knn(name , k , k0):
    whole_data = af.read_binary_classified_data(name)

    data_sets = []
    for i in range(k):
        data_sets.append([])
    for p in whole_data:
        i = random.randint(0,k-1)
        data_sets[i].append(p)

    total_profit = 0
    function_list = []
    for i in range(k):
        print("fold :",i)
        D_i = data_sets[i]
        D_i_p = []
        for j in range(k):
            if j != i:
                D_i_p = D_i_p + data_sets[j]
        X_train , Y_train = af.separate_label(D_i_p)
        X_test , Y_test = af.separate_label(D_i)
        labels , f_D_k = predict_test_data_KNN(X_train, Y_train , X_test,k0)
        function_list.append(f_D_k)
        s = 0
        for n in range(len(labels)):
            #s += profit_single_case(Y_test[n],labels[n]) 
            s += profit_outsource_case(Y_test[n],labels[n])             
        total_profit += s
        print(s)


    return total_profit/k , function_list

def k_fold_knn_comparison(name , k_list , k0_list ):
    filename_train = os.getcwd()+'/bank-marketing/'+name+'.train.csv'
    filename_train = os.getcwd()+'/bank-marketing/'+name+'.test.csv'
    Train_X , Train_Y = af.separate_label(af.read_binary_classified_data(filename_train))
    result = []
    for k in k_list:
        for k0 in k0_list:
            print("k :",k)
            profit_train , function_list = k_fold_cross_validation_knn(filename_train , k , k0)
            f_D_k = merge_functions(function_list)
            profit_test = 0
            for i in range(len(Train_X)):
                #profit_test += profit_single_case(Train_Y[i],f_D_k(Train_X[i]))
                profit_test += profit_outsource_case(Train_Y[i],f_D_k(Train_X[i]))


            print(k,k0,profit_train, profit_test)
            result.append([k,k0,profit_train,profit_test])
    af.writeCsv(name +'.k_fold_knn_comparison.csv',result)










##########     Execution Area     ##########
s_list = [2,1,0.5,0.1,0.05,0.01,0.005,0.001]
k_list = [2,3,4,5,6,7,8,9,10]
k0_list = [1,2,3,4,5,6,7,8,9,10]

#k_fold_hist_comparison('bank_marketing.bc',s_list, k_list)
k_fold_knn_comparison('bank_marketing.bc',k_list, k0_list)




