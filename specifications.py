def unit_vector(v):
    """
    Takes a vector, "v", and returns its unit vector form

    v: numpy array

    Returns:
        numpy array

    Exceptions:
        ValueError
        ZeroDivisionError
    """
    pass


def subtract_projection(a,q):
    """
    Takes two vectors and subtracts the projection of a onto q from a

    a: numpy array
    q: numpy array

    Returns:
        numpy array

    Exceptions:
        ValueError
    """
    pass


def gram_schmidt(m):
    """
    Takes a matrix and returns an orthonormal form of the matrix using Gram-Schmidt orthogonalization

    a: numpy array with dimensions "m" by "n"

    Returns:
        numpy array

    Exceptions:
        ValueError
    """
    pass

    
"""
Partial alternative explanation:

We have a matrix, "A".

We'll represent it with a list (called "A") containing each column. We'll call these
columns "a1, a2, a3 . . . an". The individual columns (a1, a2, etc.) will be transposed
row vectors.

These vectors (a1, a2, etc.) will be referred to generally as ai. So when i=2, we are referring to the vector a2.

Let's pick the first vector, a1.

We'll divide vector a1 by (np.linalg.norm(a1)). This divides the original vector by its norm (thanks numpy).
This creates a unit vector version of a1. We will call the resulting unit vector version of a1, "q1".

This first unit vector can just be assigned to the variable q1 and left alone for the moment. Please don't just incorporate (np.linalg.norm(a1))
as a value when we're trying to call q1. In my opinion, setting it as a variable may be less efficient but is much easier to read and debug.

For all subsequent vectors, (a2, a3, a4, etc.), we will create the unit vector version like we did above.

Then, with a2, we will (for some reason that is unknown to me) find a2^t (the transposed version of a2) by calculating:

        a2 - ((q1^t)*a2)q1.

If it floats your boat, you can assign q1^t as a variable like so:
    q1^t = np.transpose(q1)

    pick a vector
    make it a unit vector
    subtract projections of subsequent
