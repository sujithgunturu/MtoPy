# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:01:31 2020

@author: Personal
"""
from Rot2 import * 
from insertRow import * 
from insertCol import * 


def rot3(alpha, beta, gamma):
    
    # Inputs:
    # alpha, beta, gamma : angles in radians
    # Outputs:
    # Rx: Rotation around x axis by alpha
    # Ry: Rotation around y axis by beta
    # Rz: Rotation around z axis by gamma
    # Rotations counterclockwise when looking at origin
    # ROTATION AROUND X AXIS BY ALPHA
    
    Rx, _ = rot2(alpha)
    Rx = insertRow(Rx, [[0, 0]], 0)
    Rx = insertCol(Rx, [[1], [0], [0]], 0)
     
    # ROTATION AROUND Y AXIS BY BETA
    Ry, _ = rot2(beta);
    Ry = insertRow(Ry, [[0,0]], 1)
    Ry = insertCol(Ry, [[0], [1], [0]], 1)

    # ROTATION AROUND Z AXIS BY GAMMA
    Rz, _ = rot2(gamma)
    Rz = insertRow(Rz, [[0, 0]], 2)
    Rz = insertCol(Rz, [[0], [0],[1]], 2)
                   
                         
    _, dRx = rot2(alpha);
    dRx = insertRow(dRx, [[0, 0]], 0);
    dRx = insertCol(dRx, [[1] ,[0], [0]], 0);

    # ROTATION AROUND Y AXIS BY BETA
    _, dRy = rot2(beta);
    dRy = insertRow(dRy, [[0,0]], 1);
    dRy = insertCol(dRy, [[0], [1], [0]], 1);

    # ROTATION AROUND Z AXIS BY GAMMA
    _, dRz = rot2(gamma);
    dRz = insertRow(dRz, [[0,0]], 2);
    dRz = insertCol(dRz, [[0], [0], [1]], 2);

                        
                        
    return Rx, Ry, Rz, dRx, dRy, dRz

