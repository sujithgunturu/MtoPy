# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:24:03 2020

@author: Personal
"""

import numpy as np
Inf = float("inf")

def matchPts(X, Y, flip = True):
    
    d, N = X.shape
    Z      = np.zeros((d,N))
    D      = Inf*np.ones((N,N))
    Dn     = D
    for j in range(N):
        x = X[:,j]
        for k in range(N):
            y       = Y[:,k]
            D[j,k]  = np.linalg.norm(x-y)
            if flip:
                Dn[j,k] = np.linalg.norm(x+y)
    
    sig = 1
    for j in range(N):
        #[r, c]  = find(D==min(D(:)))
        r, c = np.where(D == np.min(D))
        #r       = r[1]                  # make unique
        #c       = c(1)                  # make unique
        val     = D[r,c]
        sig     = 1                    #% sign (+ or -)
        if flip:
            rn, cn = np.where(D == np.min(D))
            #rn       = rn[1]
            #cn       = cn[1]
            valn     = Dn[rn, cn]
            if valn < val:
                r       = rn
                c       = cn
                sig     = -1
            else:
                sig     = 1
        Z[:,c]      = sig*X[:,r]
        D[r, :]     = Inf
        D[:, c]     = Inf
        if flip:
            Dn[r, :]    = Inf
            Dn[:, c]    = Inf
    return Z     
        
   
            
            
        
                         
    

        
    