import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
import math 

def generateRandData(N, l, u, gVar):
	'''generateRandData(N, l, u, gVar): Generate N uniformly random data points in the range [l,u) with zero-mean Gaussian random noise with variance gVar'''
	x = np.random.uniform(l,u,N)
	e = np.random.normal(0,gVar,N)
	t = np.sin(2*math.pi*x) + e
	return x,t

def pdist1D(X):
	'''pdist1D(X): computes pairwise squared euclidean distance between 1D points stored in a vector X'''
	X = np.matlib.repmat(X, X.shape[0], 1);
	D = X-X.T
	return D*D

def computePhi(X, s=1):
	'''computePhi(X, s)'''
	D = pdist1D(X)
	phi = np.exp(-0.5*D/s)
	return phi

	return 0

def fig3_8():
	'''Recreate Figure 3_8 from the text.'''
	# set parameters
	s = 0.1 #variance parameter for RBFs
	beta = 10 #noise precision
	alpha = 0.001 #prior precision
	m0 = 0 #prior mean
	numPoints = 10 #number of training points
	pltrange = [-1,2]

	#generate training data
	[data, t] = generateRandData(numPoints, 0, 1, 1/beta)

	# Compute Phi (i.e., put training data through basis functions)
	phi = computePhi(data, s)

	# Compute posterior mean, mn, and covariance, Sn
	Sn = #fill this in
	mn = #fill this in

	#Compute predictive mean and predictive variance
	xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
	mx = #fill this in, predictive mean at each i in xx, hint, can use: [ ***expression for mean of one i here*** for i in xx]
	sx = #fill this in, predictive variance at each i in xx, hint, can use: [ ***expression for variance of one i here*** for i in xx]
	
	# Plot everything
	fig = plt.figure()
	plt.errorbar( xx, mx, sx, linewidth=5, alpha=0.1)
	plt.plot( xx, mx, c='r')
	plt.plot( xx, [math.sin(2*math.pi*i) for i in xx], c='b')
	plt.scatter(data, t, linewidth=3)
	ymin = min(np.hstack((mx-np.sqrt(sx)-1, [np.sin(2*math.pi*i) for i in xx])))
	ymax = max(mx+np.sqrt(sx)+1)
	yy = np.arange(ymin,ymax,0.01)
	for i in range(data.shape[0]):
		yx = data[i]*np.ones(yy.shape)
		plt.plot(yx,yy,c='g',linewidth=1)

	plt.axis([pltrange[0], pltrange[1], ymin, ymax])
	plt.show()


if __name__ == '__main__':
	fig3_8()