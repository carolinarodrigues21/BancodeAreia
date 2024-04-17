"""
Este é o código central para a produção da pilha, obtenção das avalanches e energias da 

autores: Carolina Rodrigues e Lucca Martins
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from atualiza import atualizaSlope as atualiza
from verifica import *
from avalanches import *

def pilhaDeAreia(L:int, grao_final:int, p:float):

    #deltaH crítico entre as células da pilha 
    z_critico = np.array(Zcritico(L))

    #contagem de deslizamentos no sistema
    deslizamento = 0 

    #altura de cada parte da pilha 
    h = np.zeros(L)

    #deltaH entre as células da pilha 
    z = np.zeros(L)

    #contagem de grãos no sistema
    grao = 0

    energia = np.zeros(grao_final+1)

    #valor da energia no início do sistema
    energia[0] = 0

    magnitudeAvalanche = np.zeros(grao_final+1)

    #valor da avalanche no início do sistema
    magnitudeAvalanche[0]= 0 

    while grao < grao_final:
        grao += 1               #mais um grão na pilha
        h[0] += 1               #aumenta a altura da primeira casa [0]
        z[0] += 1               #aumenta a diferença de altura da posição 0 com a 1
        e = 0                   #valor da energia
        MagAv = 0               #valor da magnitude da avalanche


        #verifica se ocorre deslizamento 
        desliza, avalanche = verifica(z,z_critico,L)

        #se ocorre desliazamento:
        while desliza == True:
            for i in range(0,L-1):
                z[i] =  h[i] - h[i+1]                           #diferença de altura da casa a partir das alturas
                if z[i] >= z_critico[i]: 
                    z, h, e = atualiza(z,h,i,p,e)               #altera a configuração da pilha com após deslizamento
                    z_critico[i] = np.random.randint(2,4)       #recalcula o z_critico depois de um deslizamento 
                    deslizamento += 1                           #contador do número de deslizamentos
            
            if z[-1] >= z_critico[-1]:                          # verifica para o final da pilha
                z, h, e = atualiza(z,h,-1,p,e)
                z_critico[-1] = np.random.randint(2,4)
                deslizamento += 1                               
            
            desliza,avalanche = verifica(z,z_critico,L)         #verifica de novo se houve deslizamento para sair ou não do loop
            MagAv += avalanche
            
        energia[grao] = energia[grao-1] + e                     #calcula a energia do estado atual acumulando ao anterior
        magnitudeAvalanche[grao] = MagAv                        #calcula a magnitude das avalanches pela entrada do grão


    #ajustar os dados da pilha de areia
    x = range(0,L)

    y_areiaFit = []
    x_areiaFit = []
    for i in x:
        if h[i] > 0:
            y_areiaFit.append(h[i])
            x_areiaFit.append(i)
        else:
            pass

    x_areiaFit = np.array(x_areiaFit)

    popt, pcov = curve_fit(fitSand, x_areiaFit, y_areiaFit)
    a,b = popt
    erra = np.sqrt(pcov[0,0])        #erro do coeficiente angular
    errb = np.sqrt(pcov[1,1])        #erro do coeficiente linear

    listaAvalanche = []
    for i in range(0,len(magnitudeAvalanche)):
        if magnitudeAvalanche[i] != 0:
            listaAvalanche.append(magnitudeAvalanche[i])

    # print("Pilha de Areia na estabilidade após %i deslizamentos e %i avalanches" %(deslizamento, len(listaAvalanche)))
    # plt.fill_between(x,h, color ='gold')
    # plt.xlabel("extensão do banco de areia")
    # plt.ylabel("altura da pilha")
    # plt.legend()
    # plt.savefig('imagens\graficosFinais\Banco(g=%i)(p=%.3f).png' %(grao,p))
    # plt.show()

    # print("Pilha de Areia na estabilidade após %i deslizamentos e %i avalanches" %(deslizamento, len(listaAvalanche)))
    # #criar gráfico da pilha de areia com o fit linear
    # plt.fill_between(x,h, color ='gold')
    # plt.plot(x_areiaFit,fitSand(x_areiaFit,a,b), color = "green", label = "a =%.3f $\pm$ %.3f \nb =%.3f $\pm$ %.3f" %(a,erra,b,errb))
    # plt.xlabel("extensão do banco de areia")
    # plt.ylabel("altura da pilha")
    # plt.legend(prop={'size': 15})
    # plt.savefig('imagens\graficosFinais\BancoFit(g=%i)(p=%.3f).png' %(grao,p))
    # plt.show()

    # x_grao = np.array(range(0,grao_final+1))
    # x_grao_fit = np.array(range(10**2,grao_final+1))

    # energia_fit = []
    # for i in range(10**2,10**4+1):
    #     energia_fit.append(energia[i])


    # logA = np.log(x_grao_fit) 
    # logB = np.log(energia_fit)

    # popt,pcov = np.polyfit(logA, logB, 1, cov=True)         # ajuste log(y) = m*log(x) + c
    # m = popt[0]
    # c = popt[1]
    # y_fit = np.exp(m*logA + c)                              # calcula os valores ajustados de y 

    # errm = np.sqrt(pcov[0,0])
    # errc = np.sqrt(pcov[1,1])


    # print("Energia por grão de areia para p=%.2f, L=%i e %i grãos de areia" %(p,L,grao))
    # #criar gráfico da relação da energia por grão de areia no sistema
    # plt.plot(x_grao,energia, color ='green', label = "Dados" )
    # plt.plot(x_grao_fit, y_fit, color = "orange", label = "a =%.5f $\pm$ %.5f \nb =%.5f $\pm$ %.5f" %(m,errm,c,errc))
    # plt.xlabel("Número de grãos na pilha")
    # plt.ylabel("energia da pilha")
    # plt.xscale("log")
    # plt.yscale("log")
    # plt.legend(prop={'size': 15})
    # plt.savefig('imagens\graficosFinais\Energia(L=%i)(p=%.3f).png' %(L,p))
    # plt.show()

    # AvalanchePorP_semiLogHist(listaAvalanche, p, L)

    return listaAvalanche

def Zcritico(L:int):
        z_critico = []
        while len(z_critico) < L:
            z_critico.append(np.random.randint(2,4))
        return z_critico

def fitSand(x,a,b):
    return a*x + b  