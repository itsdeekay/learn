import numpy as np
import sklearn
import random
from sklearn import tree    
from sklearn.externals.six import StringIO
from sklearn import linear_model

if __name__ == "__main__":
    houses = [102,113,118]
    for p in range (len(houses)):
        for j in range (len(houses)):
            if(p!=j):
                current_input_directory = 'deepak/hh%d/hh%d_hh%d' %(houses[p],houses[p],houses[j])
                for i in range(16):
                    source_adj = '%s/final_tree_path_vectors_source_%d.csv' %(current_input_directory,i+1)
                    target_adj = '%s/final_tree_path_vectors_target_%d.csv' %(current_input_directory,i+1)
                    data_s = np.loadtxt(source_adj,delimiter=",")
                    data_t = np.loadtxt(target_adj,delimiter=",")
                    tppf = open(current_input_directory+'/transform_%d.txt' %(i+1),'w')
                    for k in range(len(data_t[0])):
                        clf = linear_model.Lasso(alpha = 0.1)
                        clf.fit(data_s,data_t[:,k])
                        lasso_coeff = clf.coef_
                        tvals = ' '.join([str(a1) for a1 in lasso_coeff])
                        tppf.write(tvals+'\n')
                    tppf.close()
                    print '%d Completed' %(i)
                
                current_input_directory = 'deepak/hh%d' %(houses[p])
                for i in range(16):
                    source_adj = '%s/hh%d_hh%dsource_final_%d.csv' %(current_input_directory,houses[p],houses[j],i+1)
                    target_adj = '%s/hh%d_hh%dtarget_final_%d.csv' %(current_input_directory,houses[p],houses[j],i+1)
                    data_s = np.loadtxt(source_adj,delimiter=",")
                    data_t = np.loadtxt(target_adj,delimiter=",")
                    tppf = open(current_input_directory+'/hh%d_hh%d_transform_%d.txt' %(houses[p],houses[j],i+1),'w')
                    for k in range(len(data_t[0])):
                        clf = linear_model.Lasso(alpha = 0.1)
                        clf.fit(data_s,data_t[:,k])
                        lasso_coeff = clf.coef_
                        tvals = ' '.join([str(a1) for a1 in lasso_coeff])
                        tppf.write(tvals+'\n')
                    tppf.close()
                    print '%d Source Completed' %(i)
                