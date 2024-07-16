import numpy as np
import matplotlib.pyplot as plt

def normalizedAvalanchesHistogram(data, p): 
    limites  =  []
    for n in range(16):
        limites.append(1.4**n)

    n, bins = np.histogram(data, bins=limites)

    bins_mean = [0.5 * (bins[i] + bins[i+1]) for i in range(len(n))]
    plt.scatter(bins_mean, n)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim([1,1000])
    plt.ylim([1,1000])
    plt.title('Histogram for %.2f' %(p))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()