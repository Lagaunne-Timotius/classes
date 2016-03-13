import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
import matplotlib.image as mping
import math
from skimage import data
from skimage.transform import resize
from sklearn import preprocessing
from skimage import feature
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
#Feature extraction
Images = np.load("C:\\Users\\talyxd\\Documents\\project1-intelli-script\\TrainImages.npy")

from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.transform import warp, AffineTransform
from skimage.feature import hog

min_max_scaler = preprocessing.MinMaxScaler()
data_final=np.array([[]])
index=range(0,1655)
for a in index:
    temp= resize(Images[a], (20, 20))
    temp= min_max_scaler.fit_transform(temp)
    temp=np.around(temp,decimals=0)
    temp=hog(temp, orientations=9,pixels_per_cell=(5,5),cells_per_block=(1,1),visualise=False)
    temp=np.array([temp])
    if a == 0:
        data_final=temp
    else:
        data_final=np.concatenate((data_final,temp),axis=0)
        
X=data_final
Y = np.load("C:\\Users\\talyxd\\Documents\\project1-intelli-script\\TrainY.npy")

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5,random_state=2)

clf = LinearSVC()
clf.fit(X_train, y_train)  
y_pred=clf.predict(X_test)
print(y_pred.shape)

confusion_matrix(y_test, y_test)
confusion_matrix(y_test, y_pred)
