import numpy as np
import sklearn
import random
from sklearn import tree    
from sklearn.externals.six import StringIO

def outputData(t):
    global leaf_nodes,idx_leaf_nodes, current_a,features_considered    
    for each in leaf_nodes:
        idx = (idx_leaf_nodes == each)
        mean_data = arr[idx,:]
        mean  = np.mean(mean_data,axis=0)
        current_a[features_considered] = mean[:]
        means = ' '.join([str(a1) for a1 in current_a])
        divisor = np.sum(t.value[each])
        tval = np.asarray(t.value[each],dtype=np.float32)
        tval = tval / float(divisor)
        tvals = ' '.join([str(a1) for a1 in tval[0]])
        tppf_mean.write(means+'\n')
        tppf_ld.write(tvals+'\n')

if __name__ == "__main__":
    houses = [102,113,118]
    for p in range (len(houses)):
        for j in range (len(houses)):
            if(p!=j):
                
                current_input_directory = 'deepak/hh%d/hh%d_hh%d' %(houses[p],houses[p],houses[j])
                
                for i in range(16):
                    source_adj = '%s/Source_%d.txt' %(current_input_directory,i+1)
                    data = np.loadtxt(source_adj,delimiter=" ")
                    #np.random.shuffle(data)
                    tppf_mean = open(current_input_directory+'/Source_mean_%d.txt' %(i+1),'w')
                    tppf_ld = open(current_input_directory+'/Source_ld_%d.txt' %(i+1),'w')
                    total_size=data.size; # Number of elements
                    col=data[0].size; #No. of columns
                    row=total_size/col #No. of rows

                    for t in range(100):
                        mtry = 10
                        current_a = np.zeros(col-11)
                        rand_point = range(col-11)
                        random.shuffle(rand_point)
                        #Taking only sensor data while ignoring the temporal data.
                        features_considered = rand_point[0:mtry]
                        arr = data[:,0:col-1]
                        arr = arr[:,features_considered]
                        labels=data[:,col-1]
                        clf = tree.DecisionTreeClassifier()
                        clf = clf.fit(arr, labels)
                        t=clf.tree_
                        idx_leaf_nodes = clf.apply(arr)
                        leaf_nodes, counts = np.unique(idx_leaf_nodes, return_counts=True)
                        outputData(t)
                    tppf_ld.close()
                    tppf_mean.close()
                    
                for i in range(16):
                    target_adj = '%s/Target_%d.txt' %(current_input_directory,i+1)
                    data = np.loadtxt(target_adj,delimiter=" ")
                    np.random.shuffle(data)
                    tppf_mean = open(current_input_directory+'/Target_mean_%d.txt' %(i+1),'w')
                    tppf_ld = open(current_input_directory+'/Target_ld_%d.txt' %(i+1),'w')
                    total_size=data.size; # Number of elements
                    col=data[0].size; #No. of columns
                    row=total_size/col #No. of rows

                    for t in range(100):
                        mtry = 10
                        current_a = np.zeros(col-11)
                        rand_point = range(col-11)
                        random.shuffle(rand_point)
                        #Taking only sensor data while ignoring the temporal data.
                        m=np.ndarray((row,col-11))
                        features_considered = rand_point[0:mtry]
                        arr = data[:,features_considered]
                        labels=data[:,col-1]
                        clf = tree.DecisionTreeClassifier()
                        clf = clf.fit(arr, labels)
                        t=clf.tree_
                        idx_leaf_nodes = clf.apply(arr)
                        leaf_nodes, counts = np.unique(idx_leaf_nodes, return_counts=True)
                        outputData(t)
                    tppf_ld.close()
                    tppf_mean.close()