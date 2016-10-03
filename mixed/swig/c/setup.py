from distutils.core import setup, Extension

name = "hw"      # name of the module
version = "1.0"  # the module's version number

setup(name=name, version=version,
      # distutils detects .i files and compiles them automatically
      ext_modules=[Extension(name='_hw', # SWIG requires _ as a prefix for the module name
                             sources=["hw.i", "src/hw.c"],
                             include_dirs=['src'])
    ])
