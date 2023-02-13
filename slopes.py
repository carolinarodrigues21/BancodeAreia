from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

#a = -1.676     b= 128.644 (L= 80, graos = 5*10^3)

#a = -1.746     b= 175.209 (L = 100, graos = 10^4)
#a = -1.672     b= 128.482 (L= 100, graos = 5*10^3)

#a = -1.684     b= 182.702 (L= 200, graos = 10^4)
#a = -1.635     b= 127.044 (L= 200, graos = 5*10^3)
#a = -1.677     b= 199.793 (L= 200, graos = 12*10^3)
#a = -1.733     b= 262.403 (L= 200, graos = 2*10^4)

#a = -1.671     b= 128.429 (L= 400, graos = 5*10^3)

x_L = [80, 100, 100, 200,200,200,200,400]
x_grãos = [5000, 5000, 10000, 5000, 10000, 12000, 20000, 5000]
x_p = np.arange(0,1,0.1)

slopes_Lg = [-1.755, -1.687, -1.698, -1.682,-1.682, -1.682, -1.701, -1.710 ]
slopes = [-1.723, -1.712, -1.709, -1.42, -1.21]
s_p = [-1.723, -1.709,-1.557,-1.605,-1.676,-1.654,-1.376,-1.595,-1.357,-1.371]

errory_Lg =  [0.005, 0.003, 0.004, 0.003,0.002, 0.003, 0.001, 0.004]
# errory = [0.002, 0.003, 0.009, 0.06,0.06]
errory_p = [0.002, 0.009, 0.02, 0.03, 0.02, 0.06, 0.05, 0.07, 0.10, 0.06]



def slope_graph(x,y, erry, save_path:str, x_label:str, y_lim:bool):

    def fit(x,a,b):
        return a*x+b

    x = np.array(x)
    slopes = np.array(y)
    errory = np.array(erry)

    popt, pcov = curve_fit(fit, x, slopes)
    a,b = popt
    erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
    errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear

    plt.scatter(x,slopes,color='red')
    plt.plot(x,fit(x,a,b), color = "green", label = "a =%.6f $\pm$ %.6f \nb =%.3f $\pm$ %.3f" %(a,erra,b,errb))
    plt.errorbar(x, slopes, yerr=errory, fmt="o")
    plt.grid(True)
    if y_lim == True:
        plt.ylim(-1.9,-1.5)
    plt.xlabel(x_label)
    plt.ylabel("slopes (a)")
    plt.legend()
    plt.savefig(save_path)
    return plt.show()

para_P = slope_graph(x_p,s_p, errory_p,'Slopep.pdf', 'p', True)
para_L = slope_graph(x_L,slopes_Lg,errory_Lg, 'SlopeL.pdf', 'L', True)
para_L = slope_graph(x_grãos,slopes_Lg,errory_Lg, 'Slopeg.pdf', 'grãos', True)