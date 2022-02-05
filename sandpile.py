#%%
"""
Este é o código central que chamará as demais funções utilizadas 

Carolina Rodrigues e Lucca Martins
"""
import numpy as np
import matplotlib.pyplot as plt
from atualiza import atualizaSlope as atualiza
from verifica import verifica

L = 100                    #tamanho máximio do banco de areia

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


z_critico = np.array(Zcritico(L))
#print(z_critico)

grao = 0
grao_final = 10000

deslizamento = 0 
p = 0

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
                z,h = atualiza(z,h,i,p)
                z_critico[i] = np.random.randint(2,4)
                deslizamento += 1
        
        if z[-1] >= z_critico[-1]:
            z, h = atualiza(z,h,-1,p)
            z_critico[-1] = np.random.randint(2,4)
            deslizamento += 1
        
        desliza = verifica(z,z_critico,L)


#print(h)
#print(deslizamento)

  
x = range(0,L)

plt.fill_between(x,h, color ='gold')
plt.grid(True)
plt.title("Pilha de Areia na estabilidade após %i deslizamentos" %(deslizamento))
plt.xlabel("extensão do banco de areia")
plt.ylabel("altura da pilha")
plt.show()

# %%
