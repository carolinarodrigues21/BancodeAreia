#%%
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

slopes = [1.536,1.471,1.2,1.031,0.998,1.007]
ps = [0,0.01,0.1,0.5,0.8,1]
ps = np.array(ps)
psfit = np.linspace(0,1,100)

def fitSand(x,a,b,c):
  return b*np.exp(-a*x) + c

popt, pcov = curve_fit(fitSand, ps, slopes, p0 = (1,1e8,1))
a,b,c = popt
erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear
errc = np.sqrt(pcov[2,2])


plt.scatter(ps,slopes, color = "dodgerblue", label = "dados")
plt.plot(psfit,fitSand(psfit,a,b,c), color = "crimson", label = "a =%.3f $\pm$ %.3f \nb =%.3f $\pm$ %.3f \nc =%.3f $\pm$ %.3f" %(a,erra,b,errb,c,errc))
plt.grid(True)
plt.title("Coefientes angulares dos plots de energia pela probabilidade")
plt.xlabel("Probabilidade de um grão sair da pilha")
plt.ylabel("Coeficiente angular da energia por grão de areia")
plt.legend()
plt.show()
# %%
