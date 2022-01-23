
from munkres import Munkres, print_matrix, make_cost_matrix
import sys
from statistics import mode
from statistics import mode, StatisticsError
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

    # Compute the RI using the contingency data
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

#image after eliminating the background (setting the background to label 17)
def removeBackgroundshow(image_flat, groundTruth_flat):
    indices = np.where(groundTruth_flat==0)
    new_image_flat=image_flat
    new_image_flat[indices]=17
    return image_flat

#Relabeling using the label map
def changelabel(newlabel,data):
    newdata=[]
    for i in range(0,len(data)):
        for j in range(0,len(newlabel)):
            if data[i]==newlabel[j]:
                newdata.append(j)
    newdata=np.array(newdata)
    return newdata

#Voting with six classification result with data1 as the baseline when majority vote is not exist
def voting(data1,data2,data3,data4,data5,data6):
    voting_result=[]
    for i in range(0,len(data1)):
        try :
            voting_result.append(mode([data1[i],data2[i],data3[i],data4[i],data5[i],data6[i]]))
        except StatisticsError:
            voting_result.append(data1[i])
    voting_result=np.array([voting_result])
    return voting_result

#######
#Data Loading
#######

gmm=np.load('/home/lagaunne/project-2-team/gmm_result/gmm_labels_Local_Split.npy')
kmeans=np.load('/home/lagaunne/project-2-team/kmeans_result/kmeans_labels_Local_Split.npy')
cmeans=np.load('/home/lagaunne/project-2-team/cmeans_result/cmeans_labels_Local_Split.npy')
isodata=np.load('/home/lagaunne/project-2-team/isodata_result/isodata_labels_Local_Split.npy')
svm=np.load('/home/lagaunne/project-2-team/svm_result/svm_labels_Local_Split.npy')
lda=np.load('/home/lagaunne/project-2-team/lda_result/lda_labels_Local_Split.npy')

gmm=np.reshape(gmm,[145*145])
kmeans=np.reshape(kmeans,[145*145])
cmeans=np.reshape(cmeans,[145*145])
isodata=np.reshape(isodata,[145*145])
svm=np.reshape(svm,[145*145])
lda=np.reshape(lda,[145*145])

##Adding dummy label from 0-16
gmm_vote=np.append(gmm,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
lda_vote=np.append(lda,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
cmeans_vote=np.append(cmeans,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
kmeans_vote=np.append(kmeans,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
isodata_vote=np.append(isodata,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
svm_vote=np.append(svm,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

###Construct Label Map with K-Means as the baseline

#Construct Label Map between K-Means and LDA
matrix=contingency_matrix(kmeans_vote,lda_vote)
matrix = matrix.tolist()
cost_matrix = make_cost_matrix(matrix, lambda cost: sys.maxsize - cost)
m = Munkres()
indexes = m.compute(cost_matrix)
total = 0
newlabelA=[]
for row, column in indexes:
    value = matrix[row][column]
    total += value
    newlabelA.append(column)
    
#Construct Label Map between K-Means and Gausian Mixture Model
matrix=contingency_matrix(kmeans_vote,gmm_vote)
matrix = matrix.tolist()
cost_matrix = make_cost_matrix(matrix, lambda cost: sys.maxsize - cost)
m = Munkres()
indexes = m.compute(cost_matrix)
total = 0
newlabelB=[]
for row, column in indexes:
    value = matrix[row][column]
    total += value
    newlabelB.append(column)

#Construct Label Map between K-Means and isodata
matrix=contingency_matrix(kmeans_vote,isodata_vote)
matrix = matrix.tolist()
cost_matrix = make_cost_matrix(matrix, lambda cost: sys.maxsize - cost)
m = Munkres()
indexes = m.compute(cost_matrix)

total = 0
newlabelC=[]
for row, column in indexes:
    value = matrix[row][column]
    total += value
    newlabelC.append(column)

#Construct Label Map between K-Means and C-means
matrix=contingency_matrix(kmeans_vote,cmeans_vote)
matrix = matrix.tolist()
cost_matrix = make_cost_matrix(matrix, lambda cost: sys.maxsize - cost)
m = Munkres()
indexes = m.compute(cost_matrix)

total = 0
newlabelD=[]
for row, column in indexes:
    value = matrix[row][column]
    total += value
    newlabelD.append(column)

#Construct Label Map between K-Means and SVM
matrix=contingency_matrix(kmeans_vote,svm_vote)
matrix = matrix.tolist()
cost_matrix = make_cost_matrix(matrix, lambda cost: sys.maxsize - cost)
m = Munkres()
indexes = m.compute(cost_matrix)

total = 0
newlabelE=[]
for row, column in indexes:
    value = matrix[row][column]
    total += value
    newlabelE.append(column)

    
###Relabeling with label map

new_data1= changelabel(newlabelA,lda)
new_data2= changelabel(newlabelB,gmm)
new_data3= changelabel(newlabelC,isodata)
new_data4= changelabel(newlabelC,cmeans)
new_data5= changelabel(newlabelC,svm)

result=voting(kmeans,new_data1,new_data2,new_data3,new_data4,new_data5)
result=np.reshape(result,(21025))
np.save('/home/lagaunne/project-2-team/Voting Result/6_voting_result.npy',result)
newLabels, newGt = removeBackground(np.reshape(result, [145*145]), np.reshape(gt, [145*145]))
percentage = rand_score(newGt, newLabels)
print(percentage)

plt.imshow(np.reshape(result,[145,145]))

new_image=removeBackgroundshow(np.reshape(result, [145*145]),np.reshape(gt, [145*145]))
image=np.reshape(new_image,(145,145))
plt.imsave('/home/lagaunne/project-2-team/Voting Result/6_voting_result.jpg',image)

plt.imshow(image)
plt.show()

