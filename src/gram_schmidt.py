import numpy.linalg as la
import numpy as np

def unit_vector(vec):
    """
    Gets some vector in unit vector form

    v: numpy array

    Returns: numpy array

    Raises: ValueError
    """
    return vec/la.norm(vec)

"""
Test (pytest docs for recs)

"""

def subtract_projection(a, q):
    """
    takes two vectors and subtracts the projection of a onto q

    a: numpy array
    q: numpy array

    Returns: numpy array
    """
    return a - float(q.transpose()*a)*q

def gram_schmidt(A):
    """
    Takes the matrix and computes the orthonormal version using gram_schmidt

    a: m*n numpy array

    Returns: a matrix

    Raises: ValueError
    """
    Q = A.copy().astype(np.float64)
    n = A.shape[1]
    for i in range(A.shpe[1]):
        q = Q[:,i]
        q = unit_vector(q)
        Q[:,i] = q
        for j in range(i+1, n):
            Q[:, j] = subtract_projection(Q[:, j], q)
    return Q

gram_schmidt(np.array[[1,2,3,4],[1,2,3,4],[5,6,7,8]])
