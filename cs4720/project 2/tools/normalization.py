import numpy as np

def normalization(Images):
    index = range(len(Images))
    for i in index:
        data_max = np.max(Images[i,:])
        data_min = np.min(Images[i,:])
        if data_max-data_min!=0:
            Images[i,:] = (Images[i,:]-data_min)/(data_max-data_min)
    return Images
