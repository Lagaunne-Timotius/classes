import numpy as np
import numpy.matlib
import scipy.io as sio
import sklearn.cluster as clust
import matplotlib.pyplot as plt
import sklearn.preprocessing as prep
import sklearn.decomposition as dec


#def pca():

if __name__ == '__main__':

	indPines = sio.loadmat('Indian_pines_corrected.mat')
	indPines = indPines['indian_pines_corrected']
	gt = sio.loadmat('Indian_pines_gt.mat')
	#print(gt)
	gt = gt['indian_pines_gt']
	xCoord = np.arange(0,145,1)
	xCoord = np.matlib.repmat(xCoord,1,145)
	print(xCoord.shape)
	#indPines = indPines[0:10,0:10,:]
	indPines=np.reshape(indPines,(145*145,200))
	indPines = np.hstack((indPines,xCoord.T))

	yCounter = np.zeros(145)
	addArr = np.ones(145)
	print(indPines.shape)
	yCoord = []
	for i in range(0,145):
		yCoord = np.hstack((yCoord,yCounter))
		yCounter = yCounter + addArr

	yCoord = np.reshape(yCoord,(1,145*145))
	indPines = np.hstack((indPines,yCoord.T))
	print(indPines.shape)
	

	# means=np.mean(indPines,axis=0)
	# variance = np.var(indPines,axis=0)
	# means = np.matlib.repmat(means,145*145,1)
	# variance = np.matlib.repmat(variance,145*145,1)
	# normIndPines = (indPines - means) / variance
	
	normIndPines=prep.normalize(indPines,axis=1)
	whiten = dec.PCA(n_components=150,whiten=True)
	redIndPines=whiten.fit_transform(normIndPines)


	print(np.cov(normIndPines).shape)
	#print(normIndPines.shape)


	kmeans = clust.KMeans(n_clusters=17,init='k-means++', n_init=17)
	labels = kmeans.fit_predict(redIndPines)
	# #kmeans.predict(indPines)
	print(labels.shape)
	labels=np.reshape(labels,(145,145))
	print(labels.shape)
	plt.imshow(labels)
	plt.show()
	plt.imshow(gt)
	plt.show()


	

	#np.imshow(labels)
