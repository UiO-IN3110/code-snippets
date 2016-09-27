import numpy
from timeit import timeit
import apply_py
import apply_numpy
import apply

a = numpy.linspace(0, 10, 1e6, dtype=numpy.double)


print("Pure Python apply_sin: {}".format(apply_py.apply_sin(a)))
print("Numpy apply_sin: {}".format(apply_numpy.apply_sin(a)))
print("Cython apply_sin: {}".format(apply.apply_sin(a)))

N = 10
print("")
print("Running timings ({} integrations)".format(N))

print("Pure Python apply_sin: {}".format(timeit("apply_py.apply_sin(a)", setup="import apply_py; from __main__ import a", number=N)))
print("Numpy apply_sin: {}".format(timeit("apply_numpy.apply_sin(a)", setup="import apply_numpy; from __main__ import a", number=N)))
print("Cython apply_sin: {}".format(timeit("apply.apply_sin(a)", setup="import apply; from __main__ import a", number=N)))

