import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def normalizedAvalanchesHistogram(data, p): 
    limites  =  []
    for n in range(16):
        # limites.append(1.4**n)
        limites.append(1.5**n)

    n, bins = np.histogram(data, bins=limites)

    bins_mean = [0.5 * (bins[i] + bins[i+1]) for i in range(len(n))]
    n_norm = [n[i]/(np.sum(data)*(1.5**(i+1) - 1.5**(i))) for i in range(len(n))]
    # plt.scatter(bins_mean, n_norm)
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.title('Histogram for %.2f' %(p))
    # plt.xlabel('Value')
    # plt.ylabel('Frequency')
    # plt.xlim([1,1000])
    # plt.ylim([0,1])
    # plt.show()
    #plt.scatter(bins_mean, n)
    #plt.xscale('log')
    #plt.yscale('log')
    #plt.xlim([1,1000])
    #plt.ylim([10,1000])
    #plt.title('Histogram for %.2f' %(p))
    #plt.xlabel('Value')
    #plt.ylabel('Frequency')
    #plt.show()

    print(bins_mean)
    print(n_norm)

    for i in [-2,-1,0]:
        bins_mean.pop(i)
        n_norm.pop(i)

    print(bins_mean)
    print(n_norm)

    def fit(x,a,b):
        return np.exp(b) * x**(a)

    popt, pcov = curve_fit(fit, bins_mean, n_norm)
    a,b = popt
    erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
    errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear

    plt.scatter(bins_mean, n_norm)
    plt.plot(bins_mean,fit(bins_mean,a,b), color = "red", label = "a =%.2f $\pm$ %.2f \nb =%.2f $\pm$ %.2f" %(a,erra,b,errb))
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Histogram for %.2f' %(p))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    # plt.xlim([1,1000])
    # plt.ylim([0,1])
    plt.legend()
    plt.show()