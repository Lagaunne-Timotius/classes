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

from sklearn.decomposition import PCA, KernelPCA
import skfuzzy as fuzz
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import LinearSVC
from sklearn import svm
from scipy.sparse import coo_matrix
from scipy.special import comb

def contingency_matrix(labels_true, labels_pred, eps=None):
   classes, class_idx = np.unique(labels_true, return_inverse=True)
   clusters, cluster_idx = np.unique(labels_pred, return_inverse=True)
   n_classes = classes.shape[0]
   n_clusters = clusters.shape[0]
   # Using coo_matrix to accelerate simple histogram calculation,
   # i.e. bins are consecutive integers
   # Currently, coo_matrix is faster than histogram2d for simple cases
   contingency = coo_matrix((np.ones(class_idx.shape[0]),
                             (class_idx, cluster_idx)),
                            shape=(n_classes, n_clusters),
                            dtype=np.int).toarray()
   if eps is not None:
       # don't use += as contingency is integer
       contingency = contingency + eps
   return contingency

def check_clusterings(labels_true, labels_pred):
   """Check that the two clusterings matching 1D integer arrays"""
   labels_true = np.asarray(labels_true)
   labels_pred = np.asarray(labels_pred)

   # input checks
   if labels_true.ndim != 1:
       raise ValueError(
           "labels_true must be 1D: shape is %r" % (labels_true.shape,))
   if labels_pred.ndim != 1:
       raise ValueError(
           "labels_pred must be 1D: shape is %r" % (labels_pred.shape,))
   if labels_true.shape != labels_pred.shape:
       raise ValueError(
           "labels_true and labels_pred must have same size, got %d and %d"
           % (labels_true.shape[0], labels_pred.shape[0]))
   return labels_true, labels_pred

def rand_score(labels_true, labels_pred):
   
   labels_true, labels_pred = check_clusterings(labels_true, labels_pred)
   n_samples = labels_true.shape[0]
   classes = np.unique(labels_true)
   clusters = np.unique(labels_pred)
   # Special limit cases: no clustering since the data is not split;
   # or trivial clustering where each document is assigned a unique cluster.
   # These are perfect matches hence return 1.0.
   if (classes.shape[0] == clusters.shape[0] == 1
           or classes.shape[0] == clusters.shape[0] == 0
           or classes.shape[0] == clusters.shape[0] == len(labels_true)):
       return 1.0

   contingency = contingency_matrix(labels_true, labels_pred)

   # Compute the ARI using the contingency data
   sum_comb_c = sum(comb2(n_c) for n_c in contingency.sum(axis=1))
   sum_comb_k = sum(comb2(n_k) for n_k in contingency.sum(axis=0))

   sum_comb = sum(comb2(n_ij) for n_ij in contingency.flatten())
   t_p=sum_comb
   f_p=sum_comb_c-sum_comb
   f_n=sum_comb_k-sum_comb
   t_n=float(comb(n_samples, 2))-t_p-f_p-f_n
   result=(t_n+t_p)/float(comb(n_samples, 2))
   return result

def comb2(n):
   # the exact version is faster for k == 2: use it by default globally in
   # this module instead of the float approximate variant
   return comb(n, 2, exact=1)


if __name__ == '__main__':
    data = loadmat('Indian_pines_corrected.mat')
    data = data['indian_pines_corrected']

    gt = loadmat('Indian_pines_gt.mat')
    gt = gt['indian_pines_gt']
    
    sc = StandardScaler()
    data_std = sc.fit_transform(np.reshape(data,[145*145,200]))
    
    #Laplacian
#    embedder = manifold.SpectralEmbedding(n_components=10, random_state=0,
#                                          eigen_solver="arpack", affinity='precomputed')
#    A = kneighbors_graph(data_std, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
#    A = A.toarray()
#    A = 0.5*(A + A.T)
#    data_se = embedder.fit_transform(A)   
    
    # Stage 1, Kmeans 
#    n_clusters = 17
#    Klabels = KMeans(n_clusters,n_init=145).fit_predict(np.reshape(data,[145*145,200]))
#    Klabels=np.reshape(Klabels,(145,145))
    
    # Stage 1, Cmeans 
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
        np.reshape(data,[145*145,200]).T, 17, 3, error=0.005, maxiter=1000, init=None)
        
    
    Clabels = np.argmax(u,axis=0)
    Clabels = np.reshape(Clabels,[145,145])
    

#    Laplacian
    n_components =20
    embedder = manifold.SpectralEmbedding(n_components, random_state=0,
                                          eigen_solver="arpack", affinity='precomputed')
    A = kneighbors_graph(data_std, 9, mode='connectivity', metric='minkowski', p=2, metric_params=None, include_self=True)
    A = A.toarray()
    A = 0.5*(A + A.T)
    data_se = embedder.fit_transform(A)    
    data_se = np.reshape(data_se,[145,145,n_components])
    
    
    
#   PCA:
#    n_components = 50
#    scikit_pca = PCA(n_components)
#    data_se = scikit_pca.fit_transform(data_std) 
#    data_se = np.reshape(data_se,[145,145,n_components])
    
# No Dimensionality Reduction:
#    data_se = np.reshape(data_std,[145,145,200])
#    n_components = 200
    
    labels = Clabels
#    labels = Klabels
    
    #Eliminating outliers:
    # Parzen Window
#    window = 3
#    halfW = np.floor(window/2).astype(int)
#    inliers=np.empty([1,n_components])
#    inlier_labels=np.empty([1,1])
#    
#    for i in range(halfW,145-halfW):
#        for j in range(halfW,145-halfW):
#            ROI = labels[i-halfW:i+halfW,j-halfW:j+halfW]
#            if np.unique(ROI).shape[0]==1:
#                inliers=np.append(inliers,data_se[i,j,:].reshape([1,n_components]),axis=0)
#                inlier_labels=np.append(inlier_labels,labels[i,j].reshape([1,1]),axis=0)
#    inliers=np.delete(inliers,0,axis=0)
#    inlier_labels=np.delete(inlier_labels,0,axis=0)
#    inlier_labels = np.reshape(inlier_labels,[inlier_labels.shape[0]])
    
    # Cmean Weighting:
    weights = np.amax(u,axis=0)
    threshold = 0.1
    inliers_indx = np.where(weights>threshold)
    cmean_labels = np.reshape(labels,[145*145])
    data_se_ = np.reshape(data_se,[145*145,n_components])
    inlier_labels = cmean_labels[inliers_indx]
    inliers = data_se_[np.reshape(inliers_indx,[np.shape(inliers_indx)[1]]),:] 
    
    
    #Stage 2: Multi-Class SVM
    SVM_labels = OneVsOneClassifier(LinearSVC(random_state=0)).fit(inliers, inlier_labels).predict(np.reshape(data_se,[145*145,n_components]))
    SVM_labels = np.reshape(SVM_labels,[145,145])
    
    
    forgroundPix = np.where(gt>0)
    forgroundRows = forgroundPix[0]
    forgroundCols = forgroundPix[1]
    fgSVM = np.zeros([145,145])
    fgSVM[forgroundRows,forgroundCols] = SVM_labels[forgroundRows,forgroundCols]
    fgXmean = np.zeros([145,145])
    fgXmean[forgroundRows,forgroundCols] = labels[forgroundRows,forgroundCols]
    print('rand score using SVM', 100*rand_score(np.reshape(gt[forgroundRows,forgroundCols],[forgroundRows.shape[0]]), np.reshape(SVM_labels[forgroundRows,forgroundCols],[forgroundRows.shape[0]])))
    print('rand score using Xmean', 100*rand_score(np.reshape(gt[forgroundRows,forgroundCols],[forgroundRows.shape[0]]), np.reshape(labels[forgroundRows,forgroundCols],[forgroundRows.shape[0]])))
    print('number of classes SVM: ',np.unique(inlier_labels).shape[0])
    print('number of classes Xmean: ',np.unique(labels).shape[0])
    
    np.save("Case8",SVM_labels)
    plt.imsave("Case8_SVM.jpg",SVM_labels)
    plt.imsave("Case8_Cmean.jpg",labels)
    
    plt.imsave("Case8_SVM_BS.jpg",fgSVM)
    plt.imsave("Case8_Cmean_BS.jpg",fgXmean)
    plt.imsave("GT",gt)
    