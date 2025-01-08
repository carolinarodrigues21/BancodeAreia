import numpy as np
import matplotlib.pyplot as plt
from sandpile2 import sandpile
from histograms import *

#tamanho máximo do banco de areiass
L = 100               

#número total de grãos colocados no sistema
totalDeGraos = 10000

#valores da constante de probabilidade (p)
# probabilidades = [0.01, 0.1, 0.2, 0.5, 0.8, 0.9]
probabilidades = [0.01]

#informações para o gráfico
legendaGrafico = []

class runSandpileSimulation: 
    
    def run(self):
        self.__getSandpileProfileAndFit()
        print('hello')

    def __getSandpileProfileAndFit(self, L:int, totalDeGraos:int, probabilidades:float):
        global listaAvalanche #global variable
        listaAvalanche = sandpile.pilhaDeAreia(L, totalDeGraos, probabilidades)


simulation = runSandpileSimulation()
simulation.run()
