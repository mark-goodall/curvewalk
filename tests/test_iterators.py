from curvewalk import iterate_over, flatten
from curvewalk.lawnmower import lawnmower
import numpy as np


def test_iterate_over_array():
    array = [[1, 2], [3, 4]]
    expected = [1, 2, 4, 3]

    result = list(iterate_over(array, lawnmower))

    assert result == expected


def test_iterate_over_nparray():
    array = np.array([[1, 2], [3, 4]])
    expected = [1, 2, 4, 3]

    result = list(iterate_over(array, lawnmower))

    assert result == expected


def test_flatten():
    array = [[1, 2], [3, 4]]
    expected = [1, 2, 4, 3]

    result = flatten(array, lawnmower)

    assert result == expected
