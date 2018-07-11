"""
We have a matrix, "A".

We'll represent it with a list (called "A") containing each column. We'll call these
columns "a1, a2, a3 . . . an". The individual columns (a1, a2, etc.) will be transposed
row vectors.

These vectors (a1, a2, etc.) will be referred to generally as aiself.

So when i=2, we are referring to the vector a2.

Let's pick the first vector, a1.

We'll divide vector a1 by (np.linalg.norm(a1)). This divides the original vector by its norm (thanks numpy).
