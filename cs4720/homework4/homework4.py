import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
import math 
import textwrap

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

def sample_w(mn,sn,N):
    w=np.random.multivariate_normal(mn,np.linalg.inv(sn),N)
    return w


def fig3_8():
    '''Recreate Figure 3_8 from the text.'''
    # set parameters
    pltrange = [-1,2]
    s = 0.1 #variance parameter for RBFs
    beta = 10 #noise precision
    alpha = 0.001 #prior precision
    m0 = 0 #prior mean
    datapoints={0:1,1:2,2:4,3:25}
    
    fig = plt.figure()
    for counter,o in datapoints.items():
      
        numPoints = o #number of training points
         
        #generate training data
        [data, t] = generateRandData(numPoints, 0, 1, 1/beta)

        # Compute Phi (i.e., put training data through basis functions)
        phi = computePhi(data, s)
    
        # Compute posterior mean, mn, and covariance, Sn
        sn = alpha*np.eye(data.shape[0])+beta*phi.T@phi
        mn = beta*np.linalg.inv(sn)@phi.T@t.T

        #Compute predictive mean and predictive variance
        xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
        mx = [mn.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
        sx = [(1/beta)+np.exp(-0.5*(i-data)*(i-data)/s)@np.linalg.inv(sn)@np.exp(-0.5*(i-data)*(i-data)/s).T for i in xx]
        
        plt.subplot(*[2,2,counter+1]) #identify the subplot to use
        plt.tight_layout()
        
        #Plot everything
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
        plt.ylabel('t') #label x and y axes
        plt.xlabel('x')
        plt.rcParams["axes.titlesize"] = 10
        myTitle = 'Plot of t with Num_points = '+ str(o)
        fig.add_subplot(*[2,2,counter+1]).set_title("\n".join(textwrap.wrap(myTitle, 50)))
    plt.show()

def modified_beta_fig3_8(N):
    '''Recreate Figure 3_8 from the text.'''
    # set parameters
    pltrange = [-1,2]
    s = 0.1 #variance parameter for RBFs
    #beta = 10 #noise precision
    alpha = 0.001 #prior precision
    m0 = 0 #prior mean
    beta={0:1,1:5,2:10,3:20}
    fig = plt.figure()
    
    for counter,o in beta.items():
      
        numPoints = N #number of training points
        beta=o
        #generate training data
        [data, t] = generateRandData(numPoints, 0, 1, 1/beta)

        # Compute Phi (i.e., put training data through basis functions)
        phi = computePhi(data, s)
    
        # Compute posterior mean, mn, and covariance, Sn
        sn = alpha*np.eye(data.shape[0])+beta*phi.T@phi
        mn = beta*np.linalg.inv(sn)@phi.T@t.T

        #Compute predictive mean and predictive variance
        xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
        mx = [mn.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
        sx = [(1/beta)+np.exp(-0.5*(i-data)*(i-data)/s)@np.linalg.inv(sn)@np.exp(-0.5*(i-data)*(i-data)/s).T for i in xx]
        
        plt.subplot(*[2,2,counter+1]) #identify the subplot to use
        plt.tight_layout()
        
        #Plot everything
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
        plt.ylabel('t') #label x and y axes
        plt.xlabel('x')
        plt.rcParams["axes.titlesize"] = 10
        myTitle = 'Plot of t with beta = '+ str(beta)
        fig.add_subplot(*[2,2,counter+1]).set_title("\n".join(textwrap.wrap(myTitle, 50)))
    plt.show()

def modified_alpha_fig3_8(N):
    '''Recreate Figure 3_8 from the text.'''
    # set parameters
    pltrange = [-1,2]
    s = 0.1 #variance parameter for RBFs
    beta = 10 #noise precision
    #alpha = 0.001 #prior precision
    m0 = 0 #prior mean
    
    
    alpha={0:0.0001,1:0.0005,2:0.001,3:0.1}
    fig = plt.figure()
    for counter,o in alpha.items():
      
        numPoints = N #number of training points
        alpha=o
        #generate training data
        [data, t] = generateRandData(numPoints, 0, 1, 1/beta)

        # Compute Phi (i.e., put training data through basis functions)
        phi = computePhi(data, s)
    
        # Compute posterior mean, mn, and covariance, Sn
        sn = alpha*np.eye(data.shape[0])+beta*phi.T@phi
        mn = beta*np.linalg.inv(sn)@phi.T@t.T

        #Compute predictive mean and predictive variance
        xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
        mx = [mn.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
        sx = [(1/beta)+np.exp(-0.5*(i-data)*(i-data)/s)@np.linalg.inv(sn)@np.exp(-0.5*(i-data)*(i-data)/s).T for i in xx]
        
        plt.subplot(*[2,2,counter+1]) #identify the subplot to use
        plt.tight_layout()
        
        #Plot everything
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
        plt.ylabel('t') #label x and y axes
        plt.xlabel('x')
        plt.rcParams["axes.titlesize"] = 10
        myTitle = 'Plot of t with alpha = '+ str(alpha)
        fig.add_subplot(*[2,2,counter+1]).set_title("\n".join(textwrap.wrap(myTitle, 50)))
    plt.show()
    
def fig3_9():
    '''Recreate Figure 3_9 from the text.'''
    # set parameters
    pltrange = [0,1]
    s = 0.1 #variance parameter for RBFs
    beta = 10 #noise precision
    alpha = 0.001 #prior precision
    m0 = 0 #prior mean
    #row and column sharing
    datapoints={0:1,1:2,2:4,3:25}
    fig = plt.figure()
    for counter,o in datapoints.items():
        
        numPoints = o #number of training points
        #generate training data
        [data, t] = generateRandData(numPoints, 0, 1, 1/beta)

        # Compute Phi (i.e., put training data through basis functions)
        phi = computePhi(data, s)
    
        # Compute posterior mean, mn, and covariance, Sn
        sn = alpha*np.eye(data.shape[0])+beta*phi.T@phi
        mn = beta*np.linalg.inv(sn)@phi.T@t.T

        #Compute predictive mean and predictive variance
        xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
        mx = [mn.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
        sx = [(1/beta)+np.exp(-0.5*(i-data)*(i-data)/s)@np.linalg.inv(sn)@np.exp(-0.5*(i-data)*(i-data)/s).T for i in xx]
        
        plt.subplot(*[2,2,counter+1]) #identify the subplot to use
        plt.tight_layout()
        #w_sampling
        w=sample_w(mn,sn,5)
        mx1=[]
    
        for j in w:
            value = [j.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
            mx1.append(value)
        #Plot Everything
        for l in mx1:
            plt.plot( xx,l, c='r')
        
        plt.plot( xx, [math.sin(2*math.pi*i) for i in xx], c='b')
        plt.scatter(data, t, linewidth=3)
        ymin = min(np.hstack((mx-np.sqrt(sx)-1, [np.sin(2*math.pi*i) for i in xx])))
        ymax = max(mx+np.sqrt(sx)+1)
        yy = np.arange(ymin,ymax,0.01)
        plt.axis([pltrange[0], pltrange[1], ymin, ymax])
        plt.ylabel('t') #label x and y axes
        plt.xlabel('x')
        plt.rcParams["axes.titlesize"] = 10
        myTitle = 'Plot of t with Num points = '+ str(o)
        fig.add_subplot(*[2,2,counter+1]).set_title("\n".join(textwrap.wrap(myTitle, 50)))
    
    plt.show()

def modified_alpha_fig3_9(N):
    '''Recreate Figure 3_9 from the text.'''
    # set parameters
    pltrange = [0,1]
    s = 0.1 #variance parameter for RBFs
    beta = 10 #noise precision
    #alpha = 0.001 #prior precision
    m0 = 0 #prior mean
    #row and column sharing
    alpha={0:0.0001,1:0.0005,2:0.001,3:0.1}
    fig = plt.figure()
    for counter,o in alpha.items():
        
        numPoints = N #number of training points
        alpha=o
        #generate training data
        [data, t] = generateRandData(numPoints, 0, 1, 1/beta)

        # Compute Phi (i.e., put training data through basis functions)
        phi = computePhi(data, s)
    
        # Compute posterior mean, mn, and covariance, Sn
        sn = alpha*np.eye(data.shape[0])+beta*phi.T@phi
        mn = beta*np.linalg.inv(sn)@phi.T@t.T

        #Compute predictive mean and predictive variance
        xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
        mx = [mn.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
        sx = [(1/beta)+np.exp(-0.5*(i-data)*(i-data)/s)@np.linalg.inv(sn)@np.exp(-0.5*(i-data)*(i-data)/s).T for i in xx]
        
        plt.subplot(*[2,2,counter+1]) #identify the subplot to use
        plt.tight_layout()
        #w_sampling
        w=sample_w(mn,sn,5)
        mx1=[]
    
        for j in w:
            value = [j.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
            mx1.append(value)
        #Plot Everything
        for l in mx1:
            plt.plot( xx,l, c='r')
            
        plt.plot( xx, [math.sin(2*math.pi*i) for i in xx], c='b')
        plt.scatter(data, t, linewidth=3)
        ymin = min(np.hstack((mx-np.sqrt(sx)-1, [np.sin(2*math.pi*i) for i in xx])))
        ymax = max(mx+np.sqrt(sx)+1)
        yy = np.arange(ymin,ymax,0.01)
        plt.axis([pltrange[0], pltrange[1], ymin, ymax])
        plt.ylabel('t') #label x and y axes
        plt.xlabel('x')
        plt.rcParams["axes.titlesize"] = 10
        myTitle = 'Plot of t with alpha = '+ str(alpha)
        fig.add_subplot(*[2,2,counter+1]).set_title("\n".join(textwrap.wrap(myTitle, 50)))
    plt.show()

def modified_beta_fig3_9(N):
    '''Recreate Figure 3_9 from the text.'''
    # set parameters
    pltrange = [0,1]
    s = 0.1 #variance parameter for RBFs
    #beta = 10 #noise precision
    alpha = 0.001 #prior precision
    m0 = 0 #prior mean
    #row and column sharing
    beta={0:1,1:5,2:10,3:20}
    fig = plt.figure()
    for counter,o in beta.items():
        
        numPoints = N #number of training points
        beta=o
        #generate training data
        [data, t] = generateRandData(numPoints, 0, 1, 1/beta)

        # Compute Phi (i.e., put training data through basis functions)
        phi = computePhi(data, s)
    
        # Compute posterior mean, mn, and covariance, Sn
        sn = alpha*np.eye(data.shape[0])+beta*phi.T@phi
        mn = beta*np.linalg.inv(sn)@phi.T@t.T

        #Compute predictive mean and predictive variance
        xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
        mx = [mn.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
        sx = [(1/beta)+np.exp(-0.5*(i-data)*(i-data)/s)@np.linalg.inv(sn)@np.exp(-0.5*(i-data)*(i-data)/s).T for i in xx]
        
        plt.subplot(*[2,2,counter+1]) #identify the subplot to use
        plt.tight_layout()
        #w_sampling
        w=sample_w(mn,sn,5)
        mx1=[]
    
        for j in w:
            value = [j.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
            mx1.append(value)
        #Plot Everything
        for l in mx1:
            plt.plot( xx,l, c='r')
            
        plt.plot( xx, [math.sin(2*math.pi*i) for i in xx], c='b')
        plt.scatter(data, t, linewidth=3)
        ymin = min(np.hstack((mx-np.sqrt(sx)-1, [np.sin(2*math.pi*i) for i in xx])))
        ymax = max(mx+np.sqrt(sx)+1)
        yy = np.arange(ymin,ymax,0.01)
        plt.axis([pltrange[0], pltrange[1], ymin, ymax])
        plt.ylabel('t') #label x and y axes
        plt.xlabel('x')
        plt.rcParams["axes.titlesize"] = 10
        myTitle = 'Plot of t with beta = '+ str(beta)
        fig.add_subplot(*[2,2,counter+1]).set_title("\n".join(textwrap.wrap(myTitle, 50)))
    plt.show()
    
def modified_s_fig3_9(N):
    '''Recreate Figure 3_9 from the text.'''
    # set parameters
    pltrange = [0,1]
    #s = 0.1 #variance parameter for RBFs
    beta = 10 #noise precision
    alpha = 0.001 #prior precision
    m0 = 0 #prior mean
    #row and column sharing
    s={0:0.01,1:0.1,2:0.5,3:1}
    fig = plt.figure()
    for counter,o in s.items():
        
        numPoints = N #number of training points
        s=o
        #generate training data
        [data, t] = generateRandData(numPoints, 0, 1, 1/beta)

        # Compute Phi (i.e., put training data through basis functions)
        phi = computePhi(data, s)
    
        # Compute posterior mean, mn, and covariance, Sn
        sn = alpha*np.eye(data.shape[0])+beta*phi.T@phi
        mn = beta*np.linalg.inv(sn)@phi.T@t.T

        #Compute predictive mean and predictive variance
        xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
        mx = [mn.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
        sx = [(1/beta)+np.exp(-0.5*(i-data)*(i-data)/s)@np.linalg.inv(sn)@np.exp(-0.5*(i-data)*(i-data)/s).T for i in xx]
        
        plt.subplot(*[2,2,counter+1]) #identify the subplot to use
        plt.tight_layout()
        #w_sampling
        w=sample_w(mn,sn,5)
        mx1=[]
    
        for j in w:
            value = [j.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
            mx1.append(value)
        #Plot Everything
        for l in mx1:
            plt.plot( xx,l, c='r')
            
        plt.plot( xx, [math.sin(2*math.pi*i) for i in xx], c='b')
        plt.scatter(data, t, linewidth=3)
        ymin = min(np.hstack((mx-np.sqrt(sx)-1, [np.sin(2*math.pi*i) for i in xx])))
        ymax = max(mx+np.sqrt(sx)+1)
        yy = np.arange(ymin,ymax,0.01)
        plt.axis([pltrange[0], pltrange[1], ymin, ymax])
        plt.ylabel('t') #label x and y axes
        plt.xlabel('x')
        plt.rcParams["axes.titlesize"] = 10
        myTitle = 'Plot of t with s = '+ str(s)
        fig.add_subplot(*[2,2,counter+1]).set_title("\n".join(textwrap.wrap(myTitle, 50)))
    plt.show()
    
def modified_s_fig3_8(N):
    '''Recreate Figure 3_8 from the text.'''
    # set parameters
    pltrange = [-1,2]
    #s = 0.1 #variance parameter for RBFs
    beta = 10 #noise precision
    alpha = 0.001 #prior precision
    m0 = 0 #prior mean
    
    #row and column sharing
    s={0:0.01,1:0.1,2:0.5,3:1}
    fig = plt.figure()
    for counter,o in s.items():
      
        numPoints = N #number of training points
        s=o
        
        #generate training data
        [data, t] = generateRandData(numPoints, 0, 1, 1/beta)

        # Compute Phi (i.e., put training data through basis functions)
        phi = computePhi(data, s)
    
        # Compute posterior mean, mn, and covariance, Sn
        sn = alpha*np.eye(data.shape[0])+beta*phi.T@phi
        mn = beta*np.linalg.inv(sn)@phi.T@t.T

        #Compute predictive mean and predictive variance
        xx =  np.arange(pltrange[0],pltrange[1],0.01) #all data points to compute the predictive mean and variance at
        mx = [mn.T@(np.exp(-0.5*(i-data)*(i-data)/s)).T for i in xx] 
        sx = [(1/beta)+np.exp(-0.5*(i-data)*(i-data)/s)@np.linalg.inv(sn)@np.exp(-0.5*(i-data)*(i-data)/s).T for i in xx]
        
        plt.subplot(*[2,2,counter+1]) #identify the subplot to use
        plt.tight_layout()
        
        #Plot everything
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
        plt.ylabel('t') #label x and y axes
        plt.xlabel('x')
        plt.rcParams["axes.titlesize"] = 10
        myTitle = 'Plot of t with s = '+ str(s)
        fig.add_subplot(*[2,2,counter+1]).set_title("\n".join(textwrap.wrap(myTitle, 50)))
    plt.show()
if __name__ == '__main__':
    fig3_9()
    fig3_8()
    modified_beta_fig3_8(10)
    modified_beta_fig3_9(10)
    modified_alpha_fig3_8(10)
    modified_alpha_fig3_9(10)
    modified_s_fig3_8(10)
    modified_s_fig3_9(10)
    





