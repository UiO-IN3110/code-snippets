import numpy
from math import sin


def apply_sin(a):
    out = numpy.ndarray(len(a), dtype=numpy.double)

    for i in range(len(a)):
        out[i] = sin(a[i])

    return out
