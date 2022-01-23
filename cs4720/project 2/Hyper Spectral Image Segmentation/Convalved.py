import matplotlib.pyplot as plt
import numpy as np
import spectral as spy
from scipy import ndimage, signal
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
    
    
    mask = -1/8*np.ones([3,3])
    mask[1,1]=1
    convalved=np.empty([145,145,200])
    for i in range(200):
        convalved[:,:,i]=np.abs(signal.convolve2d(data[:,:,i],mask,mode='same',boundary='symm'))
    normal = np.sum(convalved,axis=2)
    sc = StandardScaler()
    normalized = sc.fit_transform(np.reshape(normal,[145*145]))
    
    #Laplacian
    data_std = sc.fit_transform(np.reshape(data,[145*145,200]))
    embedder = manifold.SpectralEmbedding(n_components=10, random_state=0,
                                          eigen_solver="arpack", affinity='precomputed')
    A = kneighbors_graph(data_std, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
    A = A.toarray()
    A = 0.5*(A + A.T)
    data_se = embedder.fit_transform(A) 
    
    agmented_data=np.append(data_se,np.reshape(normalized,(145*145,1)),axis=1)
    
    n_clusters = 17
    labels = KMeans(n_clusters,n_init=145).fit_predict(agmented_data)
    labels=np.reshape(labels,(145,145))