#%%
"""
Este é o código central que chamará as demais funções utilizadas 

Carolina Rodrigues e Lucca Martins
"""
import numpy as np
import matplotlib.pyplot as plt
from atualiza import atualizaSlope as atualiza
from verifica import verifica

L = 10                     #tamanho máximio do banco de areia


#altura de cada parte da pilha 
h = np.zeros(L)   

#deltaH entre as células da pilha 
z = np.zeros(L)

#slopes críticos 

def Zcritico(L):
    z_critico = []
    while len(z_critico) < L:
        z_critico.append(np.random.randint(2,4))
    return z_critico

#z_critico = np.array(np.random.randint(2,3) in range(L)) #o artigo diz de 1 a 2, mas a gente não concorda (?)

z_critico = np.array(Zcritico(L))
print(z_critico)
grao = 0
grao_final = 20

while grao < grao_final:
    grao += 1
    h[0] += 1
    z[0] += 1

    #print(z)
    #print(z_critico)

    desliza = verifica(z,z_critico,L)

    while desliza == True:
        for i in range(0,L-1):
            z[i] =  h[i] - h[i+1]
            if z[i] >= z_critico[i]: 
                z,h = atualiza(z,h,i)
                z_critico[i] = np.random.randint(2,3)
        
        if z[-1] >= z_critico[-1]:
            z, h = atualiza(z,h,-1)
            z_critico[-1] = np.random.randint(2,3)
        
        desliza = verifica(z,z_critico,L)



print(h)
    
# %%
