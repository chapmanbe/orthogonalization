import pytest
import numpy as np
import gramschmidt as gs

def test_unit():
    v = np.zeros([2,1])
    with pytest.raises(ValueError):
        gs.unit_vector(v)
    v2 = np.ones([2,1])
    "assert something == something"


def test_projection():
    """
    test if the result and original are orthogonal, if dot product ==0
    """
    v = np.array([1,2,3])
    q = gs.unit_vector(v)

    assert np.dot(v,gs.substract_projection(v,q)) == 0
    q2 = np.array([1,2])
    with pytest.raises(ValueError):
        gs.substract_projection(v,q2)
