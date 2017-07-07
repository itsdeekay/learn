import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


#file_t = current_input_directory +'/train_PCA.txt'
X = np.array([[-1, -1, 2], [-2, -1, 3], [-3, -2, 1], [1, 1, 1], [2, 1, 2], [3, 2, 3]])
X_std = StandardScaler().fit_transform(X)
cov_mat = np.cov(X_std.T)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()
matrix_w = np.hstack((eig_pairs[0][1].reshape(3,1), 
                      eig_pairs[1][1].reshape(3,1)))

Y = X_std.dot(matrix_w)
print Y
pca = PCA(n_components=2)
data = pca.fit_transform(X_std)
data2 = pca.components_
data3 = pca.explained_variance_
l = pca.explained_variance_ratio_
print data
#print data2.T
print np.dot(X_std,data2.T)


#data = np.column_stack((data,data2))

#np.savetxt('train_PCA.txt', data, delimiter=' ',fmt='%5.5f')
