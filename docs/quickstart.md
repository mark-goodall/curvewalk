# Quickstart

## Iterating over arrays

To iterate over an array using one of the curves, you could do the following:

```python
import curvewalk
from curvewalk.lawnmower import lawnmower

array = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16],
]

for item in curvewalk.iterate_over(array, lawnmower):
  print(item, end=", ")
# 1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 16, 15, 14, 13,
```

The method `curvewalk.iterate_over` can also accept a numpy style class as
input.

### Iterating in a different axis order

To use a different axes order, pass in the alternative axes order. For example,
to iterate over the above array mirrored on the diagonal we can use the
following:

```python
for item in curvewalk.iterate_over(array, lawnmower, order=(1, 0)):
  print(item, end=", ")
# 1, 5, 9, 13, 14, 10, 6, 2, 3, 7, 11, 15, 16, 12, 8,  4,

This can become more useful or necessary with larger arrays or higher
dimensions, where the default order may not be suitable for your use case.
```

## Determining the position along a curve

There are inverse methods which can be used to determine how far along the
curve a point is:

```python
from curvewalk.lawnmower import lawnmower_inverse

print(lawnmower_inverse((1, 1), (2, 2)))  # Output: 2
```

In the above example the point `(1, 1)` is the third point along the curve in a
2x2 array, with zero indexing.
