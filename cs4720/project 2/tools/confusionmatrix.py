import numpy as np

def confusionmatrix(y_test,y_pred):
  combine= np.vstack((y_test,y_pred))
  labels = numpy.unique(combine)
  conMat = np.zeros((len(labels),len(labels)))
  length = range(len(labels))
  new = dict(zip(length, zip(labels)))
  index = range(len(y_test))
  for i in index:
      for key1, value1 in new.items():
          for key2, value2 in new.items():
              if y_test[i] == value1:  
                  if y_pred[i] == value2:
                      conMat[key1,key2] += 1
  return conMat.astype(int)
