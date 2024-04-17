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
totalDeGraos = 10000

#valores da constante de probabilidade (p)
probabilidades = [0.01, 0.1, 0.2, 0.5, 0.8, 0.9]

#informações para o gráfico
legendaGrafico = []
formatoScatter = ["o","p","v","*","^","s"]

for i in range(len(probabilidades)):
    listaAvalanche = pilhaDeAreia(L, totalDeGraos, probabilidades[i])
    legendaGrafico.append("p = " + str(probabilidades[i]))

    maiorAvalanche = np.max(listaAvalanche)
    valoresDeAvalanche = range(0,int(maiorAvalanche)+1)

    frequenciasDeAvalanches = []
    contador = 0

    for c in valoresDeAvalanche:
        for j in range(len(listaAvalanche)):
            if listaAvalanche[j] == c:
                contador += 1
        frequenciasDeAvalanches.append(contador)
        contador = 0

    plt.scatter(valoresDeAvalanche,frequenciasDeAvalanches, marker=formatoScatter[i])

plt.xscale('log')
plt.yscale('log')
plt.legend(legendaGrafico)
plt.xlim((0.8,500))
plt.ylim((0.8,np.max(np.array(frequenciasDeAvalanches))+1000))
plt.xlabel("Tamanho da Avalanche (Energia)")
plt.ylabel("Frequência Normalizada")
plt.show()
    