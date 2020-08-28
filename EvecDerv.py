# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:32:21 2020

@author: Personal
"""


import numpy as np
from scipy.linalg import kron, qr
def EvecDerv(A, dA, L, dL, V):
    orth = False            # orthogonalize V?
    N    = len(np.array(A)[1, :])
    dV   = np.zeros((N,N))
    I    = np.eye(N)
    
    if orth: 
        #if V is not approximately orthogonal make it orthogonal
        Q, R      = qr(V)      # Q~= V;   R~= +I or -I
        R         = np.diag(R)
        R         = kron(np.ones((N,1)),R.T)
        V         = Q.T@R      # Fix sign of orthogonalized V to match original
    
    #if max(max(V.conj().T @V-I)) > (N^2)*1e-4:
    #    print('Warning: In EvecDerv() max(V-I)=%8.6f\n',max(max(V.conj().T @ V-I)));
                                        
               
    # NON-REPEATING EIGENVALUES METHOD-2 (PSEUDOINVERSE)
    for k in range(N):      
        lamda   = L[k]
        dlamda  = dL[k]
        v       = V[:,k]
        f       = (dlamda*I - dA) @ v 
        B       = A - (lamda * I)
        x       = np.linalg.pinv(B) @ f
        alpha   = v.conj().T @ x
        dv      = x + alpha * v
        dV[:,k]   = dv
      
    return dV