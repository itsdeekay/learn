import numpy as np

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
    np.random.shuffle(data)
    training, test = data[:n,:], data[n:,:]
    X = training[:n,:K]
    Y = training[:n,K]
    return X,Y,training,test


def entropy(Y):
    current_entropy = 0
    unique_values, counts_of_unique_values = np.unique(Y, return_counts=True)
    probabilities = counts.astype('float')/len(Y)
    for pb in probabilities:
        if pb != 0.0:
            current_entropy -= pb * np.log2(pb)
    return current_entropy
    

def information_gain(Y, attr):

    parent_entropy = entropy(Y)
    child_entropy = 0
    # We partition x, according to attribute values x_i
    unique_values, counts_of_unique_values = np.unique(attr, return_counts=True)
    probabilities = counts.astype('float')/len(attr)

    # We calculate a weighted average of the entropy
    for pb, uv in zip(probabilities, unique_values):
        child_entropy -= pb * entropy(Y[attr == uv])

    return parent_entropy-child_entropy
    
N,K,data = reading_data("ticdata.txt")
print(data[0])
X,Y,train_data,test_data = train_test(data,1000,K)
