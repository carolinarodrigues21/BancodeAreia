import matplotlib.pyplot as plt
import math as mt
import numpy as np

def avalancheVariaBin(listaAvalanche):
    bins = [5,10, 15, 30, 50, 75, 100]

    for i in bins:
        plt.hist(listaAvalanche,bins = i,ec = "k", density = True)
        plt.title("Frequência de Avalanches por Energia (bins = %i)" %(i))
        plt.grid(True)
        plt.xlabel("Tamanho da Avalanche (Energia)")
        plt.ylabel("Frequência Normalizada")
        plt.savefig('imagens\graficosFinais\Freq(L=%i)(p=%.3f)(bins=%i).png' %(L,p,i))
        return plt.show()

def AvalanchePorP(listaAvalanche, p, L):

    # bin = mt.sqrt(len(listaAvalanche))
    bin = 5

    plt.hist(listaAvalanche,bins = int(bin),ec = "k", density = True)
    plt.title("Frequência de Avalanches por Energia (bins = %i)" %(bin))
    plt.grid(True)
    plt.xlabel("Tamanho da Avalanche (Energia)")
    plt.ylabel("Frequência Normalizada")
    plt.savefig('imagens\graficosFinais\Freq(L=%i)(p=%.3f).png' %(L,p))
    return plt.show()


def AvalanchePorP_semiLogHist(listaAvalanche, p, L):

    bin = mt.sqrt(len(listaAvalanche))
    hist, bins = np.histogram(listaAvalanche, bins=int(bin))
    logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
    plt.title("Frequência de Avalanches por Energia (bins = %i) (p = %.2f)" %(bin, p))
    plt.hist(listaAvalanche, bins=logbins)
    plt.xscale('log')
    plt.savefig('imagens\graficosFinais\HistSLogFreq(p=%.3f).png' %(p))
    plt.show()