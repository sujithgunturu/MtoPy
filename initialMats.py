# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:54:30 2020

@author: Personal
"""
from math import * 
import numpy as np 
np.random.seed(1)

def spdMats(N):
    B = np.random.random((N,N))
    #B =  np.random.rand(N, N)
    #B = np.random.uniform(low=0.5, high=1.5, size=(N,N))
    B =  B.conj().T @ B
    D, V = np.linalg.eig(B)
    D[-1] = D[-2]
    D[-3] = D[-2]
    D = np.diag(D)
    B = V @ D @ V.conj().T 
    C = np.random.random((N,N))
    #C = np.random.rand(N, N)
    #C = np.random.uniform(low=0.5, high=1.5, size=(N,N))
    C = 0.5 * (C.T @ C)
    B0 = B-C
    B1 = B+C
    return B0, B1

def initialMats(TMAX,delt,N):
    B0, B1 = spdMats(N)
    dB = (B1 - B0)/TMAX
    alpha0 = pi/7;  beta0 = -pi/3;   gamma0 = -pi/6;
    alpha1 = 0;     beta1 = pi/3;  gamma1 = pi/10;
    dalpha = (alpha1 - alpha0)/TMAX
    dbeta  = (beta1 - beta0)/TMAX
    dgamma = (gamma1 - gamma0)/TMAX
    
    params = {'N':N,'TMAX':TMAX,'delt':delt, 'B0': B0,'B1': B1,'dB': dB,
            'alpha0': alpha0,'beta0': beta0,'gamma0': gamma0,                 
            'alpha1': alpha1,'beta1': beta0,'gamma1': gamma1,
            'dalpha': dalpha,'dbeta': dbeta,'dgamma': dgamma}
    return params
