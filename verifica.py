import numpy as np 

def verifica(z,zc,L):

    contador = 0 
    for i in range(0,L):
        if z[i]>= zc[i]:
            contador += 1
        else: 
            contador += 0
    
    if contador != 0:
        return True 
    else:
        return False
