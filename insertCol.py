# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:10:00 2020

@author: Personal
"""

import numpy as np
def insertCol(A, c, n):
    # Inputs: 
    # A : matrix.
    # c : column vector (must be of the same size as a column of A).
    # n : place where column c should be inserted.
    # Output: 
    # B : nth column of B is c, rest of elements are same as A.
    # Insert column c as the nth column of A.
    # The output B has one more column than A.
    # If n == 0 then c is the first column of B. 
    # If n == size(A,2) then c is the last column of B.
    # (size(A,2) is # cols of A)
    
    c = np.array(c[:])
    A = np.array(A)
    N = len(A[0, :])
    if n == 0:           # r inserted as column 
        B = np.column_stack((c, A))
    elif n == N:
        B = np.column_stack((A, c))      # r inserted as column N
    else:      # 0 < n < N
        Ale = A[:, 0:n]
        Ari = A[:, n:N]
        B = np.column_stack((Ale, c, Ari))
    
    return B

