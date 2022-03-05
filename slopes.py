from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

#x = [80, 100, 100, 200,200,200,200,400]
#x = [5000, 5000, 10000, 5000, 10000, 12000, 20000, 5000]
x = [0, 0.01, 0.1, 0.5, 0.8]
x = np.array(x)
#slopes = [-1.755, -1.687, -1.698, -1.682,-1.682, -1.682, -1.701, -1.710 ]
slopes = [-1.723, -1.712, -1.709, -1.42, -1.21]
slopes = np.array(slopes)
#errory = [0.005, 0.003, 0.004, 0.003,0.002, 0.003, 0.001, 0.004]
errory = [0.002, 0.003, 0.009, 0.06,0.06]
errory = np.array(errory)

def fit(x,a,b):
    return a*x+b

popt, pcov = curve_fit(fit, x, slopes)
a,b = popt
erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear

plt.scatter(x,slopes,color='red')
plt.plot(x,fit(x,a,b), color = "green", label = "a =%.3f $\pm$ %.3f \nb =%.3f $\pm$ %.3f" %(a,erra,b,errb))
plt.errorbar(x, slopes, yerr=errory, fmt="o")
plt.grid(True)
#plt.ylim(-1.9,-1.5)
plt.xlabel("p")
plt.ylabel("slopes (a)")
plt.legend()
plt.savefig("Slopesp.pdf")
plt.show()