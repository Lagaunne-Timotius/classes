import numpy as np
import numpy.matlib as matlib
import matplotlib.pyplot as plt
import sklearn as sk
from scipy.io import loadmat
from scipy.spatial.distance import pdist, squareform
from scipy import exp, signal
from scipy.linalg import eigh
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OutputCodeClassifier
from sklearn.svm import LinearSVC

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, KernelPCA
from sklearn.cluster import KMeans
from sklearn import (manifold, datasets, metrics, decomposition, cluster, ensemble,discriminant_analysis, random_projection)
from sklearn.neighbors import kneighbors_graph, KNeighborsClassifier
import skfuzzy as fuzz
from sklearn import mixture
import scipy.misc as scimisc
from sklearn.cluster import MeanShift, estimate_bandwidth

from scipy.sparse import coo_matrix
from scipy.special import comb
from scipy.spatial import distance
import sklearn.decomposition as dec
# from TwoStageClassification import n_components


np.random.seed(100)

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

def randindex(ground_truth,clust_result):
    a=0
    b=0
    n=len(ground_truth)
    for i in range(0,n-1):
        for j in range(i+1,n):
            a= a+int(((ground_truth[i]==ground_truth[j]))and(clust_result[i]==clust_result[j]))
            b= b+int(((ground_truth[i]!=ground_truth[j]))and(clust_result[i]!=clust_result[j]))
   
    rand_index=(200*(a+b))/(n*(n-1))
    return rand_index

def removeBackground(image_flat, groundTruth_flat):

    indices = np.where(groundTruth_flat==0)
    
    image_flat = np.delete(image_flat,indices)
    groundTruth_flat = np.delete(groundTruth_flat,indices)

    return image_flat,groundTruth_flat

def smartPCA(flatImage, bandwidth, n_components=1):

    dim = flatImage.shape[1]

    numBands = int(dim/bandwidth)
    extras = np.mod(dim,bandwidth)

    whitenedData = np.zeros((flatImage.shape[0],numBands))

    startCounter = 0
    endCounter = bandwidth
    pca = dec.PCA(n_components=n_components,whiten=True)
    for i in range(0,numBands):

        if extras:
            endCounter=endCounter+1
            extras = extras - 1

        sectionToWhiten = flatImage[:,startCounter:endCounter]
        whiten = pca.fit_transform(sectionToWhiten)
        startCounter = startCounter + bandwidth
        endCounter = endCounter + bandwidth
        whitenedData[:,i] = whiten.T


    return whitenedData

if __name__ == '__main__':
    data    = loadmat('Indian_pines_corrected.mat')
    data    = data['indian_pines_corrected']

    gt  = loadmat('Indian_pines_gt.mat')
    gt  = gt['indian_pines_gt']

    sc  = StandardScaler()
    data_bg = sc.fit_transform(np.reshape(data, [145*145, 200]))
    
    #Add distance metric to data
    data_reshaped   = np.reshape(data, (145*145,200))
    origin = np.zeros((1,200))
    Y = np.empty(145*145)
    for i in range(145*145):
        Y[i]    = np.sqrt(np.sum(origin - data_reshaped[i,:])**2)
    
    new_data = np.load('laplacian_10D.npy')
    new_data = np.array(new_data)

    nDim = 4
    
    data_bg1 = data[0:70,0:70,:]
    data_bg2 = data[0:70,70:145,:]
    data_bg3 = data[70:145,0:70,:]
    data_bg4 = data[70:145,70:145,:]
     
    pca_data1 = smartPCA(sc.fit_transform(np.reshape(data_bg1, (70*70,200))), 200/nDim)
    pca_data1 = np.reshape(pca_data1, (70, 70, nDim))
    pca_data2 = smartPCA(sc.fit_transform(np.reshape(data_bg2, (70*75,200))), 200/nDim)
    pca_data2 = np.reshape(pca_data2, (70, 75, nDim))
    pca_data1 = np.append(pca_data1, pca_data2, axis=1)    
     
    pca_data3 = smartPCA(sc.fit_transform(np.reshape(data_bg3, (75*70,200))), 200/nDim)
    pca_data3 = np.reshape(pca_data3, (75, 70,nDim))
    pca_data4 = smartPCA(sc.fit_transform(np.reshape(data_bg4, (75*75,200))), 200/nDim)
    pca_data4 = np.reshape(pca_data4, (75, 75,nDim))
    pca_data3 = np.append(pca_data3, pca_data4, axis=1)
     
    pca_data = np.append(pca_data1, pca_data3, axis=0)


    
    print(pca_data.shape)
  
    #cmeans clustering
    pca_data = np.append(pca_data, np.reshape(smartPCA(data_bg, 200/2), (145,145,2)), axis=2)
    pca_data = np.reshape(pca_data, (145*145, nDim+2))
#     for i in range(nDim+2):
#         plt.imshow(np.reshape(pca_data[:,i], [145,145]))
#         plt.show()
        
    pca_data = sc.fit_transform(pca_data)

    fpc = []
    cntr, u, u0, d, jm, p, fpc = fuzz._cluster.cmeans(pca_data.T, 17, 2, error=0.005, maxiter=1000, init=None)
    labels  = np.reshape(np.argmax(u, axis=0), [145, 145])
    
#     #Rand Score
    newLabels, newGt    = removeBackground(np.reshape(labels, [145*145]), np.reshape(gt, [145*145]))
      
    percentage = rand_score(newGt, newLabels)
    print(percentage)
    
    plt.imshow(labels)
    plt.show()
    
    
#Eliminating outliers:
    sc = StandardScaler()
    data_std = sc.fit_transform(np.reshape(data,[145*145,200]))
    weights = np.amax(u,axis=0)
    threshold = 0.5
    inliers_indx = np.where(weights>threshold)
    inlier_labels = np.reshape(labels,[145*145])[inliers_indx]
    inliers = data_std[np.reshape(inliers_indx,[np.shape(inliers_indx)[1]]),:]        
    
    SVM_labels = OneVsRestClassifier(LinearSVC(random_state=15)).fit(inliers, inlier_labels).predict(np.reshape(data_std,[145*145,200]))
#    clf = OutputCodeClassifier(LinearSVC(random_state=0),code_size=2, random_state=0)
#    SVM_labels =clf.fit(inliers, inlier_labels).predict(np.reshape(data_std,[145*145,200]))
#    
    C_range = np.logspace(-2, 10, 13)
    gamma_range = np.logspace(-9, 3, 13)
    param_grid = dict(gamma=gamma_range, C=C_range)
    cv = StratifiedShuffleSplit(inlier_labels, n_iter=5, test_size=0.2, random_state=42)
    grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
    grid.fit(inliers, inlier_labels)

    C_2d_range = [1e-2, 1, 1e2]
    gamma_2d_range = [1e-1, 1, 1e1]
    classifiers = []
    for C in C_2d_range:
        for gamma in gamma_2d_range:
            clf = SVC(C=C, gamma=gamma)
            clf.fit(X_2d, y_2d)
            classifiers.append((C, gamma, clf))    
    
    
    forgroundPix = np.where(gt>0)
    forgroundRows = forgroundPix[0]
    forgroundCols = forgroundPix[1]
    fgSVM = np.zeros([145,145])
    SVM_labels = np.reshape(SVM_labels,[145,145])
    fgSVM[forgroundRows,forgroundCols] = SVM_labels[forgroundRows,forgroundCols]
    fgXmean = np.zeros([145,145])
    
    fgXmean[forgroundRows,forgroundCols] = labels[forgroundRows,forgroundCols]

    print('rand score using SVM', 100*rand_score(np.reshape(gt[forgroundRows,forgroundCols],[forgroundRows.shape[0]]), np.reshape(SVM_labels[forgroundRows,forgroundCols],[forgroundRows.shape[0]])))
    print('rand score using Xmean', 100*rand_score(np.reshape(gt[forgroundRows,forgroundCols],[forgroundRows.shape[0]]), np.reshape(labels[forgroundRows,forgroundCols],[forgroundRows.shape[0]])))
    print('number of classes SVM: ',np.unique(inlier_labels).shape[0])
    print('number of classes Xmean: ',np.unique(labels).shape[0])
    plt.imshow(fgSVM)
    plt.imshow(fgXmean)