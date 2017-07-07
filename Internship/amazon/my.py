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
        file = current_input_directory +'/train.processed_data.txt'
        file_t1 = current_input_directory +'/Source_PCA.txt'
        file_t2 = current_input_directory +'/Source_reduced.txt'
        data = np.loadtxt(file,delimiter=" ")
        col = data[0].size
	X = data[:,:col-1]
        Y = data[:,col-1]
        X_std = StandardScaler().fit_transform(X)
        pca = PCA(n_components=col-1)
        pca.fit(X_std)
        l = pca.explained_variance_ratio_
        d = 0
        for i in range(len(l)):
            d += l[i]
            if d>0.75:
                d = i+1
                break
        pca = PCA(n_components=d)
        pca.fit(X_std)
        data_t = pca.components_
        np.savetxt(file_t1, data_t.T, delimiter=' ',fmt='%5.5f')
        data_t = np.dot(X_std,data_t.T)
        data_t = np.column_stack((data_t,Y))
        np.savetxt(file_t2, data_t, delimiter=' ',fmt='%5.5f')
        '''
        for i in range(16):
            file = current_input_directory +'/Target/Target_%d.txt' %(i+1)
            file_t = current_input_directory +'/Target/Target_PCA_%d.txt' %(i+1)
            data = np.loadtxt(file,delimiter=" ")
            total_size=data.size; # Number of elements
            col=data[0].size; #No. of columns
            row=total_size/col
            X = data[:,:col-1]
            Y = data[:,col-1]
            X_std = StandardScaler().fit_transform(X)
            pca = PCA(n_components=col-1)
            pca.fit(X_std)
            l = pca.explained_variance_ratio_
            d = 0
            for i in range(len(l)):
                d += l[i]
                if d>0.75:
                    d = i+1
                    break
            pca = PCA(n_components=d)
            pca.fit(X_std)
            data_t = pca.components_
            np.savetxt(file_t, data_t.T, delimiter=' ',fmt='%5.5f')
            '''
        
