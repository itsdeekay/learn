import numpy as np
import sklearn
import random
import math
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

langs = ["de","fr","jp","en"] 
product = ["books","dvd","music"]

for p in range (len(langs)):
    for j in range (len(product)):
        current_input_directory = '%s/%s' %(langs[p],product[j])
        for i in range(16):
            file1 = current_input_directory +'/Target/Target_%d.txt' %(i+1)
            file2 = current_input_directory +'/Target/Target_PCA_%d.txt' %(i+1)
            file_t = current_input_directory +'/Target/Target_reduced_%d.txt' %(i+1)
            data1 = np.loadtxt(file1,delimiter=" ")
            data2 = np.loadtxt(file2,delimiter=" ")
            col=data1[0].size; #No. of columns
            X = data1[:,:col-1]
            Y = data1[:,col-1]
            X_std = StandardScaler().fit_transform(X)
            data_t = np.dot(X_std,data2)
            data_t = np.column_stack((data_t,Y))
            np.savetxt(file_t, data_t, delimiter=' ',fmt='%5.5f')
        
        
