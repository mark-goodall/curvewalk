from curvewalk.zorder import zorder, inverse_zorder
import pytest
from functools import reduce
from hypothesis import given, strategies as st


def test_minimal_2d_zorder():
    assert zorder(0, (2, 2)) == (0, 0)
    assert zorder(1, (2, 2)) == (1, 0)
    assert zorder(2, (2, 2)) == (0, 1)
    assert zorder(3, (2, 2)) == (1, 1)

    assert inverse_zorder((0, 0), (2, 2)) == 0
    assert inverse_zorder((1, 0), (2, 2)) == 1
    assert inverse_zorder((0, 1), (2, 2)) == 2
    assert inverse_zorder((1, 1), (2, 2)) == 3


def test_zorder_invalid_args():
    with pytest.raises(ValueError):
        zorder(0, (4, 4), order=(0, 1, 2))
    with pytest.raises(ValueError):
        zorder(0, (3, 3))
    with pytest.raises(ValueError):
        zorder(0, (2, 4))
    with pytest.raises(ValueError):
        zorder(
            0,
            (2, -2),
        )
    with pytest.raises(ValueError):
        inverse_zorder((0, 0), (2, 2), (0, 1, 2))
    with pytest.raises(ValueError):
        inverse_zorder((0, 0), (2, 2, 2), (0, 1, 2))
    with pytest.raises(ValueError):
        inverse_zorder((0, 0, 0), (2, 0, 2), (0, 1, 2))
    with pytest.raises(ValueError):
        inverse_zorder((0, 0, 0), (2, 4, 2), (0, 1, 2))
    with pytest.raises(ValueError):
        inverse_zorder((0, 0, 0), (3, 3, 3), (0, 1, 2))


@st.composite
def shape_and_order(draw):
    dims = draw(st.integers(min_value=1, max_value=4))
    order = draw(st.permutations(range(dims)))
    size = 2 ** draw(st.integers(min_value=1, max_value=3))
    shape = [size] * dims
    return shape, order


@given(shape_and_order())
def test_satisfies_zorder_constraints(shape_and_order):
    shape, order = shape_and_order
    pos = set()
    size = reduce(lambda x, y: x * y, shape, 1)
    dims = len(shape)
    previous = None

    for i in range(size):
        position = zorder(i, shape, order)
        pos.add(position)

        assert inverse_zorder(position, shape, order) == i

        for j in range(dims):
            assert 0 <= position[j] < shape[order[j]], (
                f"Out of bounds on index: {i} pos:{position}"
            )

        # Is near the previous position
        diff = (
            sum(abs(a - b) for a, b in zip(position, previous))
            if previous and i % 4 in [1, 2, 3]
            else 1
        )
        assert diff <= 2, f"where {position} and {previous} diff too much."

        previous = position

    assert len(pos) == size
