from distutils.core import setup, Extension

name = "helloworld"    # name of the module
version = "1.0"        # the module's version number

setup(name=name, version=version,
      # distutils detects .i files and compiles them automatically
      ext_modules=[Extension(name='_helloworld', # SWIG requires _ as a prefix for the module name
                             sources=["helloworld.i", "src/HelloWorld.cpp", "src/HelloWorld2.cpp"],
                             include_dirs=['src'],
                             swig_opts=["-c++"])
    ])
