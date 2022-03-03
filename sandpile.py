#%%
"""
Este é o código central que chamará as demais funções utilizadas 

Carolina Rodrigues e Lucca Martins
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from atualiza import atualizaSlope as atualiza
from verifica import *

L = 100                    #tamanho máximo do banco de areia

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
p = 1

energia = np.zeros(grao_final+1)
energia[0] = 0

while grao < grao_final:
    grao += 1 #mais um grão na pilha
    h[0] += 1 #aumenta a altura da primeira casa [0]
    z[0] += 1 #aumenta a diferença de altura da posição 0 com a 1
    e = 0

    #print(z)
    #print(z_critico)

    #verifica se ocorre deslizamento 
    desliza, avalanche = verifica(z,z_critico,L) 

    #se ocorre desliazamento:
    while desliza == True:
        for i in range(0,L-1):
            z[i] =  h[i] - h[i+1]                       #diferença de altura da casa a partir das alturas
            if z[i] >= z_critico[i]: 
                z, h, e = atualiza(z,h,i,p,e)                 #altera a configuração da pilha com após deslizamento
                z_critico[i] = np.random.randint(2,4)   #recalcula o z_critico depois de um deslizamento 
                deslizamento += 1 #contador do número de deslizamentos
        
        if z[-1] >= z_critico[-1]:
            z, h, e = atualiza(z,h,-1,p,e)
            z_critico[-1] = np.random.randint(2,4)
            deslizamento += 1   #contador do número de deslizamentos
        
        desliza,avalanche = verifica(z,z_critico,L) #verifica de novo se houve deslizamento para sair ou não do loop
    #print(e)
    energia[grao] = energia[grao-1] + e


#print(h)
#print(deslizamento)
#print(energia)

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

def fitSand(x,a,b):
  return a*x + b  

popt, pcov = curve_fit(fitSand, x_areiaFit, y_areiaFit)
a,b = popt
erra = pcov[0,0]
errb = pcov[1,1]


#a = -1.676     b= 128.644 (L= 80, graos = 5*10^3)

#a = -1.746     b= 175.209 (L = 100, graos = 10^4)
#a = -1.672     b= 128.482 (L= 100, graos = 5*10^3)

#a = -1.684     b= 182.702 (L= 200, graos = 10^4)
#a = -1.635     b= 127.044 (L= 200, graos = 5*10^3)
#a = -1.677     b= 199.793 (L= 200, graos = 12*10^3)
#a = -1.733     b= 262.403 (L= 200, graos = 2*10^4)

#a = -1.671     b= 128.429 (L= 400, graos = 5*10^3)


plt.fill_between(x,h, color ='gold')
plt.plot(x_areiaFit,fitSand(x_areiaFit,a,b), color = "green", label = "a =%.3f $\pm$ %.3f \nb =%.3f $\pm$ %.3f" %(a,erra,b,errb))
plt.grid(True)
plt.title("Pilha de Areia na estabilidade após %i deslizamentos e %i avalanches" %(deslizamento, avalanche))
plt.xlabel("extensão do banco de areia")
plt.ylabel("altura da pilha")
plt.legend()
#plt.savefig('imagens\Banco(g=%i)(p=%.3f).png' %(grao,p))
plt.show()

x_grao = np.array(range(0,grao_final+1))

def fitEnerg(x,A,B):
  return A*np.exp(x*B)

popt, pcov = curve_fit(fitEnerg, x_grao, energia)
A,B= popt
errA = pcov[0,0]
errB = pcov[1,1]

plt.plot(x_grao,energia, color ='green', label = "Dados" )
#plt.plot(x_grao, fitEnerg(x_grao,A,B), color = "orange", label = "a =%.3f $\pm$ %.3f \nb =%.3f $\pm$ %.3f" %(A,errA,B,errB))
plt.grid(True)
plt.title("Energia por grão de areia para p=%.2f, L=%i e %i grãos de areia" %(p,L,grao))
plt.xlabel("Número de grãos na pilha")
plt.ylabel("energia da pilha")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.savefig('imagens\graficos_energiaXgrao\Gráfico(L=%i)(p=%.3f).png' %(L,p))
plt.show()

'''
a = [-1.676, -1.746, -1.672, -1.684, -1.635, -1.677, -1.733, -1.671]
print("média de slope é ",np.mean(a))
print("o desvio padrão do slope é ",np.std(a))
'''
# %%
