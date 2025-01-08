import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class graficos: 

    def pilhaDeAreiaPerfil(deslizamento, listaAvalanche, x, h, grao, p):

        print("Pilha de Areia na estabilidade após %i deslizamentos e %i avalanches" %(deslizamento, len(listaAvalanche)))
        plt.fill_between(x,h, color ='gold')
        plt.xlabel("extensão do banco de areia")
        plt.ylabel("altura da pilha")
        plt.legend()
        plt.savefig('imagens\graficosFinais\Banco(g=%i)(p=%.3f).png' %(grao,p))
        plt.show()

    def pilhaDeAreiaPerfilComFit(self, deslizamento, listaAvalanche, x, h, grao, p):

        x_areiaFit,a,b,erra,errb = self.__fitPilhaDeAreia(x,h)

        print("Pilha de Areia na estabilidade após %i deslizamentos e %i avalanches" %(deslizamento, len(listaAvalanche)))
        #criar gráfico da pilha de areia com o fit linear
        plt.fill_between(x,h, color ='gold')
        plt.plot(x_areiaFit,self.__fitLinear(x_areiaFit,a,b), color = "green", label = "a =%.3f $\pm$ %.3f \nb =%.3f $\pm$ %.3f" %(a,erra,b,errb))
        plt.xlabel("extensão do banco de areia")
        plt.ylabel("altura da pilha")
        plt.legend(prop={'size': 15})
        plt.savefig('imagens\graficosFinais\BancoFit(g=%i)(p=%.3f).png' %(grao,p))
        plt.show()
    
    def energiaPorGrão(self, p, L, grao, graoFinal, energia):

        x_grao = np.array(range(0,graoFinal+1))
        x_grao_fit = np.array(range(10**2,graoFinal+1))
        y_fit,a,b,erra,errb = self.__fitEnergiaPorGrao(graoFinal, energia)

        print("Energia por grão de areia para p=%.2f, L=%i e %i grãos de areia" %(p,L,grao))
        plt.plot(x_grao,energia, color ='green', label = "Dados" )
        plt.plot(x_grao_fit, y_fit, color = "orange", label = "a =%.5f $\pm$ %.5f \nb =%.5f $\pm$ %.5f" %(a,erra,b,errb))
        plt.xlabel("Número de grãos na pilha")
        plt.ylabel("energia da pilha")
        plt.xscale("log")
        plt.yscale("log")
        plt.legend(prop={'size': 15})
        plt.savefig('imagens\graficosFinais\Energia(L=%i)(p=%.3f).png' %(L,p))
        plt.show()

    def normalizedAvalanchesHistogram(self, data, p):
        limites  =  []
        for n in range(16):
            limites.append(1.5**n)

        n, bins = np.histogram(data, bins=limites)

        bins_mean = [0.5 * (bins[i] + bins[i+1]) for i in range(len(n))]
        n_norm = [n[i]/(np.sum(data)*(1.5**(i+1) - 1.5**(i))) for i in range(len(n))]

        print(bins_mean)
        print(n_norm)

        for i in [-2,-1,0]:
            bins_mean.pop(i)
            n_norm.pop(i)

        print(bins_mean)
        print(n_norm)

        popt, pcov = curve_fit(self.__fitExponencial, bins_mean, n_norm)
        a,b = popt
        erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
        errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear

        plt.scatter(bins_mean, n_norm)
        plt.plot(bins_mean,self.__fitExponencial(bins_mean,a,b), color = "red", label = "a =%.2f $\pm$ %.2f \nb =%.2f $\pm$ %.2f" %(a,erra,b,errb))
        plt.xscale('log')
        plt.yscale('log')
        plt.title('Histogram for %.2f' %(p))
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.legend()
        plt.show()
    
    def __fitPilhaDeAreia(self, x, h):

        y_areiaFit = []
        x_areiaFit = []
        for i in x:
            if h[i] > 0:
                y_areiaFit.append(h[i])
                x_areiaFit.append(i)
            else:
                pass

        x_areiaFit = np.array(x_areiaFit)

        popt, pcov = curve_fit(self.__fitSand, x_areiaFit, y_areiaFit)
        a,b = popt
        erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
        errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear

        return x_areiaFit,a,b,erra,errb
    
    def __fitLinear(self, x,a,b):
        return a*x + b

    def __fitEnergiaPorGrao(self, graoFinal, energia, x_grao_fit):

        energia_fit = []
        for i in range(10**2,10**4+1):
            energia_fit.append(energia[i])

        logA = np.log(x_grao_fit) 
        logB = np.log(energia_fit)

        popt,pcov = np.polyfit(logA, logB, 1, cov=True)         # ajuste log(y) = a*log(x) + b
        a = popt[0]
        b = popt[1]
        y_fit = np.exp(a*logA + b)                              # calcula os valores ajustados de y 

        erra = np.sqrt(pcov[0,0])
        errb = np.sqrt(pcov[1,1])

        return y_fit,a,b,erra,errb
    
    def __fitExponencial(self,x,a,b):
        return np.exp(b) * x**(a)