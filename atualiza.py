def atualizaSlope(z,h,i,p,e):
    import numpy as np
    
    P = np.random.uniform()


    if i == 0:
        z[i] -= 2
        z[i+1] += 1
        h[i] -= 1
        h[i+1] += 1
        e += z[i] + 1
        return z, h, e


    else:
        if P < p:
            z[i] -= 1
            h[i] -= 1
            z[i-1] += 1
            return z, h, e
        
        else:
            if i == -1:
                z[i] -= 1
                z[i-1] += 1
                h[i] -= 1 
                return z, h, e

            else:
                z[i] -= 2
                z[i+1] += 1
                z[i-1] += 1
                h[i] -= 1
                h[i+1] += 1
                e += z[i] + 1
                return z, h, e
        
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