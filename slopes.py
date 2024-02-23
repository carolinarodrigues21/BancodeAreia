from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

x = [50, 75, 100, 150, 200,300,400]
#x = [5000, 5000, 10000, 5000, 10000, 12000, 20000, 5000]
#x = [0, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
x = np.array(x)
slopes= [-1.423,-1.493,-1.538,-1.696,-1.643,-1.462,-1.643]
#slopes = []
#slopes = [-1.700, -1.683, -1.672, -1.61, -1.59, -1.58, -1.54, -1.54, -1.52, -1.50, -1.4]
slopes = np.array(slopes)
errory = [0.05,0.07,0.05,0.05,0.05,0.06,0.04]
#errory = [0.005, 0.003, 0.004, 0.003,0.002, 0.003, 0.001, 0.004]
#errory = [0.002, 0.004, 0.007, 0.01, 0.02, 0.04, 0.05, 0.04, 0.05, 0.06, 0.1]
errory = np.array(errory)

def fit(x,a,b):
    return a*x+b

popt, pcov = curve_fit(fit, x, slopes)
a,b = popt
erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear

plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'figure.figsize': [6.7,4.5]})
plt.scatter(x,slopes,color='red')
plt.plot(x,fit(x,a,b), color = "green", label = "a =%.4f $\pm$ %.4f \nb =%.2f $\pm$ %.2f" %(a,erra,b,errb))
plt.errorbar(x, slopes, yerr=errory, fmt="o")
plt.grid(True)
#plt.ylim(-1.9,-1.5)
plt.xlabel("L") #pode ser L, p ou graos
plt.ylabel("slopes (a)")
plt.legend(loc=2)
plt.savefig("Slopesp.pdf")
plt.show()
