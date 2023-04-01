import matplotlib.pyplot as plt
import math as mt
import numpy as np

def avalancheVariaBin(listaAvalanche):
    bins = [5,10, 15, 30, 50, 75, 100]

    for i in bins:
        plt.hist(listaAvalanche,bins = i,ec = "k", density = True)

        plt.xlabel("Tamanho da Avalanche (Energia)")
        plt.ylabel("Frequência Normalizada")
        plt.savefig('imagens\graficosFinais\FreqAvaEne(L=%i)(p=%.3f)(bins=%i).png' %(L,p,i))
        return plt.show()

def AvalanchePorP(listaAvalanche, p, L):

    bin = mt.sqrt(len(listaAvalanche))

    plt.hist(listaAvalanche,bins = int(bin),ec = "k", density = True, label = 'bins=%i' %(bin))
    plt.xlabel("Tamanho da Avalanche (Energia)")
    plt.ylabel("Frequência Normalizada")
    plt.legend(prop={'size': 15})
    plt.savefig('imagens\graficosFinais\FreqAvaEne(L=%i)(p=%.3f).png' %(L,p))
    return plt.show()


def AvalanchePorP_semiLogHist(listaAvalanche, p, L):

    bin = mt.sqrt(len(listaAvalanche))
    hist, bins = np.histogram(listaAvalanche, bins=int(bin))
    logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
    plt.hist(listaAvalanche, bins=logbins, label = 'bins=%i' %(bin))
    plt.xscale('log')
    plt.xlabel("Tamanho da Avalanche (Energia)")
    plt.ylabel("Frequência")
    plt.legend(prop={'size': 15})
    plt.savefig('imagens\graficosFinais\HistSLogFreqAvaEne(p=%.3f).png' %(p))
    plt.show()