import numpy as np
from random import randint

def reading_data(s):
    file = open(s)
    data =[]
    N = int(file.readline())
    K = int(file.readline())
                            
    for line in file:                                         
        line = line.strip("\r\n")                                 
        data.append([int(x) for x in line.split('\t')]) 
    data = np.array(data) 
    
    return N,K,data

def train_test(data,n,K):
    data = data[:,:]
    data_len = len(data)
    training_data = np.empty([n,K],dtype=int)
    testing_data = np.empty([data_len-n,K],dtype=int)
    dataY1 = data[data[:,K]==1]
    dataY0 = data[data[:,K]==0]
    len_y1 = len(dataY1)/2
    len_y0 = len(dataY0)/2
    n1 = n-len_y1
    np.random.shuffle(dataY1)
    np.random.shuffle(dataY0)
    training_data = np.concatenate((dataY1[:len_y1, :],dataY0[:n1,:]))
    testing_data = np.concatenate((dataY1[len_y1:, :],dataY0[n1:,:]))
    training_data = np.array(training_data)
    testing_data = np.array(testing_data)
    np.random.shuffle(training_data)
    np.random.shuffle(testing_data)
    X = training_data[:n,:K]
    Y = testing_data[:n,K]
    print X.shape
    print Y.shape
    return X,Y,training_data,testing_data
    
N,K,data = reading_data('ticdata.txt')
n =1000
X,Y,training_data,test_data = train_test(data,n,K)