import pytest
import numpy as np
import gram_schmidt as gs

def test_unit_vector1():
  v = numpy.zeros([2,1])
  with pytest.raises(ValueError):
    gs.unit_vector(v)

def test_unit_vector2():
  v = np.ones([2,1])
  new_v = gs.unit_vector(v)
  assert np.abs(np.norm(new_v) - 1.0) < 0.0001

def test_subtract_projection():
  
