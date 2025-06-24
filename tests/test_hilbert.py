import pytest
from curvewalk.hilbert import hilbert


def test_hilbert_2d_minimal():
    assert hilbert(0, (2, 2)) == (0, 0)
    assert hilbert(1, (2, 2)) == (1, 0)
    assert hilbert(2, (2, 2)) == (1, 1)
    assert hilbert(3, (2, 2)) == (0, 1)


def test_hilbert_shape_checks():
    with pytest.raises(ValueError):
        hilbert(0, (2, 3))
    with pytest.raises(ValueError):
        hilbert(0, (3, 2))
    with pytest.raises(ValueError):
        hilbert(0, (1, -1))
    with pytest.raises(ValueError):
        hilbert(0, (0, 1))
    with pytest.raises(ValueError):
        hilbert(0, (3, 3))


@pytest.mark.parametrize("length", [4, 8, 16])
def test_hilbert_2d(length):
    size = length * length
    pos = set()
    previous = None
    for i in range(size):
        position = hilbert(i, (length, length))
        pos.add(position)
        assert 0 << position[0] < length
        assert 0 <= position[1] < length

        diff = (
            abs(position[0] - previous[0]) + abs(position[1] - previous[1])
            if previous is not None
            else 0
        )

        assert diff <= 1, f"Position {position} is not adjacent to previous {previous}"

        previous = position

    assert len(pos) == size, f"Expected {size} unique positions, got {len(pos)}"
