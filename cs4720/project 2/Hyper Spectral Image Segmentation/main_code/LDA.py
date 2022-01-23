
# coding: utf-8

# In[41]:

import numpy as np
import numpy.matlib as matlib
import matplotlib.pyplot as plt
import sklearn as sk
from scipy.io import loadmat
from scipy.spatial.distance import pdist, squareform
from scipy import exp, signal
from scipy.linalg import eigh

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, KernelPCA
from sklearn.cluster import KMeans
from sklearn import (manifold, datasets, metrics, decomposition, cluster, ensemble,discriminant_analysis, random_projection)
from sklearn.neighbors import kneighbors_graph, KNeighborsClassifier
#import skfuzzy as fuzz
from sklearn import mixture
import scipy.misc as scimisc
from sklearn.cluster import MeanShift, estimate_bandwidth
import numpy as np
import lda
import lda.datasets
from scipy.io import loadmat
import matplotlib.pylab as plt
from sklearn import cluster, datasets
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles
from scipy.sparse import coo_matrix
from scipy.special import comb
from scipy.spatial import distance
import sklearn.decomposition as dec


np.random.seed(100)

####  Rand Index 
### We create the rand index function from the modification of ARI from scikit_learn

###Creating contigency matrix
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

###Clustering checking
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

###Rand_Score
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

##pairwise Combination
def comb2(n):
    # the exact version is faster for k == 2: use it by default globally in
    # this module instead of the float approximate variant
    return comb(n, 2, exact=1)

###Background removing for rand_indexscore
def removeBackground(image_flat, groundTruth_flat):

    indices = np.where(groundTruth_flat==0)
    
    image_flat = np.delete(image_flat,indices)
    groundTruth_flat = np.delete(groundTruth_flat,indices)

    return image_flat,groundTruth_flat

#image after eliminating the background (setting the background to label 17)
def removeBackgroundshow(image_flat, groundTruth_flat):
    indices = np.where(groundTruth_flat==0)
    new_image_flat=image_flat
    new_image_flat[indices]=17
    return image_flat

###PCA
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
    
##Loading Data
    gt = loadmat('/home/lagaunne/Desktop/Indian_pines_gt.mat')
    gt=gt['indian_pines_gt']
    data = loadmat('/home/lagaunne/Desktop/Indian_pines_corrected.mat')
    data=data['indian_pines_corrected']
###Normalized Data
    sc  = StandardScaler()
    data_bg = sc.fit_transform(np.reshape(data, [145*145, 200]))
    
##Feature Extraction
    ##Local_Split PCA
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
    
    pca_data = np.append(pca_data, np.reshape(smartPCA(data_bg, 200/4), (145,145,4)), axis=2)
    pca_data = np.reshape(pca_data, (145*145, nDim+4))    
    pca_data = sc.fit_transform(pca_data)
    
    X=pca_data
    
##LDA
    ###Word Construction
    K_means = cluster.KMeans(n_clusters=100)

    words = K_means.fit(X)
    words = K_means.labels_.astype(np.int)
    ##Document Construction
    K_means2 = cluster.KMeans(n_clusters=17)
    K_means2.fit(X)
    document = K_means2.labels_.astype(np.int)
    document=np.array(document)
    ###Word Distribution Construction
    feature=contingency_matrix(document,words)

    model = lda.LDA(n_topics=17, n_iter=2000, random_state=1)
    model.fit(feature)
    topic_word = model.topic_word_  # model.components_ also works
    sp=topic_word.shape
    
    ###Assignment 
    topic_label=[]
    for i in range(0,sp[1]):
        index=0
        value=0
        for j in  range(0,sp[0]):
            if topic_word[j,i]>value:
                value=topic_word[j,i]
                index=j
        topic_label.append(index)
    ## Assignment of Topic to each pixel 
    image_label=[]
    for i in range(0,len(words)):
        for j in  range(0,len(topic_label)):
            if words[i]==j:
                image_label.append(topic_label[j])
                
    ##Words show
    words_new=np.reshape(words,(145,145))
    fig = plt.figure()
    plt.imshow(words_new)
    ###Document show
    document_new=np.reshape(document,(145,145))
    fig = plt.figure()
    plt.imshow(document_new)
    ###LDA show
    image_label=np.array(image_label)
    LDA_result=np.reshape(image_label,(145,145))
    fig = plt.figure()
    plt.imshow(LDA_result)
    plt.show()
         
    #Rand Score
    newLabels, newGt    = removeBackground(np.reshape(LDA_result, [145*145]), np.reshape(gt, [145*145]))
    percentage = rand_score(newGt, newLabels)
    print(percentage)

    #Eliminate background and show result
    new_image=removeBackgroundshow(np.reshape(image_label, [145*145]),np.reshape(gt, [145*145]))
    image=np.reshape(new_image,(145,145))
    plt.imshow(image)
    plt.show()

