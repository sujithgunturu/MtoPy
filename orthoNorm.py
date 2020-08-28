# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:54:24 2020

@author: Personal
"""
import numpy as np

def orthoNNorm(Vr):
    N      = len(Vr[:, 0])
    for k in range(N):
        v   = Vr[:,k]
        Vr[:,k]     = v/np.linalg.norm(v)
    I       = np.eye(N)
    D       = Vr.conj().T @ Vr - I
    D2      = D.conj().T @ D
    V       = Vr @ (I - 0.5*D + 0.375*D2)
    return V
        
        
