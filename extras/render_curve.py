from curvewalk.zorder import zorder
from curvewalk.hilbert import hilbert
from curvewalk.lawnmower import lawnmower
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from typing import Tuple
from functools import reduce


def render_curve(shape: Tuple[int, ...], curve_function):
    """
    Render a curve based on the provided shape and curve function.

    :param shape: A tuple representing the shape of the curve.
    :param curve_function: The function to generate the curve.
    """
    fig, ax = plt.subplots()
    ax.set_title(f"Curve {curve_function.__name__} with shape {shape}")

    size = reduce(lambda x, y: x * y, shape, 1)
    prev_coord = None
    colour_map = plt.get_cmap("hsv")
    for i in range(size):
        colour_pos = i / size
        coord = curve_function(i, shape)
        plt.plot(
            *[(a, b) for a, b in zip(prev_coord, coord)],
            "-",
            color=colour_map(colour_pos),
        ) if prev_coord else None
        prev_coord = coord

    # Plot the curve
    ax.set_aspect("equal", adjustable="box")

    plt.show()


def render_curve_3d(shape: Tuple[int, ...], curve_function):
    """
    Render a 3D curve based on the provided shape and curve function.

    :param shape: A tuple representing the shape of the curve.
    :param curve_function: The function to generate the curve.
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_title(f"Curve {curve_function.__name__} with shape {shape}")

    size = reduce(lambda x, y: x * y, shape, 1)
    prev_coord = None
    colour_map = plt.get_cmap("hsv")
    for i in range(size):
        colour_pos = i / size
        coord = curve_function(i, shape)
        if prev_coord:
            ax.plot(*zip(prev_coord, coord), "-", color=colour_map(colour_pos))
        prev_coord = coord

    # Plot the curve
    ax.set_box_aspect([1.0, 1.0, 1.0])  # type:ignore # Type is wrong in matplotlib
    plt.show()


if __name__ == "__main__":
    arg_parser = ArgumentParser(description="Render a curve")
    arg_parser.add_argument("kind", type=str, help="Kind of curve to render")
    arg_parser.add_argument(
        "shape",
        type=str,
        help="Shape of the curve to render as a comma-separated list of integers",
    )

    args = arg_parser.parse_args()

    shape = args.shape.split(",")
    shape = [int(x) for x in shape]
    shape = tuple(shape)

    if len(shape) == 2:
        match args.kind:
            case "zorder":
                render_curve(shape, zorder)
            case "hilbert":
                render_curve(shape, hilbert)
            case "lawnmower" | "boustrophedon":
                render_curve(shape, lawnmower)
            case _:
                raise ValueError(f"Unknown curve kind: {args.kind}")
    elif len(shape) == 3:
        match args.kind:
            case "zorder":
                render_curve_3d(shape, zorder)
            case "hilbert":
                render_curve_3d(shape, hilbert)
            case "lawnmower" | "boustrophedon":
                render_curve_3d(shape, lawnmower)
            case _:
                raise ValueError(f"Unknown curve kind: {args.kind}")
