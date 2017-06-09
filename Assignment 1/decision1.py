import numpy as np
import time

number_of_nodes = 0
def entropy(y):
    N = len(y)
    s1 = (y == 1).sum()

    if 0 == s1 or N == s1:
        return 0
    p1 = float(s1) / N
    p0 = 1 - p1

    return -p0 * np.log2(p0) - p1 * np.log2(p1)


def information_gain(x, y, split):
    y0 = y[x < split]
    y1 = y[x >= split]
    N = len(y)
    y0len = len(y0)

    if y0len == 0 or y0len == N:
        return 0

    p0 = float(len(y0)) / N
    p1 = 1 - p0
    ig = entropy(y) - p0 * entropy(y0) - p1 * entropy(y1)
    return ig


class Node:
    def __init__(self, depth=0, max_depth=None):
        self.depth = depth
        self.max_depth = max_depth

    def fit(self, X, Y):
        if len(Y) == 1 or len(set(Y)) == 1:
            self.col = None
            self.split = None
            self.right = None
            self.left = None
            self.prediction = Y[0]
        else:
            D = X.shape[1]
            cols = range(D)

            max_ig = 0
            best_col = None
            best_split = None

            for col in cols:
                ig, split = self.find_split(X, Y, col)
                if ig > max_ig:
                    max_ig = ig
                    best_col = col
                    best_split = split

            if max_ig == 0:
                self.col = None
                self.split = None
                self.right = None
                self.left = None
                self.prediction = np.round(Y.mean())
            else:
                self.col = best_col
                self.split = best_split

                if self.depth == self.max_depth:
                    self.right = None
                    self.left = None

                    self.prediction = [
                        np.round(Y[X[:, best_col] < self.split].mean()),
                        np.round(Y[X[:, best_col] >= self.split].mean()),
                    ]
                else:
                    left_idx = (X[:, best_col] < self.split)
                    xleft = X[left_idx]
                    yleft = Y[left_idx]

                    self.left = Node(depth=self.depth + 1, max_depth=self.max_depth)
                    self.left.fit(xleft, yleft)

                    # -------

                    right_idx = (X[:, best_col] >= self.split)
                    Xright = X[right_idx]
                    Yright = Y[right_idx]

                    self.right = Node(depth=self.depth + 1, max_depth=self.max_depth)
                    self.right.fit(Xright, Yright)

    def find_split(self, X, Y, col):
        x_values = X[:, col]
        sort_idx = np.argsort(x_values)
        x_values = x_values[sort_idx]
        y_values = Y[sort_idx]

        boundaries = np.nonzero(y_values[:-1] != y_values[1:])[0]
        best_split = None
        max_ig = 0

        for i in boundaries:
            split = (x_values[i] + x_values[i + 1]) / 2
            ig = information_gain(x_values, y_values, split)
            if ig > max_ig:
                max_ig = ig
                best_split = split

        return max_ig, best_split

    def predict_one(self, x):
        if self.col is not None and self.split is not None:
            feature = x[self.col]
            if feature < self.split:
                if self.left:
                    p = self.left.predict_one(x)
                else:
                    p = self.prediction[0]
            else:
                if self.right:
                    p = self.right.predict_one(x)
                else:
                    p = self.prediction[1]
        else:
            p = self.prediction
        return p

    def predict(self, X):
        N = len(X)
        P = np.zeros(N)
        for i in range(N):
            P[i] = self.predict_one(X[i])
        return P


class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, Y):
        self.root = Node(max_depth=self.max_depth)
        self.root.fit(X, Y)

    def predict(self, X):
        return self.root.predict(X)

    def score(self, X, Y):
        P = self.root.predict(X)
        return np.mean(P == Y)


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

if __name__ == '__main__':
    
    N,K,data = reading_data('ticdata.txt')
    X,Y,training_data,test_data = train_test(data,1000,K)
    Xtest = test_data[:,:K]
    Ytest = test_data[:,K]
    print(len(Xtest))
    model = DecisionTree()
    t0 = time.time()
    model.fit(X, Y)

    print 'Training time: ',+ (time.time() - t0)

    t0 = time.time()
    print 'Training accuracy: ', model.score(X, Y)
    print 'Time to compute train accuracy: ', (time.time() - t0), 'Train size: ', len(Y)

    t0 = time.time()
    print 'Test accuracy: ', model.score(Xtest, Ytest)
    print 'Time to compute test accuracy: ', (time.time() - t0), 'Test size: ', len(Ytest)