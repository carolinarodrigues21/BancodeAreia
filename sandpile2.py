"""
Este é o código central para a produção da pilha, obtenção das avalanches e energias

autores: Carolina Rodrigues e Lucca Martins
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from atualiza2 import atualizaPilha
from verifica2 import verificaDeslizamento
from avalanches import *
from graficos import graficos

class sandpile: 

    def pilhaDeAreia(self, L:int, graoFinal:int, p:float):

        #deltaH crítico entre as células da pilha 
        z_critico = np.array(self.__criticalZ(L))

        #contagem de deslizamentos no sistema
        deslizamento = 0

        #altura de cada parte da pilha 
        h = np.zeros(L)

        #deltaH entre as células da pilha 
        z = np.zeros(L)

        #contagem de grãos no sistema
        grao = 0

        energia = np.zeros(graoFinal+1)

        #valor da energia no início do sistema
        energia[0] = 0

        magnitudeAvalanche = np.zeros(graoFinal+1)

        #valor da avalanche no início do sistema
        magnitudeAvalanche[0]= 0

        while grao < graoFinal:
            grao += 1               #mais um grão na pilha
            h[0] += 1               #aumenta a altura da primeira casa [0]
            z[0] += 1               #aumenta a diferença de altura da posição 0 com a 1
            e = 0                   #valor da energia
            MagAv = 0               #valor da magnitude da avalanche

            #verifica se ocorre deslizamento
            desliza, avalanche = verificaDeslizamento.verifica(z,z_critico,L)

            #se ocorre desliazamento:
            while desliza == True:
                for i in range(0,L-1):
                    z[i] =  h[i] - h[i+1]                           #diferença de altura da casa a partir das alturas
                    if z[i] >= z_critico[i]: 
                        z, h, e = atualizaPilha.atualiza(z,h,i,p,e)               #altera a configuração da pilha com após deslizamento
                        z_critico[i] = np.random.randint(2,4)       #recalcula o z_critico depois de um deslizamento 
                        deslizamento += 1                           #contador do número de deslizamentos
                
                if z[-1] >= z_critico[-1]:                          # verifica para o final da pilha
                    z, h, e = atualizaPilha.atualiza(z,h,-1,p,e)
                    z_critico[-1] = np.random.randint(2,4)
                    deslizamento += 1                               
                
                desliza,avalanche = verificaDeslizamento.verifica(z,z_critico,L)       #verifica de novo se houve deslizamento para sair ou não do loop
                MagAv += avalanche
                
            energia[grao] = energia[grao-1] + e                     #calcula a energia do estado atual acumulando ao anterior
            magnitudeAvalanche[grao] = MagAv                        #calcula a magnitude das avalanches pela entrada do grão

        #ajustar os dados da pilha de areia
        x = range(0,L)

        listaAvalanche = []
        for i in range(0,len(magnitudeAvalanche)):
            if magnitudeAvalanche[i] != 0:
                listaAvalanche.append(magnitudeAvalanche[i])

        graficos.pilhaDeAreiaPerfilComFit(deslizamento, listaAvalanche, x, h, grao, p)

        graficos.energiaPorGrão(p,L,grao,graoFinal,energia)

        return listaAvalanche

    def __criticalZ(self, L:int):
            z_critico = []
            while len(z_critico) < L:
                z_critico.append(np.random.randint(2,4))
            return z_critico


    def verifica(self,z,zc,L):
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
        for j in range(0,len(avalanche)-1):
            if avalanche[j]==1 and avalanche[j] == avalanche[j+1] :
                contadorAva += 1
        
        if contadorDes != 0:
            return True, contadorAva
        else:
            return False, contadorAva