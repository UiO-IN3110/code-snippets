from distutils.core import setup, Extension
import numpy
import os

setup(name='simple',
      version='1.0',
      ext_modules =[Extension('_simple',
                             ['simple.c', 'simple.i'],
                    include_dirs = [numpy.get_include(),'.'])
                   ])
