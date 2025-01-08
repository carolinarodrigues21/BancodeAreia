'''
Verifica se ocorre deslizamento

'''

class verificaDeslizamento:

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
    
