def atualizaSlope(z,h,i,p):
    import numpy as np
    
    P = np.random.uniform()

    if i == 0:
        z[i] -= 2
        z[i+1] += 1
        h[i] -= 1
        h[i+1] += 1
        return z, h


    else:
        if P < p:
            z[i] -= 1
            h[i] -= 1
            z[i-1] += 1
            return z, h
        
        else:
            if i == -1:
                z[i] -= 1
                z[i-1] += 1
                h[i] -= 1 
                return z, h

            else:
                z[i] -= 2
                z[i+1] += 1
                z[i-1] += 1
                h[i] -= 1
                h[i+1] += 1
                return z, h
        
    '''
    else:
        
        if i == 0:
            z[i] -= 2
            z[i+1] += 1
            h[i] -= 1
            h[i+1] += 1
        

        if i == -1:
            z[i] -= 1
            z[i-1] += 1
            h[i] -= 1 

        else:
            z[i] -= 2
            z[i+1] += 1
            z[i-1] += 1
            h[i] -= 1
            h[i+1] += 1
    
            
    return z, h
    '''