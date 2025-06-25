from typing import Optional, Tuple


def zorder(
    index: int, shape: Tuple[int, ...], order: Optional[Tuple[int, ...]] = None
) -> Tuple[int, ...]:
    """
    Returns a position in the z order pattern, given a shape to traverse
    over. If order is specified, perform the iteration over a different
    ordering of the axes.
    """

    # Setup an ascending order
    if order is None:
        order = tuple(range(len(shape)))

    # Check the size of the input are correct
    if len(order) != len(shape):
        raise ValueError("Order must match the number of dimensions in shape.")

    if not all(s > 0 for s in shape):
        raise ValueError("All dimensions in shape must be greater than zero.")

    if not all(s == shape[0] for s in shape):
        raise ValueError("All dimensions in shape must be equal for z-ordering.")

    dim = shape[0]
    if (dim & (dim - 1)) != 0 and dim > 1:
        raise ValueError("Shape size must be a power of 2 for z-ordering.")

    bit_length = dim.bit_length()

    position = [0] * len(shape)

    for bit in range(bit_length):
        for axis in order:
            position[axis] |= (index & 0x1) << bit
            index >>= 1

    return tuple(position)
