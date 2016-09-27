cdef extern from "math.h":
     double sin(double arg)

cdef double f(double x):
    return sin(x**2)

cpdef double integrate_f(double a, double b, int N):
    cdef double s=0
    cdef double dx = (b-a)/N
    cdef int i
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
