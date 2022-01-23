import numpy as np
from scipy.io import loadmat
from scipy import signal
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import skfuzzy as fuzz
from sklearn import mixture
from scipy.sparse import coo_matrix
from scipy.special import comb
import sklearn.decomposition as dec

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
    '''Removes background for Rand Index calculation'''
    indices = np.where(groundTruth_flat==0)
    
    image_flat = np.delete(image_flat,indices)
    groundTruth_flat = np.delete(groundTruth_flat,indices)

    return image_flat,groundTruth_flat

def removeBackground1(image_flat, groundTruth_flat):
    '''Assigns background a different label for image show'''
    indices = np.where(groundTruth_flat==0)   
    image_flat[indices] = 17
    return image_flat

def smartPCA(flatImage, bandwidth, n_components=1):
    '''Split Band PCA selects 1 high variance band from the specified bands'''
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
    #Load Input data
    data    = loadmat('Indian_pines_corrected.mat')
    data    = data['indian_pines_corrected']

    #Load Ground truth
    gt  = loadmat('Indian_pines_gt.mat')
    gt  = gt['indian_pines_gt']

    #StandardScaler for normalization
    sc  = StandardScaler()
    data_bg = sc.fit_transform(np.reshape(data, [145*145, 200]))    #Normalize inputs  

    #Localized PCA method,
    #Divide the image into 4 quadrants and then do a dimensionality reduction and combine the data and then do a clustering.
    #Number of dimensions per quadrant
    nDim = 4
    #4 Quadrants 
    data_bg1 = data[0:70,0:70,:]
    data_bg2 = data[0:70,70:145,:]
    data_bg3 = data[70:145,0:70,:]
    data_bg4 = data[70:145,70:145,:]
    
    #Apply PCA on all 4 quadrants
    #Q1 & Q2 PCA 
    pca_data1 = smartPCA(sc.fit_transform(np.reshape(data_bg1, (70*70,200))), 200/nDim)
    pca_data1 = np.reshape(pca_data1, (70, 70, nDim))
    pca_data2 = smartPCA(sc.fit_transform(np.reshape(data_bg2, (70*75,200))), 200/nDim)
    pca_data2 = np.reshape(pca_data2, (70, 75, nDim))
    pca_data1 = np.append(pca_data1, pca_data2, axis=1)    
     
    #Q3 & Q4 PCA
    pca_data3 = smartPCA(sc.fit_transform(np.reshape(data_bg3, (75*70,200))), 200/nDim)
    pca_data3 = np.reshape(pca_data3, (75, 70,nDim))
    pca_data4 = smartPCA(sc.fit_transform(np.reshape(data_bg4, (75*75,200))), 200/nDim)
    pca_data4 = np.reshape(pca_data4, (75, 75,nDim))
    pca_data3 = np.append(pca_data3, pca_data4, axis=1)
     
    #Merge all the data from 4 quadrants
    pca_data = np.append(pca_data1, pca_data3, axis=0)
    
    #cmeans clustering
    #Append the Split Band PCA bands to localized PCA dimensions
    pca_data = np.append(pca_data, np.reshape(smartPCA(data_bg, 200/4), (145,145,4)), axis=2)
    
    #Global PCA
#     pca = dec.PCA(n_components=8,whiten=True)
#     pca_data = pca.fit_transform(data_bg)    
#     pca_data = np.load('GPCA.npy')

    #Final vector for clustering
    pca_data = np.reshape(pca_data, (145*145, nDim+4))
    pca_data = sc.fit_transform(pca_data)
    print('Feature vecture size: '+str(pca_data.shape))

    #Kmeans 17 class clustering
    n_clusters  = 17
    labels2  = KMeans(n_clusters, n_jobs=-1).fit_predict(pca_data)
    #5x5 median filtering for max voting
    labels2 = signal.medfilt2d(np.uint8(np.reshape(labels2, (145, 145))), 5)
    #Save the labels for voting
#     np.save('kmeans_labels_Global', labels2)
    newLabels, newGt    = removeBackground(np.reshape(labels2, [145*145]), np.reshape(gt, [145*145]))
    newLabelsShow    = np.reshape(removeBackground1(np.reshape(labels2, [145*145]), np.reshape(gt, [145*145])), (145,145))
    percentage = rand_score(newGt, newLabels)
    print("KMeans: "+str(percentage*100))   
#     plt.imshow(newLabelsShow)
#     plt.show()

    #GMM 17 class clustering
    g = mixture.GMM(n_components=17)
    labels1  = g.fit_predict(pca_data, y=np.reshape(labels2, (145*145)))
    #5x5 median filtering for max voting
    labels1 = signal.medfilt2d(np.uint8(np.reshape(labels1, (145, 145))), 5)
    #Save the labels for voting
#     np.save('gmm_labels_Global', labels1)
    newLabels, newGt    = removeBackground(np.reshape(labels1, [145*145]), np.reshape(gt, [145*145]))
    newLabelsShow    = np.reshape(removeBackground1(np.reshape(labels1, [145*145]), np.reshape(gt, [145*145])), (145,145))
    percentage = rand_score(newGt, newLabels)
    print('GMM: '+str(percentage*100))   
#     plt.imshow(newLabelsShow)
#     plt.show()

    #Fuzzy C-means 17 class classification
    fpc = []
    cntr, u, u0, d, jm, p, fpc = fuzz._cluster.cmeans(pca_data.T, 17, 2, error=0.005, maxiter=1000, init=None)
    labels  = np.reshape(np.argmax(u, axis=0), [145, 145])
    labels = signal.medfilt2d(np.uint8(labels), 3)
    #Save the labels for voting
#     np.save('cmeans_labels_Global', labels)  
    #Rand Score
    newLabels, newGt    = removeBackground(np.reshape(labels, [145*145]), np.reshape(gt, [145*145]))
    newLabelsShow    = np.reshape(removeBackground1(np.reshape(labels, [145*145]), np.reshape(gt, [145*145])), (145,145))
    percentage = rand_score(newGt, newLabels)
    print("CMeans: "+str(percentage*100))
#     plt.imshow(newLabelsShow)
#     plt.show()