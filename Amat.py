# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:15:20 2020

@author: Personal
"""

import numpy as np
from Rot3 import *

def Amat(t, params):
    N      = params['N']
    TMAX   = params["TMAX"]
    # OBTAIN NxN ROTATION MATRIX 'Q' AND ITS DERIVATIVE 'dQ'
    alpha0  = params["alpha0"]
    alpha1 = params["alpha1"]
    beta0   = params["beta0"] 
    beta1  = params["beta1"]
    gamma0  = params["gamma0"]
    gamma1 = params["gamma1"]
    alpha   = alpha0 + (t/TMAX)*(alpha1 - alpha0)
    beta    = beta0  + (t/TMAX)*(beta1  - beta0 )
    gamma   = gamma0 + (t/TMAX)*(gamma1 - gamma0)
    Q, dQ = rotMat(alpha, beta, gamma, N)
    # OBTAIN NxN SPD MATRIX 'B' AND ITS DERIVATIVE 'dB'
    # At time t=TMAX/2 make sure that 3 eigenvalues of B will be equal!
    B0      = np.array(params["B0"])
    B1      =  np.array(params["B1"]) 
    dB      =  np.array(params["dB"]) 
    B       = B0 + (t/TMAX)*(B1-B0)

    # OBTAIN NxN SIMILARITY TRANSFORM 'A' AND ITS DERVATIVE 'dA'
    # At time t=TMAX/2 make sure that 3 eigenvalues of A will be equal!
    A       = Q.conj().T @ B @ Q
    dA      = (dQ.conj().T @ B @ Q) + (Q.conj().T @ B @ dQ) +  ((Q.conj().T @ dB @ Q) )


    return A, dA
   
def rotMat(alpha, beta, gamma, N):
    Q = np.eye(N,N) 
    dQ = np.zeros((N,N))
    
    Rx, Ry, Rz, dRx, dRy, dRz = rot3(alpha, beta, gamma)

    Q[0:3,0:3] = Rx@Ry@Rz
    dQ[0:3,0:3] = dRx@Ry@Rz + Rx@dRy@Rz + Rx@Ry@dRz
    return Q, dQ

