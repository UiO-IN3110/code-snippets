import numpy
cimport numpy

cdef extern from "math.h":
     double sin(double arg)

cpdef numpy.ndarray[numpy.double_t, ndim=1] apply_sin(numpy.ndarray[numpy.double_t, ndim=1] a):
    cdef int i

    cdef numpy.ndarray[numpy.double_t, ndim=1] out
    out = numpy.ndarray(len(a), dtype=numpy.double)

    for i in range(len(a)):
        out[i] = sin(a[i])

    return out
