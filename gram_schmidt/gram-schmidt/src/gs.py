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
A = np.matrix([[1,2,1],[3,8,1],[0,4,1]],dtype=np.float64)
print(A)
print(A[:,0])
print(A[:,1])
a1=A[:,0]
a2=A[:,1]
#print(np.dot(A[:,0],A[:,1]))
print(a1.shape)
print(np.transpose(a1).shape)

print('1',np.transpose(a1)*a2,'\n')
print('2',a1*np.transpose(a2),'\n')
print('3',np.transpose(a2)*a1,'\n')
print('4',a2*np.transpose(a1),'\n')



def unit_vec(mat, i):
    '''
    Returns a unit vector version of a column in a np.array
    
    mat: a numpy array
    i: index of which column to compute on
    
    '''
    unit_vec = mat[i]/np.linalg.norm(mat[i])
    
    return unit_vec

def sub_proj(mat):
    '''
    returns a vector 
    '''
    pass

def check_dots(mat):
    '''
    returns the dot product between each column of a matrix to check for
    orthogonailty
    
    mat: a numpy matrix 
    '''
    
    for i in range(mat.shape[1]):
        dots = []
        dots.append = np.dot(mat[i])