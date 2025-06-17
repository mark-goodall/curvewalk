from curvewalk.lawnmower import lawnmower, inverse_lawnmower
from hypothesis import given, strategies as st


def test_minimal_2d_lawnmower():
    assert lawnmower(0, (2, 2)) == (0, 0)
    assert lawnmower(1, (2, 2)) == (0, 1)
    assert lawnmower(2, (2, 2)) == (1, 1)
    assert lawnmower(3, (2, 2)) == (1, 0)

    assert inverse_lawnmower((0, 0), (2, 2)) == 0
    assert inverse_lawnmower((0, 1), (2, 2)) == 1
    assert inverse_lawnmower((1, 1), (2, 2)) == 2
    assert inverse_lawnmower((1, 0), (2, 2)) == 3


def test_minimal_3d_lawnmower():
    assert lawnmower(0, (2, 2, 2)) == (0, 0, 0)
    assert lawnmower(1, (2, 2, 2)) == (0, 0, 1)
    assert lawnmower(2, (2, 2, 2)) == (0, 1, 1)
    assert lawnmower(3, (2, 2, 2)) == (0, 1, 0)
    assert lawnmower(4, (2, 2, 2)) == (1, 1, 0)
    assert lawnmower(5, (2, 2, 2)) == (1, 1, 1)
    assert lawnmower(6, (2, 2, 2)) == (1, 0, 1)
    assert lawnmower(7, (2, 2, 2)) == (1, 0, 0)

    assert inverse_lawnmower((0, 0, 0), (2, 2, 2)) == 0
    assert inverse_lawnmower((0, 0, 1), (2, 2, 2)) == 1
    assert inverse_lawnmower((0, 1, 1), (2, 2, 2)) == 2
    assert inverse_lawnmower((0, 1, 0), (2, 2, 2)) == 3
    assert inverse_lawnmower((1, 1, 0), (2, 2, 2)) == 4
    assert inverse_lawnmower((1, 1, 1), (2, 2, 2)) == 5
    assert inverse_lawnmower((1, 0, 1), (2, 2, 2)) == 6
    assert inverse_lawnmower((1, 0, 0), (2, 2, 2)) == 7


@st.composite
def order_2d(draw):
    return draw(st.permutations([0, 1]))


@st.composite
def order_3d(draw):
    return draw(st.permutations([0, 1, 2]))


@st.composite
def order_4d(draw):
    return draw(st.permutations([0, 1, 2, 3]))


@given(
    st.tuples(
        st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)
    ),
    order_2d(),
)
def test_satisfies_2d_constraints(shape, order):
    pos = set()
    size = shape[0] * shape[1]
    previous = None
    for i in range(size):
        position = lawnmower(i, shape, order)
        pos.add(position)
        assert inverse_lawnmower(position, shape, order) == i

        assert 0 <= position[0] < shape[0]
        assert 0 <= position[1] < shape[1]

        # Is near the previous position
        diff = (
            abs(position[0] - previous[0]) + abs(position[1] - previous[1])
            if previous
            else 1
        )
        assert diff == 1, f"where {position} and {previous} diff too much."

        previous = position

    # Is unique walker and visits all positions
    assert len(pos) == size


@given(
    st.tuples(
        st.integers(min_value=1, max_value=25),
        st.integers(min_value=1, max_value=25),
        st.integers(min_value=1, max_value=25),
    ),
    order_3d(),
)
def test_satisfies_3d_constraints(shape, order):
    pos = set()
    size = shape[0] * shape[1] * shape[2]
    previous = None
    for i in range(size):
        position = lawnmower(i, shape, order)
        pos.add(position)
        assert inverse_lawnmower(position, shape, order) == i

        assert 0 <= position[0] < shape[0]
        assert 0 <= position[1] < shape[1]
        assert 0 <= position[2] < shape[2]

        # Is near the previous position
        diff = (
            abs(position[0] - previous[0])
            + abs(position[1] - previous[1])
            + abs(position[2] - previous[2])
            if previous
            else 1
        )
        assert diff <= 2, f"where {position} and {previous} diff too much."

        previous = position

    # Is unique walker and visits all positions
    assert len(pos) == size


@given(
    st.tuples(
        st.integers(min_value=1, max_value=5),
        st.integers(min_value=1, max_value=5),
        st.integers(min_value=1, max_value=5),
        st.integers(min_value=1, max_value=5),
    ),
    order_4d(),
)
def test_satisfies_4d_constraints(shape, order):
    pos = set()
    size = shape[0] * shape[1] * shape[2] * shape[3]
    previous = None
    for i in range(size):
        position = lawnmower(i, shape, order)
        pos.add(position)
        assert inverse_lawnmower(position, shape, order) == i

        assert 0 <= position[0] < shape[0]
        assert 0 <= position[1] < shape[1]
        assert 0 <= position[2] < shape[2]
        assert 0 <= position[3] < shape[3]

        # Is near the previous position
        diff = (
            abs(position[0] - previous[0])
            + abs(position[1] - previous[1])
            + abs(position[2] - previous[2])
            + abs(position[3] - previous[3])
            if previous
            else 1
        )
        assert diff <= 2, f"where {position} and {previous} diff too much."

        previous = position

    # Is unique walker and visits all positions
    assert len(pos) == size
