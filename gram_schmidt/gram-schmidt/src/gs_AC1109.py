#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:49:43 2018

@author: robynpack
"""
import numpy as np
'''
1. make the first col in A a unit vector, start with ai=0
    a. qi=ai/||ai||
2. take that vec, subtract the  projections of it from all remaining
3. go to the next vector, do the same

4. once finished, if you take the dot product of any two cols, should be 0

functions
1. unit_vec
2. subtract projcetion
check_dots
'''

def unit_vector(v):
    """
    Takes a vector v and returns a unit vector form
    v: numpy array
    Returns :
        numpy array
    Exceptions:
        ValueError
    """
    
    return v/la.norm(v)


def subtract_projection(a, q):
    """
    subtract projection of a onto q from a
    Takes two vectors and substracts the projection of a onto q from a
    a : numpy array
    q: numpy array
    Retruns:
        numpy array
    Exceptions:
        ValueError: if a and q are not the same dimension
    """
    return a -float(q.transpose() * a) * q

def gram-schmidt(A):
    """
    Takes a matrix and returns an orthonormal "version" suing Gram-Schmidt 
    a: numpy array
    Returns:
        numpy array
    Exceptions:
    """
    Q = A.copy().astype(np.float64)
    n = A.shape[1]
    for i in range(A.shape[1]):
        q = Q[:, i]
        q = unit_vector(q)
        Q[:, i] = q
        for j in range(i + 1, n):
            Q[:, j] = subtract_projection(Q[:, j], q)
    return Q
