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
    array = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    expected = [
        1,
        2,
        3,
        4,
        8,
        7,
        6,
        5,
        9,
        10,
        11,
        12,
        16,
        15,
        14,
        13,
    ]

    result = flatten(array, lawnmower)
    assert result == expected

    expected_order_flip = [
        1,
        5,
        9,
        13,
        14,
        10,
        6,
        2,
        3,
        7,
        11,
        15,
        16,
        12,
        8,
        4,
    ]

    result_flipped = flatten(array, lawnmower, order=(1, 0))
    assert result_flipped == expected_order_flip
