# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:10:20 2020

@author: Personal
"""

import numpy as np
def insertRow(A, r, n):
    
    # Inputs: 
    #           r : row vector (must be of the same size as a row of A).
    #           n : place where row r should be inserted.
    # Output: 
    #           B : nth row of B is r, rest of elements are same as A.
    # Insert row r as the nth row of A.
    # The output B has one more row than A.
    # If n == 0 then r is the first row of B. 
    # If n == size(A,1) then r is the last row of B.
    #      (size(A,1) is # rows of A)
    r = np.array(r[:])
    A = np.array(A)
    N = len(np.array(A)[:, 1]);
    if n == 0:            # r inserted as row 1
        
        B = np.row_stack((r, A))
        # B = [[r.conj().T], [A]]
    elif n == N:
        B = np.row_stack((A, r))  # r inserted as row N
    else:                      # % 0 < n < N:
        Aup = A[0:n,:]
        Adn = A[n:N,:]
        B =  np.row_stack((Aup, r, Adn))
        
    return B
