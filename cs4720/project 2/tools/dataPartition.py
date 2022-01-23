import numpy as np

def dataPartition(X,Y,test_size):
    count = math.ceil((1-test_size)*len(Y))
    X_train = np.array([[]])
    y_train = np.array([[]])
    X_test = np.array([[]])
    y_test = np.array([[]])
    numArray = []
    
    while len(numArray)<count:
        n = np.random.random_integers(0,len(X)-1) #generate random integer
        if n not in numArray:
            numArray.append(n)
    numArray=sorted(numArray)
    X_train=X[numArray,:]
    y_train=Y[numArray]
    a=list(range(len(Y)))
    for i in range(len(numArray)):
        a.remove(numArray[i])
    X_test = X[a,:] #store random X in X_train
    y_test = Y[a] #store random Y in y_train
      
    return X_train,X_test,y_train,y_test
