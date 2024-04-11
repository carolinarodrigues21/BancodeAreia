import matplotlib.pyplot as plt
import math as mt
import numpy as np

# def avalancheVariaBin(listaAvalanche):
#     bins = [5,10, 15, 30, 50, 75, 100]

#     for i in bins:
#         plt.hist(listaAvalanche,bins = i,ec = "k", density = True)

#         plt.xlabel("Tamanho da Avalanche (Energia)")
#         plt.ylabel("Frequência Normalizada")
#         plt.savefig('imagens\graficosFinais\FreqAvaEne(L=%i)(p=%.3f)(bins=%i).png' %(L,p,i))
#         return plt.show()

def AvalanchePorPLogLog(listaAvalanche, p, L):

    print('estou aqui na certa!!!!')
    maiorzao = np.max(listaAvalanche)
    valoresDeAvalanche = range(0,int(maiorzao)+1)

    frequencias = []
    contador = 0

    for c in valoresDeAvalanche:
        for i in range(len(listaAvalanche)):
            if listaAvalanche[i] == c:
                contador += 1
        frequencias.append(contador)
        contador = 0

    print(frequencias)
    plt.scatter(valoresDeAvalanche,frequencias)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim((0.8,maiorzao+1))
    plt.ylim((0.8,np.max(np.array(frequencias))+1000))
    plt.xlabel("Tamanho da Avalanche (Energia)")
    plt.ylabel("Frequência Normalizada")
    return plt.show()

# def AvalanchePorP(listaAvalanche, p, L):

#     bin = mt.sqrt(len(listaAvalanche))

#     plt.hist(listaAvalanche,bins = int(bin),ec = "k", density = True, label = 'bins=%i' %(bin))
#     plt.xlabel("Tamanho da Avalanche (Energia)")
#     plt.ylabel("Frequência Normalizada")
#     plt.legend(prop={'size': 15})
#     plt.savefig('imagens\graficosFinais\FreqAvaEne(L=%i)(p=%.3f).png' %(L,p))
#     return plt.show()


# def AvalanchePorP_semiLogHist(listaAvalanche, p, L):

#     bin = mt.sqrt(len(listaAvalanche))
#     hist, bins = np.histogram(listaAvalanche, bins=int(bin))
#     logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
#     plt.hist(listaAvalanche, bins=logbins, ec = "k", density = True, label = 'bins=%i' %(bin))
#     plt.xscale('log')
#     plt.xlabel("Tamanho da Avalanche (Energia)")
#     plt.ylabel("Frequência")
#     plt.legend(prop={'size': 15})
#     plt.savefig('imagens\graficosFinais\HistSLogFreqAvaEne(p=%.3f).png' %(p))
#     plt.show()