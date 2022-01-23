import matplotlib.pyplot as plt
import numpy as np
import spectral as spy
from scipy.io import loadmat

if __name__ == '__main__':
    data = loadmat('Indian_pines_corrected.mat')
    data = data['indian_pines_corrected']

    gt = loadmat('Indian_pines_gt.mat')
    gt = gt['indian_pines_gt']
    
    ntopics = 17   # number of topics to generate
    (kmeans_classes, c) = spy.kmeans(data, nclusters=ntopics, max_iterations=100)
    kmeans_classes += 1
        
    
    fig = plt.figure(figsize=(12,6))
    p = plt.subplot(2, 1, 1)
    v = spy.imshow(classes=gt, fignum=fig.number)
    p.set_title('Ground Truth')
    
    p = plt.subplot(2, 1, 2)
    v = spy.imshow(classes=kmeans_classes , fignum=fig.number)
    p.set_title('k-means classes');
    plt.show(v)