


#Homework 2 for Introduction to Machine Learning and Pattern Recognition, Sp 2016
import numpy as np
import matplotlib.pyplot as plt
import math 
from decimal import *



if __name__ == '__main__':
    # parameters for the true Gaussian
    trueMean = 0.5
    fixedVariance = 0.2

    # parameters for the Gaussian prior on the trueMean
    priorMean = 0.5
    priorVariance = 0.2

    #perform iterative experiment
    numDraws = 10
    drawResult = []
    for draw in range(numDraws):
        drawResult.append(np.random.normal(trueMean, fixedVariance, 1)[0])
        print(["%.2f" % e for e in drawResult])
        print('Frequentist/Maximum Likelihood Probability of Heads:' + str(sum(drawResult)/len(drawResult)))
        print('Bayesian/MAP Probability of Heads:' + str((sum(drawResult)+priorMean)/(len(drawResult)+1)))
        input("Hit enter to continue...\n")
        
        






