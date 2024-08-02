import numpy as np
import matplotlib.pyplot as plt

def normalizedAvalanchesHistogram(data, p): 
    limites  =  []
    for n in range(16):
        # limites.append(1.4**n)
        limites.append(1.5**n)

    n, bins = np.histogram(data, bins=limites)

    bins_mean = [0.5 * (bins[i] + bins[i+1]) for i in range(len(n))]
    n_norm = [n[i]/(np.sum(data)*(1.5**(i+1) - 1.5**(i))) for i in range(len(n))]
    plt.scatter(bins_mean, n_norm)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Histogram for %.2f' %(p))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.xlim([1,1000])
    plt.ylim([0,1])
    plt.show()
    #plt.scatter(bins_mean, n)
    #plt.xscale('log')
    #plt.yscale('log')
    #plt.xlim([1,1000])
    #plt.ylim([10,1000])
    #plt.title('Histogram for %.2f' %(p))
    #plt.xlabel('Value')
    #plt.ylabel('Frequency')
    #plt.show()