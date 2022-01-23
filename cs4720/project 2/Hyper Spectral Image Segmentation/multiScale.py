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

if __name__ == '__main__':
    data = loadmat('Indian_pines_corrected.mat')
    data = data['indian_pines_corrected']

    gt = loadmat('Indian_pines_gt.mat')
    gt = gt['indian_pines_gt']
    
#    image = np.arange(3*3*4).reshape(3, 4, 3)
#    subsampled = block_reduce(image, block_size=(2, 2, 1), func=np.mean)
    
    downsample1 = block_reduce(data, block_size=(2,2,1),func=np.mean)
    resample1 = ndimage.zoom(downsample1, (2,2,1), order=0)
    gt1 = np.uint8(block_reduce(gt, block_size=(2,2),func=np.mean))
    gtresample1 = ndimage.zoom(gt1,2,order=2)
    
    downsample2 = block_reduce(data, block_size=(3,3,1),func=np.mean)
    gt2 = np.uint8(block_reduce(gt, block_size=(3,3),func=np.mean))
    
    sc = StandardScaler()
    data_std = sc.fit_transform(np.reshape(data,[145*145,200]))
    data_std1 = sc.fit_transform(np.reshape(downsample1,[73*73,200]))  
    data_std2 = sc.fit_transform(np.reshape(downsample2,[49*49,200]))   
    
    
    #just for test resampling
    data_std1 = sc.fit_transform(np.reshape(resample1,[146*146,200]))  

    # Laplacian
    embedder = manifold.SpectralEmbedding(n_components=25, random_state=0,
                                          eigen_solver="arpack", affinity='precomputed')
    A = kneighbors_graph(data_std, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
    A = A.toarray()
    A = 0.5*(A + A.T)
    data_se = embedder.fit_transform(A)
    
    embedder1 = manifold.SpectralEmbedding(n_components=25, random_state=0,
                                          eigen_solver="arpack", affinity='precomputed')
    A1 = kneighbors_graph(data_std1, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
    A1 = A1.toarray()
    A1 = 0.5*(A1 + A1.T)
    data_se1 = embedder1.fit_transform(A1)
    
    
    embedder2 = manifold.SpectralEmbedding(n_components=25, random_state=0,
                                          eigen_solver="arpack", affinity='precomputed')
    A2 = kneighbors_graph(data_std2, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
    A2 = A2.toarray()
    A2 = 0.5*(A2 + A2.T)
    data_se2 = embedder2.fit_transform(A2)    
    
    
    # Sklearn Kmeans
    n_clusters = 17
    labels = KMeans(n_clusters,n_init=100).fit_predict(data_se)
    labels=np.reshape(labels,(145,145))
    
    #test resampling
    labels = KMeans(n_clusters,n_init=100).fit_predict(data_se1)
    labels=np.reshape(labels,(146,146))
    
    labels1 = KMeans(n_clusters,n_init=100).fit_predict(data_se1)
    labels1=np.reshape(labels1,(73,73))
    
    labels2 = KMeans(n_clusters,n_init=100).fit_predict(data_se2)
    labels2=np.reshape(labels2,(49,49))    
    
    percentage = metrics.adjusted_rand_score(np.reshape(gt,(145*145)), np.reshape(labels,(145*145)))
    print('Percentage = ',percentage*100)
    
    percentage1 = metrics.adjusted_rand_score(np.reshape(gt1,(73*73)), np.reshape(labels1,(73*73)))
    print('Percentage1 = ',percentage1*100)

    percentage2 = metrics.adjusted_rand_score(np.reshape(gt2,(49*49)), np.reshape(labels2,(49*49)))
    print('Percentage2 = ',percentage2*100)


    plt.imshow(labels)
    plt.savefig("labels")
    plt.imshow(labels1)
    plt.savefig("labels1")
    plt.imshow(labels2)
    plt.savefig("labels2")