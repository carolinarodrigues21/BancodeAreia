import numpy as np 

def f(epsilon,L,c,ni,b):

    g = c*epsilon*L**(-ni)

    return L**(-b)*g