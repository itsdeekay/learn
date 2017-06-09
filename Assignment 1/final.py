import numpy as np
import time
import sys
from random import randint
from copy import deepcopy
import copy


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
    return X,Y,training_data,testing_data

def entropy(y):
    current_entropy = 0
    unique_values, counts_of_unique_values = np.unique(Y, return_counts=True)
    probabilities = counts_of_unique_values.astype('float')/len(Y)
    for pb in probabilities:
        if pb != 0.0:
            current_entropy -= pb * np.log2(pb)
    return current_entropy


def information_gain(x, y, split):
    y_left = y[x < split]
    y_right = y[x >= split]
    N = len(y)
    y_left_len = len(y_left)

    if y_left_len == 0 or y_left_len == N:
        return 0

    p_left = float(len(y_left)) / N
    p_right = 1 - p_left
    IG = entropy(y) - p_left * entropy(y_left) - p_right * entropy(y_right)
    return IG
    
class Node:
    def __init__(self, depth=0, max_depth=None):
        self.depth = depth
        self.max_depth = max_depth
        self.value = None
        self.attr = None
        self.split = None
        self.right_node = None
        self.left_node = None
        self.parent = None
        self.reached = 0
        
    def fit(self, X, Y,parent):
        self.parent = parent
        if len(Y) == 1 or len(set(Y)) == 1:
            self.attr = None
            self.split = None
            self.right_node = None
            self.left_node = None
            self.value = Y[0]
        else:
            number_of_attributes = X.shape[1]
            attributes = range(number_of_attributes)
            maximum_IG = 0
            best_attr = None
            best_split = None

            for atr in attributes:
                IG, split = self.find_split(X, Y, atr)
                if IG > maximum_IG:
                    maximum_IG = IG
                    best_attr = atr
                    best_split = split

            
            if maximum_IG == 0:
                self.attr = None
                self.split = None
                self.right_node = None
                self.left_node = None
                self.value = np.round(Y.mean())
            else:
                global number_attr
                number_attr[best_attr] +=1
                self.attr = best_attr
                self.split = best_split
                if self.depth == self.max_depth:
                    self.right_node = None
                    self.left_node = None
                    self.value = np.round(Y.mean())

                else:
                    left_idx = (X[:, best_attr] < self.split)
                    Xleft = X[left_idx]
                    Yleft = Y[left_idx]

                    self.left_node = Node(depth=self.depth + 1, max_depth=self.max_depth)
                    self.left_node.fit(Xleft, Yleft,self)

                    # -------

                    right_idx = (X[:, best_attr] >= self.split)
                    Xright = X[right_idx]
                    Yright = Y[right_idx]

                    self.right_node = Node(depth=self.depth + 1, max_depth=self.max_depth)
                    self.right_node.fit(Xright, Yright,self)

    def find_split(self, X, Y, attr):
        x_values = X[:, attr]
        sort_idx = np.argsort(x_values)
        x_values = x_values[sort_idx]
        y_values = Y[sort_idx]
        boundaries = np.nonzero(y_values[:-1] != y_values[1:])[0]
        best_split = None
        maximum_IG = 0

        for i in boundaries:
            split = (x_values[i] + x_values[i + 1]) / 2
            ig = information_gain(x_values, y_values, split)
            if ig > maximum_IG:
                maximum_IG = ig
                best_split = split

        return maximum_IG, best_split

    def predict_one(self, x):
        if self.attr is not None and self.split is not None:
            feature = x[self.attr]
            if feature < self.split:
                if self.left_node:
                    p = self.left_node.predict_one(x)
                else:
                    p = self.value
            else:
                if self.right_node:
                    p = self.right_node.predict_one(x)
                else:
                    p = self.value
        else:
            p = self.value
        return p

    def predict(self, X):
        N = len(X)
        P = np.zeros(N)
        for i in range(N):
            P[i] = self.predict_one(X[i])
        return P
 
                    
    def leaf_nodes(self,X,Y,Xtest,Ytest):
        global s1,model,number_of_nodes,terminal_nodes
        if self.left_node:
            self.left_node.leaf_nodes(X,Y,Xtest,Ytest)
        if self.right_node:
            self.right_node.leaf_nodes(X,Y,Xtest,Ytest)
        if self.parent is not None and self.parent.reached ==0 :
            temp_node = Node()
            temp_node = deepcopy(self.parent)
            left_idx = (X[:, self.parent.attr] < self.parent.split)
            right_idx = (X[:, self.parent.attr] >= self.parent.split)
            Yleft = Y[left_idx]
            Yright = Y[right_idx]
            YR = np.concatenate((Yleft, Yright))
            self.parent.left_node = None
            self.parent.right_node = None
            self.parent.attr = None
            self.parent.split = None
            self.parent.reached = 1
            self.parent.value = np.round(YR.mean())
            number_of_nodes = 0
            terminal_nodes = 0
            model.non()
            print  number_of_nodes
            print terminal_nodes
            temp = model.score(Xtest,Ytest)
            print temp
            temp = np.round(temp * 1000) / 1000.0
            if temp>=s1:
                s1 = temp
                print s1
                #self.parent.leaf_nodes(model,X,Y,Xtest,Ytest)
            else:
                self.parent = deepcopy(temp_node)
                self.parent.reached = 1
        
    def nl_nodes(self):
        global leaf_node
        if self.left_node is not None and self.right_node is not None:
            leaf_node.append(self)
        if self.left_node:
            self.left_node.nl_nodes()
        if self.right_node:
            self.right_node.nl_nodes()
    
    def non(self):
        global number_of_nodes
        global terminal_nodes
        number_of_nodes +=1
        if self.left_node is None and self.right_node is None:
            terminal_nodes+=1
        if self.left_node:
            self.left_node.non()
        if self.right_node:
            self.right_node.non()
    
def prun(model,X,Y,Xtest,Ytest):
    global leaf_node,s1
    model.nl_nodes()
    max_accuracy=s1
    max_i =-1
    max_val = -1
    ii = 0
    for i in leaf_node:
        left_t = copy.copy(i.left_node)
        right_t = copy.copy(i.right_node)
        left_idx = (X[:, i.attr] < i.split)
        right_idx = (X[:, i.attr] >= i.split)
        Yleft = Y[left_idx]
        Yright = Y[right_idx]
        YR = np.concatenate((Yleft, Yright))
        i.left_node = None
        i.right_node = None
        i.value = np.round(YR.mean())
        temp = model.score(Xtest,Ytest)
        temp = np.round(temp * 1000) / 1000.0
        if temp>max_accuracy:
            max_accuracy = temp
            max_i = ii
            max_val = np.round(YR.mean())
        i.left_node = left_t
        i.right_node = right_t
        i.value = None
        
        ii+=1
    print max_accuracy
    print max_i
    print max_val
    leaf_node[max_i].left_node = None
    leaf_node[max_i].right_node = None
    leaf_node[max_i].value = int(max_val)
    
              
         
class DT:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        
    def fit(self, X, Y):
        self.root = Node()
        self.root.fit(X, Y, parent=None)

    def score(self, X, Y):
        P = self.root.predict(X)
        return np.mean(P == Y)
        
    def predict(self, X):
        return self.root.predict(X)
    
    def leaf_nodes(self,X,Y,Xtest,Ytest):
        self.root.leaf_nodes(X,Y,Xtest,Ytest)
     
    def non(self):
        return self.root.non()
        
    def nl_nodes(self):
        return self.root.nl_nodes()
     
def add_noise(noise,Y,n):
    noice_data = int((noise*n)/100)
    for i in range(noice_data):
        r = randint(0,n-1)
        if Y[r] ==1:
            Y[r] = 0
        else:
            Y[r] = 1
    return Y


    

N,K,data = reading_data('ticdata.txt')
n =1000
X,Y,training_data,test_data = train_test(data,n,K)
Xtest = test_data[:,:K]
Ytest = test_data[:,K]
number_of_nodes = 0
terminal_nodes = 0
number_attr = np.zeros(K)
model = DT()
t0 = time.time()

arg = int(sys.argv[1])
if arg==1:
    model.fit(X, Y)
    model.non()
    print ''
    print 'Number of Nodes: ', number_of_nodes
    print ''
    print 'Number of Terminal Nodes: ', terminal_nodes
    print 'Number of times an attribute is used as the splitting function'
    print ''
    print 'Training accuracy: ', model.score(X, Y)
    print ''
    print 'Test accuracy: ', model.score(Xtest, Ytest)
    print ''
    #for i in range(K):
    #    print 'Attribute ',i, ' Counts: ',number_attr[i]


if arg ==2:
    noise = 0
    Y = add_noise(noise,Y,n)
    model.fit(X,Y)
    print 'Number of Nodes: ', number_of_nodes

if arg ==3:
    leaf_node = []
    model.fit(X,Y)
    model.non()
    print 'Number of Nodes: ', number_of_nodes
    print 'Number of terminal Nodes: ', terminal_nodes
    s = model.score(Xtest,Ytest)
    s = np.round(s * 1000) / 1000.0
    print 'Current Score: ',s
    print 'Pruning Starts...'
    s1 = s
    prun(model,X,Y,Xtest,Ytest)
    s = model.score(Xtest,Ytest)
    s = np.round(s * 1000) / 1000.0
    print 'New Score: ', s
    number_of_nodes = 0
    terminal_nodes = 0
    model.non()
    print 'Number of Nodes in Pruned tree: ',number_of_nodes
    print 'Number of terminal Nodes: ', terminal_nodes

