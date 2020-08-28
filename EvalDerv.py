# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:24:45 2020

@author: Personal
"""
import numpy as np

def EvalDerv(V, dA):
    # Finds derivative of all eigenvalues
    # INPUTS:
    # V   : NxN matrix whose columns are eigenvectors of A(t)
    # dA  : NxN derivative of matrix A(t)
    # OUTPUT:     
    # dL  : Nx1 eigenvectors of A(t)
    N = len(np.array(V)[:, 1])
    dL = np.zeros((N,1))
    for k in range(N):
        v = V[:,k]     # kth eigenvectordL(k) = v'*dA*v;
        dL[k] = v.T @ dA @ v
    return dL

