from distutils.core import setup, Extension
import numpy
import os

os.environ['CC'] = 'g++';
setup(name='matt_simple_test', version='1.0', ext_modules =[Extension('_simple',
 ['simple.cc', 'simple.i'], include_dirs = [numpy.get_include(),'.'])])