import integral_py
import integral_semipy
import integral

print("Integrate: {}".format(integral_py.integrate_f(1.0, 10.0, 10000)))
print("Integrate: {}".format(integral_semipy.integrate_f(1.0, 10.0, 10000)))
print("Integrate: {}".format(integral.integrate_f(1.0, 10.0, 10000)))


