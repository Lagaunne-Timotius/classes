README

**** To run project2 algorithm: 
make sure indian_pine_corrected data set is in the same folder as project2.py

python project2.py
    -> This has the implementation for Localized PCA and Split Band PCA for dimensionality reduction
    -> For clustering we have Kmeans, GMM & Fuzzy c-means clustering methods

Parameters are as follows:

nDim = Number of dimensions for locazlied PCA
n_clusters = 17 

**** To run ISODATA algorithm
make sure isodata.py is in same directory as runIsodata.py

python runIsodata.py

Parameters are as follows:

K = starting number of clusters
I = max iterations
P = number of clusters that can be merged, only tested with 2
THETA_M =  minimum number of points in a cluster before it is merged or deleted

This algorithm was ported from code for a single dimension found in pyradar.py and is not incredibly stable


To run LDA algorithm (LDA.py)
-make sure all the indianpines dataset are in in the correct path 
-make sure lda packages and other packages in anaconda also installed  
-output will be the document labels, words labels, images of LDA with its background, images of LDA after background removed and rand index score

To run Majority Voting (Voting_6_Classifier.py)
Noted : All the classification result are in each folder (lda_result, svm_result,gmm_result, kmeans_result,cmeans_result,isodata_result)

- Make sure all classifcation result are downloaded 
- Change the path of each label used for voting in the file
  + To use Split PCA , change the file name to algorithmname_labels_Split.npy
  + To use Local PCA , change the file neame to algorithmname_labels_Local.npy
  + To use Global PCA, change the file name to algorithmname_labels_Global.npy
  + To use Local_Split PCA, change the file name to algorithmname_labels_Local_Split.npy
- To add or reduce the number of classifier 
  +Add or reduce the number of input based on the classifier in voting function
  +Change the input of the function as well in the main 
- Newlabeleddata
  +new_data1= changelabel(newlabelA,lda)
  +new_data2= changelabel(newlabelB,gmm)
  +new_data3= changelabel(newlabelC,isodata)
  +new_data4= changelabel(newlabelC,cmeans)
  +new_data5= changelabel(newlabelC,svm)
  +kmeans= kmeans
- The output will be the voting resulted image and the voting resulted image after the background removed
  
To run Two_Stage_Classification_Final:
The code has two part: stage1 and stage2
for stage 1 : options are K-means and C-means
for stage 2: if you are using K-means in stage1 use Window searching but if you are using C-means you can use both window searching and weighting to eliminate outliers.

to compare with other methods, data has been loaded(LPCA,Local_Split_PCA, GPCA)
By setting threshold and window you can define how eliminate outliers.



