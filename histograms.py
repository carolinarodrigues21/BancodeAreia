import numpy as np
import matplotlib.pyplot as plt

def normalizedAvalanchesHistogram(data, p): 
    limites  =  []
    for n in range(16):
        limites.append(1.4**n)

    plt.hist(data, bins=limites, edgecolor='black', density=True)
    plt.xscale('log')
    plt.title('Histogram for %.2f' %(p))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()