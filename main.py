"""
Este é o código central para a produção da pilha, obtenção das avalanches e energias da 

autores: Carolina Niklaus e Lucca Martins
"""

import numpy as np
import matplotlib.pyplot as plt
from sandpile import pilhaDeAreia

#tamanho máximo do banco de areiass
L = 100               

#número total de grãos colocados no sistema
grao_final = 10000

#valores da constante p
valoresDeP = [0.1, 0.5]

for i in range(len(valoresDeP)):
    listaAvalanche = pilhaDeAreia(L, grao_final, valoresDeP[i])

    maiorzao = np.max(listaAvalanche)
    valoresDeAvalanche = range(0,int(maiorzao)+1)

    frequencias = []
    contador = 0

    for c in valoresDeAvalanche:
        for j in range(len(listaAvalanche)):
            if listaAvalanche[j] == c:
                contador += 1
        frequencias.append(contador)
        contador = 0

    print(frequencias)
    plt.scatter(valoresDeAvalanche,frequencias)

plt.xscale('log')
plt.yscale('log')
plt.xlim((0.8,maiorzao+1))
plt.ylim((0.8,np.max(np.array(frequencias))+1000))
plt.xlabel("Tamanho da Avalanche (Energia)")
plt.ylabel("Frequência Normalizada")
plt.show()
    