import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.spatial.distance import pdist, squareform
from scipy import exp, signal
from scipy.linalg import eigh

import spectral as spy

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, KernelPCA
from sklearn.cluster import KMeans
from sklearn import (manifold, datasets, metrics, decomposition, cluster, ensemble,discriminant_analysis, random_projection)
from sklearn.neighbors import kneighbors_graph, KNeighborsClassifier
 
import lda        
import lda.datasets           

if __name__ == '__main__':
    data = loadmat('Indian_pines_corrected.mat')
    data = data['indian_pines_corrected']

    gt = loadmat('Indian_pines_gt.mat')
    gt = gt['indian_pines_gt']

    sc = StandardScaler()
    data_std = sc.fit_transform(np.reshape(data,[145*145,200]))

#    # PCA
    PCA_D = 2
    scikit_pca = PCA(n_components = PCA_D)
    X_spca = scikit_pca.fit_transform(data_std)
 
    #Apply KPCA
#    kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
#    X_kpca = kpca.fit_transform(data_std)

    # Laplacian
#    embedder = manifold.SpectralEmbedding(n_components=25, random_state=0,
#                                          eigen_solver="arpack", affinity='precomputed')
#    A = kneighbors_graph(data_std, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
#    A = A.toarray()
#    A = 0.5*(A + A.T)
#    data_se = embedder.fit_transform(A)
#    np.save('laplacian_output_1',data_se)
    

    
#   #spectral clustering    
#    spectral = cluster.SpectralClustering(n_clusters=17, eigen_solver=None, random_state=None, n_init=10, gamma=1.0, affinity='rbf', n_neighbors=10, eigen_tol=0.0, assign_labels='kmeans', degree=3, coef0=1, kernel_params=None)
#    labels = spectral.fit(data_se,y=None)
#    labels = np.reshape(labels,(145,145))
   
#    #Spectral Kmeans:
#    n_clusters = 17
#    (labels, c) = spy.kmeans(np.reshape(X_spca,[145,145,PCA_D]), nclusters=n_clusters, max_iterations=100)
#    fig = plt.figure(figsize=(12,6))
#    p = plt.subplot(2, 1, 1)
#    v = spy.imshow(classes=gt, fignum=fig.number)
#    p.set_title('Ground Truth')
#    
#    p = plt.subplot(2, 1, 2)
#    v = spy.imshow(classes=labels , fignum=fig.number)
#    p.set_title('k-means classes');
#    plt.show(v)  
   
   # Sklearn Kmeans
    n_clusters = 17
    labels = KMeans(n_clusters,n_init=100).fit_predict(X_spca)
    labels=np.reshape(labels,(145,145))

    # median filter:
#    filtered = signal.medfilt2d(np.uint8(labels),5);
 
#    # LDA:
#    lda_model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
#    lda_model.fit(data_se.astype(np.int64))
#    labels = lda_model.components_  # model.components_ also works


    percentage = metrics.adjusted_rand_score(np.reshape(gt,(145*145)), np.reshape(labels,(145*145)))
    print('Percentage = ',percentage*100)
    
#    percentage = metrics.adjusted_rand_score(np.reshape(gt,(145*145)), np.reshape(filtered,(145*145)))
#    print('Filtered Percentage = ',percentage*100) 
    
    plt.imshow(labels)
    plt.show()
    plt.imshow(gt)
    plt.show()    
    
#    plt.imshow(filtered)
#    plt.show()
     
     indx = np.where(X_spca[:,0]>0)
     indxn =np.where(X_spca[:,0]<=0)
     X_spca[indx]=0
     X_spca[indxn]=1