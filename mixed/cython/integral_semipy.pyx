from libc.math cimport sin

def f(x):
    return sin(x**2)

cpdef double integrate_f(double a, double  b, int N):
    cdef double s = 0
    cdef double dx = (b-a)/N
    cdef int i
    for i in range(N):  # compiles to C loop if i is declared as int
        s += f(a+i*dx)
    return s*dx
