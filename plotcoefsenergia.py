
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

slopes = [1.536,1.471,1.2,1.031,0.998,1.007,1.105,1.072,1.045,1.017,1.015,1.006,1.296]
ps = [0,0.01,0.1,0.5,0.8,1,0.2,0.3,0.4,0.6,0.7,0.9,0.05]
ps = np.array(ps)
psfit = np.linspace(0,1,100)

def fitSand(x,a,b,c):
  return b*np.exp(-a*x) + c

popt, pcov = curve_fit(fitSand, ps, slopes, p0 = (1,1e8,1))
a,b,c = popt
erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear
errc = np.sqrt(pcov[2,2])


print("Coefientes angulares dos plots de energia pela probabilidade")
plt.scatter(ps,slopes, color = "dodgerblue", label = "dados")
plt.plot(psfit,fitSand(psfit,a,b,c), color = "crimson", label = "a =%.1f $\pm$ %.1f \nb =%.2f $\pm$ %.2f \nc =%.3f $\pm$ %.3f" %(a,erra,b,errb,c,errc))
plt.grid(True)
plt.title("Coefientes angulares dos plots de energia pela probabilidade")
plt.xlabel("Probabilidade de um grão sair da pilha")
plt.ylabel("Coeficiente angular da energia por grão de areia")
plt.legend(prop={'size': 15})
plt.show()

#Diferença fracionária:
def diffrac(p,slope):
  cima = abs(slope - fitSand(p,a,b,c))
  return cima/slope

#Criando o array das diferenças:
diferenca = []
for i in range(len(slopes)):
  diferenca.append(diffrac(ps[i],slopes[i]))
diferenca = np.array(diferenca)

plt.scatter(ps,diferenca) 
plt.grid(True)
plt.title("Diferença fracionária entre a simulação e o ajuste")
plt.xlabel("Probabilidade de um grão sair da pilha")
plt.ylabel("Diferença fracionária")
plt.show()
# %%
