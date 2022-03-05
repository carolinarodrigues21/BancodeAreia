'''
Verifica se ocorre deslizamento

'''

import numpy as np 

def verifica(z,zc,L):
    contadorDes = 0 
    avalanche = []
    
    for i in range(0,L):
        if z[i]>= zc[i]:
            contadorDes += 1
            avalanche.append(1)
        else: 
            contadorDes += 0
            avalanche.append(0)
    
    contadorAva = 0
    #print(avalanche)
    for j in range(0,len(avalanche)-1):
        if avalanche[j]==1 and avalanche[j] == avalanche[j+1] :
            #print("entrei")
            contadorAva += 1
            #print(contadorAva)
    
    #print(contadorAva)
    
    if contadorDes != 0:
        return True, contadorAva
    else:
        return False, contadorAva

'''
def verificaAvalanche(z,zc,L):

    avalanche = 0 #define o contador
    for i in range(0,L): #vai loopar em todo o array
        if z[i] >= zc[i] and z[i+1] + 1 >= zc[i+1]: #se houver avalanche nessa posição, vai rodar
            avalanche += 1 
    
    return avalanche
'''
    
