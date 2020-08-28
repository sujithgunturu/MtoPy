import numpy as np 
from initialMats import *
from Amat import * 
from EvalDerv import *
from EvecDerv import * 
from matchPts import *
import numpy as np
from orthoNorm import *
from scipy import io

dAt = io.loadmat('dA.mat')
dLt = io.loadmat('dl.mat')
dVt = io.loadmat('dV.mat')
A0t  = io.loadmat('A0.mat')
dA0t = io.loadmat('dA0.mat')
Vt =   io.loadmat('V.mat')
B0t = io.loadmat('B0.mat')
B1t = io.loadmat('B1.mat')
dBt = io.loadmat('dB.mat')
AdA = dAt["dArray"][0]
AdL = dLt["dLArray"][0]
AdV = dVt["dVArray"][0]
AA0 = A0t["A"]
AdA0 = dA0t["dA"]
AV = Vt["VArray"][0]
AB0 = B0t['a']
AB1 = B1t['b']
AdB = dBt['c']


np.random.seed(1)
delt = 2e-6
TMAX = 1e-3
N = 6

params = initialMats(TMAX,delt, N)
params["B0"] = AB0
params["B1"] = AB1
params["dB"] = AdB

# Initialization
iter    = 0
t       = 0
A, dA = Amat(t, params)
dA = AdA0
A = AA0
L, V  = np.linalg.eig(A)
L  = L.reshape(N,1) 

Vtrue   = V
EVerrs  = np.zeros((N,floor(TMAX/delt)))
ELerrs  = np.zeros((1,floor(TMAX/delt)))
while t <= TMAX:
    # Derivative of A(t), L(t), 
    _ , dA =  Amat(t, params)
    dL      = EvalDerv(V, dA)
    dL = AdL[iter]
    dV      = EvecDerv(A, dA, L, dL, V)
    dV = AdV[iter]
    # Increments

    t       = t + delt;
    A       = A + delt*(dA)
    L       = L + delt*dL
    V       = V + delt*dV
    
    

    # Normalize eigenvectors
    V       = orthoNNorm(V);
    
    #for k in range(N):
    #    v = V[:,k]
    #    V[:, k] = V[:, k]/ np.linalg.norm(v)
    
    # True eigenvalues & eigenvectors of A(t+delt)
    Ltrue, Vtrue    = np.linalg.eig(A)
    Ltrue           = Ltrue.reshape(N, 1)
    #Ltrue           = matchPts(Ltrue.conj().T, L.conj().T , False)
    #Ltrue           = Ltrue.T
    #Vtrue           = matchPts(Vtrue, V)
    
    ELerrs[0][iter] = abs(max((Ltrue - L)))
    for k in range(N):
        EVerrs[k, iter] =  np.linalg.norm(Vtrue[:, k] - V[:, k])
    
    iter    = iter + 1;
    #if max(EVerrs[k,:]) > N*N*1e-3:
        # print("warning", iter, t, max(EVerrs[k,:]) )

# mat1 = io.loadmat('saveEL.mat')
# mat2 = io.loadmat('saveEV.mat')
# ELerrs = mat1["ELerrs"]
# EVerrs = mat2["EVerrs"]
import matplotlib.pyplot as plt
plt.figure(figsize = (9,6))
plt.subplot(211)
plt.semilogy(ELerrs.T)
plt.xlabel("iters")
plt.ylabel("error in eigenvalues")

plt.subplot(212)
plt.plot(EVerrs.T)
plt.xlabel("iters")
plt.ylabel("error in eigevectors")
plt.yscale("log")
plt.show()

