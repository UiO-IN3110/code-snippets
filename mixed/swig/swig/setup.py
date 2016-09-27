import os
from distutils.core import setup, Extension

name = "hw"    # name of the module
version = 1.0  # the module's version number

swig_cmd = "swig -python -I.. %s.i" % name

print "running SWIG:", swig_cmd
os.system(swig_cmd)

sources = ["../hw.c", "hw_wrap.c"]
setup(name=name, version=version,
      ext_modules=[Extension('_' + name, # SWIG requires _
                   sources, include_dirs=[os.pardir])
    ])
