import numpy as np
import numpy.matlib
import scipy.io as sio
import scipy.misc as scimisc
import sklearn.cluster as clust
import matplotlib.pyplot as plt
import sklearn.preprocessing as prep
import sklearn.decomposition as dec
#import sklearn.lda as lda
import sklearn.metrics as metrics
from scipy.sparse import coo_matrix
from scipy.special import comb
import sklearn.mixture as mix
import isodata
import scipy.signal as signal

# these functions are used to compute the rand index score
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


#show
def showByLabel(image,gt, label):


	row = gt.shape[0]
	col = gt.shape[1]
	gt = np.reshape(gt,(row*col))
	ind = np.where(gt==label)
	
	labels = np.zeros(row*col)
	labels[ind] = 10

	labels = np.reshape(labels,(row,col))
	plt.imshow(labels)
	plt.show()
	return labels


#plot a specific labels spectra
def plotSpecByLabel(image,gt,label):
	
	row = image.shape[0]
	col = image.shape[1]
	dim = image.shape[2]

	gt = np.reshape(gt,(row*col))
	ind = np.where(gt==label)

	
	image = np.reshape(image,(row*col,dim))

	xCoord = np.arange(0,dim,1)
	#plt.hold()
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)
	print(np.array(ind).shape)
	for i in range(0,np.array(ind).shape[1]):
		ax1.plot(xCoord,image[np.array(ind)[0][i],:])

	plt.show()
	return

#scales a particular band to be between 0 and 1 or an arbitrary upper limit
def scaleBand(band,scale=1):

	oneMat = np.ones((band.shape[0],band.shape[1]))
	bandMin = np.min(band) * oneMat
	band = (band - bandMin)
	bandMax = np.max(band) * oneMat
	band = (band/bandMax)*scale

	return band

# attempted to use these functions for background subtraction
def NDNI(uncorrectedData):

	band1510 = uncorrectedData[:,:,119]
	band1680 = uncorrectedData[:,:,136]
	oneMat = np.ones((145,145))

	ndni = (np.log(oneMat/band1510) - np.log(oneMat/band1680)) / (np.log(oneMat/band1510) + np.log(oneMat/band1680))
	ndni = scaleBand(ndni)

	return ndni


def NDWI(uncorrectedData):

	band860 = uncorrectedData[:,:,52]
	band1240 = uncorrectedData[:,:,90]

	ndwi = (band860 - band1240)/(band860 + band1240)
	ndwi = scaleBand(ndwi)

	return ndwi


def NDVI(uncorrectedData):

	band850 = indPines[:,:,49]
	band660 = indPines[:,:,28]

	ndvi = (band850 - band660)/(band850 + band660)
	ndvi = scaleBand(ndvi)

	return ndvi

# creates false color image of RGB for display
def falseColorImage(uncorrectedData):


	r = scaleBand(uncorrectedData[:,:,30],255).astype(np.uint8)
	g = scaleBand(uncorrectedData[:,:,14],255).astype(np.uint8)
	b = scaleBand(uncorrectedData[:,:,8],255).astype(np.uint8)
	
	rgb=np.dstack((r,g,b))

	return rgb

# to append spatial data to image
def appendCoordinateData(imageData,index,col):

	
	#reshape data if it hasn't already been

	xCoord = np.zeros((imageData.shape[0],1))
	yCoord = np.zeros((imageData.shape[0],1))
	print(imageData.shape)
	for i in range(0,imageData.shape[0]):
		xCoord[i] = np.mod(index[i],col)
		yCoord[i] = np.int(index[i]/col)


	print(xCoord.shape)
	print(yCoord.shape)
	imageData = np.hstack((imageData,xCoord))
	imageData = np.hstack((imageData,yCoord))

	return imageData




def loadData():

	indPinesCorrected = sio.loadmat('Indian_pines_corrected.mat')
	indPinesCorrected = indPinesCorrected['indian_pines_corrected']

	indPines = sio.loadmat('Indian_pines.mat')
	indPines = indPines['indian_pines']

	gt = sio.loadmat('Indian_pines_gt.mat')
	gt = gt['indian_pines_gt']
	
	

	return indPines,indPinesCorrected,gt

# applies an upper threshold to an image
def applyThreshold(image,threshold):

	row = image.shape[0]
	col = image.shape[1]

	labelMat = np.zeros((row,col))
	for i in range(0,row):
		for j in range(0,col):

			if(image[i][j] > threshold):
				labelMat[i][j] = 1
			else:
				labelMat[i][j] = 0

	return labelMat


# algorithm for split Band PCA

def splitBandPCA(flatImage, bandwidth):

	dim = flatImage.shape[1]

	numBands = int(dim/bandwidth)
	extras = np.mod(dim,bandwidth)

	whitenedData = np.zeros((flatImage.shape[0],numBands))

	startCounter = 0
	endCounter = bandwidth
	pca = dec.PCA(n_components=1,whiten=True)
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



# remove background for rand index scoring
def removeBackground(image_flat, groundTruth_flat):

	indices = np.where(groundTruth_flat==0)
	
	image_flat = np.delete(image_flat,indices)
	groundTruth_flat = np.delete(groundTruth_flat,indices)

	return image_flat,groundTruth_flat



if __name__ == '__main__':

	

	data,dataCorrected,groundTruth = loadData()

	row  = groundTruth.shape[0]
	col = groundTruth.shape[1]
	dim = data.shape[2]
	dimCorrected = dataCorrected.shape[2]

	


	
	

	reduced = np.load('Local_Split_PCA.npy')

	rows = reduced.shape[0]
	cols = reduced.shape[1]
	dims = reduced.shape[2]

	reduced = np.reshape(reduced,(rows*cols,dims))

	
	#set up parameters for ISODATA
	parameters = {'K':58,'I':1000,'P':2,'THETA_M':20}
	
	labels=isodata.isodata_classification(reduced,parameters)
	

	labelMat = np.reshape(labels,(rows,cols))

	#Optional median filtering on result
	#labelMat = signal.medfilt(labelMat,3)
	#labelMat = np.random.randint(0,16,(145,145))
	plt.imshow(labelMat)
	plt.show()
	

	# calculate Rand Index score
	labelMat,groundTruth_flat = removeBackground(np.reshape(labelMat,(145*145)),np.reshape(groundTruth,(145*145)))
	percentage = rand_score(groundTruth_flat, labelMat)
	print('Percent: ' + str(percentage))
	