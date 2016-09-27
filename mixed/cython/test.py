from timeit import timeit
import integral_py
import integral_semipy
import integral

print("Pure Python integrate: {}".format(integral_py.integrate_f(1.0, 10.0, 10000)))
print("Semi (C)Python integrate: {}".format(integral_semipy.integrate_f(1.0, 10.0, 10000)))
print("Cython integrate: {}".format(integral.integrate_f(1.0, 10.0, 10000)))

N = 1000
print("")
print("Running timings ({} integrations)".format(N))

print("Pure Python integrate: {}".format(timeit("integral_py.integrate_f(1.0, 10.0, 10000)", setup="import integral_py", number=N)))
print("Semi (C)Python integrate: {}".format(timeit("integral_semipy.integrate_f(1.0, 10.0, 10000)", setup="import integral_semipy", number=N)))
print("Cython integrate: {}".format(timeit("integral.integrate_f(1.0, 10.0, 10000)", setup="import integral", number=N)))

