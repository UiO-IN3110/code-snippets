from distutils.core import setup, Extension
from Cython.Distutils import build_ext

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("integral", ["integral.pyx"]),
                 Extension("integral_semipy", ["integral_semipy.pyx"]),
                 Extension("integral_py", ["integral_py.pyx"])]
)
