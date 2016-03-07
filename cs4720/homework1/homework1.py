
#Homework 1 for Introduction to Machine Learning and Pattern Recognition, Sp 2016
#Recreate Figures 1.4, 1.5, 1.6 and 1.7 in the text
import numpy as np
import matplotlib.pyplot as plt
import math 
import textwrap


def generateData(N, l, u, gVar):
	'''generateData(N, l, u, gVar): Generate N uniformly spaced data points in the range [l,u) with zero-mean Gaussian random noise with variance gVar'''
	# x = np.random.uniform(l,u,N)
	step = (u-l)/(N);
	x = np.arange(l+step/2,u+step/2,step)
	e = np.random.normal(0,gVar,N)
	t = np.sin(2*math.pi*x) + e
	return x,t
    
def generateRandData(N, l, u, gVar):
	'''generateRandData(N, l, u, gVar): Generate N uniformly random data points in the range [l,u) with zero-mean Gaussian random noise with variance gVar'''
	x = np.random.uniform(l,u,N)
	e = np.random.normal(0,gVar,N)
	t = np.sin(2*math.pi*x) + e
	return x,t

def fitdata(x,t,M):
	'''fitdata(x,t,M): Fit a polynomial of order M to the data (x,t)'''	
	X = np.array([x**m for m in range(M+1)]).T
	w = np.linalg.inv(X.T@X)@X.T@t
	return w

def fitdata_regularized(x,t,M,L):
    '''fitdata(x,t,M): Fit a polynomial of order M to the data (x,t)'''
    I=np.identity(M+1)
    X = np.array([x**m for m in range(M+1)]).T
    w = np.linalg.inv(X.T@X+(L*I))@X.T@t
    return w


def plotPoly(x,t,w,l,u,subplotloc):
	'''plotPoly(x,t,w,l,u,subplotloc): Plot data (x,t) and the polynomial with parameters w across the range [l,u) in a sub figure at location subplotloc'''
	xrange = np.arange(l,u,0.001)  #get equally spaced points in the xrange
	y = np.sin(2*math.pi*xrange) #compute the true function value
	X = np.array([xrange**m for m in range(w.size)]).T
	esty = X@w #compute the predicted value

	#plot everything
	plt.subplot(*subplotloc) #identify the subplot to use
	plt.tight_layout()
	p1 = plt.plot(xrange, y, 'g') #plot true value
	p2 = plt.plot(x, t, 'bo') #plot training data
	p3 = plt.plot(xrange, esty, 'r') #plot estimated value

	#add title, legend and axes labels
	plt.ylabel('t') #label x and y axes
	plt.xlabel('x')
	plt.rcParams["axes.titlesize"] = 10
	myTitle = 'Plot of data, true function, and estimated polynomial with order M = ' + str(w.size-1) + ' and N =' + str(x.size)
	fig.add_subplot(*subplotloc).set_title("\n".join(textwrap.wrap(myTitle, 50)))
	plt.legend((p1[0],p2[0],p3[0]),('True Function', 'Training Data', 'Estimated\nPolynomial'), fontsize=6)
    
    #generating rms for test and training data
def datarms(N,x1,t1,x2,t2):
    #initializing list 
    trainingrms=[]
    testrms=[]
    #initializing order of polynomial
    a=[0,1,2,3,4,5,6,7,8,9]
    #looped through the order of polynomial to get the rms of each order
    for i in a:
        w= fitdata(x1,t1,i)
        X = np.array([x1**m for m in range(w.size)]).T
        esty = X@w #compute the predicted value
        
        error=0.5*sum((esty-t1)**2)
        rms=((2*error)/N)**(0.5)
        trainingrms.append(rms)
        
        X = np.array([x2**m for m in range(w.size)]).T
        esty= X@w
        error=0.5*sum((esty-t2)**2)
        rms=((2*error)/N)**(0.5)
        testrms.append(rms)
        
    #return order and rms of training and test data    
    return a,trainingrms,testrms
            

if __name__ == '__main__':
    #figure 1.4
    fig = plt.figure()

    x1,t1 = generateData(10,0,1,.25)  #generate N data points in the range [0,1]
    w = fitdata(x1,t1,0) #fit a polynomial of order 0 to the data x,t
    plotPoly(x1,t1,w,0.05,.95,[2,2,1]) #plot the data and the polynomial that was estimated

    w = fitdata(x1,t1,1) #fit a polynomial of order 1 to the data x,t
    plotPoly(x1,t1,w,0.05,.95,[2,2,2]) #plot the data and the polynomial that was estimated

    w = fitdata(x1,t1,3) #fit a polynomial of order 3 to the data x,t
    plotPoly(x1,t1,w,0.05,.95,[2,2,3]) #plot the data and the polynomial that was estimated

    w = fitdata(x1,t1,9) #fit a polynomial of order 9 to the data x,t
    plotPoly(x1,t1,w,0.05,.95,[2,2,4])  #plot the data and the polynomial that was estimated

    plt.savefig('fig1_4.pdf') #save resulting figure into pdf file named fig1_4.pdf
    plt.show()
    
    #figure 1.5
    fig2 = plt.figure()
    #training data 
    x1,t1 = generateData(10,0,1,.25)
    #test data
    x2,t2 = generateData(10,0,1,.25)
    
    #fitting model 
    a,trainingrms,testrms =datarms(10,x1,t1,x2,t2)
    #ploting data
    p1=plt.plot(a,trainingrms,'b')
    p2=plt.plot(a,trainingrms,'bo')
    p3=plt.plot(a,testrms,'r')
    p4=plt.plot(a,testrms,'ro')
    #adding axis label
    plt.ylabel('Erms') #label x and y axes
    plt.xlabel('M')
    #adding legend
    plt.legend((p3[0],p1[0]),('Training','Test'), fontsize=12)
    plt.savefig('fig1_5.pdf') #save resulting figure into pdf file named fig1_5.pdf
    
    #figure 1.6
    fig3 = plt.figure()
    
    x1,t1 = generateData(15,0,1,.25) #generating 15 random data 
    w1 = fitdata(x1,t1,9) #fit a polynomial of order M to the data x,t
    plotPoly(x1,t1,w1,0.05,.95,[1,2,1]) #plot the data and the polynomial that was estimated
    
    x2,t2 = generateData(100,0,1,.25) #generating 100 random data
    w2 = fitdata(x2,t2,9) #fit a polynomial of order M to the data x,t
    plotPoly(x2,t2,w2,0.05,.95,[1,2,2]) #plot the data and the polynomial that was estimated

    plt.savefig('fig1_6.pdf') #save resulting figure into pdf file named fig1_6.pdf
    
    #figure 1.7
    fig4 = plt.figure()
    
    x,t = generateData(10,0,1,.25) #generating random data
    w1 = fitdata_regularized(x,t,9,math.exp(-18)) #fit a polynomial of order 9 with lambda=exp(-18) to the data x,t
    plotPoly(x,t,w1,0.05,.95,[1,2,1]) #plot the data and the polynomial that was estimated
    
    w2 = fitdata_regularized(x,t,9,math.exp(0))#fit a polynomial of order 9 with lambda=exp(0) to the data x,t
    plotPoly(x,t,w2,0.05,.95,[1,2,2]) #plot the data and the polynomial that was estimated
    
    plt.savefig('fig1_7.pdf') #save resulting figure into pdf file named fig1_7.pdf
    plt.show()
    
    







