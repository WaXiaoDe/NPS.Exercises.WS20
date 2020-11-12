import numpy as np
import matplotlib.pyplot as plt
import B1_assistant_functions as af
from sklearn.neighbors import KNeighborsClassifier



# Define a function that imports the data from the csv file
def import_data(name):
    data = af.read_csv(name)
    X = []
    Y = []
    for line in data:
        X.append(line[1])
        Y.append(line[0])
    return X,Y



# Define a function that trains a new data set with kNN method for given
# train data with label, test data and given k
def predict_test_data(train_X, train_Y, test_data, k):
    predict_label = []
    neigh = KNeighborsClassifier(n_neighbors=k)
    neigh.fit(train_X, train_Y)
    for point in test_data:
        predict_label.append(neigh.predict([point]))
    return predict_label



# Define a function that generates a test data set with correct label
# and store it
def chess_board_points(m,n):
    X = np.random.uniform(size = (n,2) )
    Y = []
    for point in X:
        Y.append( (-1)**(int(point[0]*m)+int(point[1]*m)) )
    # Now for train data output
    newformat_data = []
    for i in range(len(Y)):
        newformat_data.append([Y[i],X[i][0],X[i][1]])
    af.writeCsv('chess-test.csv', newformat_data)
    return X,Y


# Define the loss function for binary classification: 
def L_class(y,t):
    if y*t == 1:
        return 0
    else:
        return 1


# Define a function that calculates the empirical risk for given 
# train data with label, test data and given k
def empirical_risk(train_X, train_Y, test_X, test_Y, k):
    n = len(test_Y)
    predict_label = predict_test_data(train_X, train_Y, test_X, k)
    s = sum([L_class(test_Y[i],predict_label[i]) for i in range(n)])
    return s/n


# Define a function that finds the  k with minimal emprical risk for a 
# given range of k
def find_k_star(train_X, train_Y, test_X, test_Y, k_range):
    # ？
    k_star = 99999999999999
    k_star_list = []
    min_risk = 999999999
    risk_list = []
    min_risk_list = []
    for k in range(1,k_range):
        temp_risk = empirical_risk(train_X, train_Y, test_X, test_Y, k)
        risk_list.append(temp_risk)
        if temp_risk <= min_risk:
            k_star = k
            min_risk = temp_risk
        k_star_list.append(k_star)
        min_risk_list.append(min_risk)
        print(k,k_star,min_risk)
    return [k_star, min_risk, k_star_list, min_risk_list, risk_list ]




# Execution area

m = 4
n = 5000

# test_X, test_Y = chess_board_points(m,n)

k_range = 100

train_X, train_Y = import_data("chess-4-0.1-10000.csv")
test_X, test_Y = import_data("chess-test.csv")
k_star, min_risk, k_star_list, min_risk_list, risk_list = find_k_star(train_X, train_Y, test_X, test_Y, k_range)

newformat_data = []
for i in range(1, k_range):
    newformat_data.append([ i, risk_list[i-1], min_risk_list[i-1], k_star_list[i-1] ])
af.writeCsv('RESULT.csv', newformat_data)

print(k_star,min_risk)
#print(k_star, min_risk, k_star_list, min_risk_list, risk_list)



'''
for k in [1,50,100,300]:
    plt.title('Prediction for k='+str(k))
    af.plot_data(test_data, predict_test_data(train_X,train_Y,test_data,k))
'''


