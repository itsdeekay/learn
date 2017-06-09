from pprint import pprint
import numpy as np

def reading_data(s):
    file = open(s)
    data =[]
    N = int(file.readline())
    K = int(file.readline())
                            
    for line in file:                                         
        line = line.rstrip()                                 
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
    probabilities = counts_of_unique_values.astype('float')/len(Y)
    for pb in probabilities:
        if pb != 0.0:
            current_entropy -= pb * np.log2(pb)
    return current_entropy
    

def information_gain(Y, attr):

    parent_entropy = entropy(Y)
    child_entropy = 0
    # We partition x, according to attribute values x_i
    unique_values, counts_of_unique_values = np.unique(attr, return_counts=True)
    probabilities = counts_of_unique_values.astype('float')/len(attr)

    # We calculate a weighted average of the entropy
    for pb, uv in zip(probabilities, unique_values):
        child_entropy -= pb * entropy(Y[attr == uv])

    return parent_entropy-child_entropy
    
def partition(x):
    r =[]
    unique_values, counts_of_unique_values = np.unique(x, return_counts=True)
    for n in range(N):
        for i in unique_values:
            if n
                r.add(i)
            else:
            
        

def is_pure(s):
    return len(set(s)) == 1

def recursive_split(x, y):
    # If there could be no split, just return the original set
    if is_pure(y) or len(y) == 0:
        return y

    # We get attribute that gives the highest mutual information
    gain = np.array([information_gain(y, x_attr) for x_attr in x.T])
    selected_attr = np.argmax(gain)

    # If there's no gain at all, nothing has to be done, just return the original set
    if np.all(gain < 1e-6):
        return y


    # We split using the selected attribute
    sets = partition(x[:, selected_attr],selected_attr)

    res = {}
    for k, v in sets.items():
        y_subset = y.take(v, axis=0)
        x_subset = x.take(v, axis=0)

        res["x_%d = %d" % (selected_attr, k)] = recursive_split(x_subset, y_subset)

    return res
    
N,K,data = reading_data("ticdata.txt")
X,Y,train_data,test_data = train_test(data,1000,K)
pprint(recursive_split(X, Y))