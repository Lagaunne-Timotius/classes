import matplotlib.pyplot as plt
import numpy as np
import spectral as spy
from scipy import ndimage
from scipy.io import loadmat
from skimage.measure import block_reduce
from sklearn import (manifold, datasets, metrics, decomposition, cluster, ensemble,discriminant_analysis, random_projection)
from sklearn.neighbors import kneighbors_graph, KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy import exp, signal

if __name__ == '__main__':
    data = loadmat('Indian_pines_corrected.mat')
    data = data['indian_pines_corrected']

    gt = loadmat('Indian_pines_gt.mat')
    gt = gt['indian_pines_gt']
    
    data1 = data[:,:,0:40]
    data2 = data[:,:,40:200]
    
    sc = StandardScaler()
    data_std1 = sc.fit_transform(np.reshape(data1,[145*145,40]))
    data_std2 = sc.fit_transform(np.reshape(data2,[145*145,160]))
    
    #Laplacian
    embedder = manifold.SpectralEmbedding(n_components=10, random_state=0,
                                          eigen_solver="arpack", affinity='precomputed')
    A = kneighbors_graph(data_std1, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
    A = A.toarray()
    A = 0.5*(A + A.T)
    data_se1 = embedder.fit_transform(A)   
    
    A = kneighbors_graph(data_std2, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
    A = A.toarray()
    A = 0.5*(A + A.T)
    data_se2 = embedder.fit_transform(A)
    
    data_se = np.append(data_se1,data_se2,axis=1)
    data_se = np.append(data_se,data)    
    data_se = sc.fit_transform(data_se)
    # Sklearn Kmeans
    n_clusters = 17
    labels = KMeans(n_clusters,n_init=145).fit_predict(data_se)
    labels=np.reshape(labels,(145,145))
    
    filtered = signal.medfilt2d(np.uint8(labels),3);
    
    percentage = metrics.adjusted_rand_score(np.reshape(gt,(145*145)), np.reshape(labels,(145*145)))
    print('Percentage = ',percentage*100)
