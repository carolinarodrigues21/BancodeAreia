
import numpy as np

def atualizaSlope(z,h,i):

    if i == 0:
        z[i] -= 2
        z[i+1] += 1
        h[i] -= 1
        h[i+1] += 1

    elif i == -1:
        z[i] -= 1
        z[i-1] += 1
        h[i] -= 1 

    else:
        z[i] -= 2
        z[i+1] += 1
        z[i-1] += 1
        h[i] -= 1
        h[i+1] += 1

    return z, h