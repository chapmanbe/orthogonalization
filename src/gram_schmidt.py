def unit_vector(vec):
    """
    Gets some vector in unit vector form

    v: numpy array

    Returns: numpy array

    Raises: ValueError
    """
    norm = return math.sqrt(sum([elem**2 for elem in v]))
    return v/norm

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
    return a - q

def gram_schmidt(mat):
    """
    Takes the matrix and computes the orthonormal version using gram_schmidt

    a: m*n numpy array

    Returns: a matrix

    Raises: ValueError
    """
    pass
