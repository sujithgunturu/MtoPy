# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:57:54 2020

@author: Personal
"""
from math import *
def rot2(theta):
    # Input theta is assumed to be in radians
    # Returns 2x2 rotation matrix around z axis
    # dR is the derivative of R w.r.t. theta
    c = cos(theta); 
    s = sin(theta);
    R = [[c, -s], [s, c]];
    # if nargout > 1:
    dR = [[-s, -c], [c, -s]];

    return R, dR
