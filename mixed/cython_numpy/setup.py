from distutils.core import setup, Extension
from Cython.Distutils import build_ext

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("apply", ["apply.pyx"]),
                 Extension("apply_py", ["apply_py.pyx"])]
)
