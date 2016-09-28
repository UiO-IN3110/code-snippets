from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "Integration",
    ext_modules = cythonize("*.pyx"),
)
