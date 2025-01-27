"""
This file belong to https://github.com/snolfi/evorobotpy
Author: Stefano Nolfi, stefano.nolfi@istc.cnr.it

setupErDiscrim.py, python wrapper for discrim.cpp

This file is part of the python module ErDiscrim.so that include the following files:
discrim.cpp, discrim.h, robot-env.cpp, robot-env.h, utilities.cpp, utilities.h, ErDiscrim.pxd, ErDiscrim.pyx and setupErDiscrim.py
And can be compiled with cython and installed with the commands: cd ./evorobotpy/lib; python3 setupErDiscrim.py build_ext –inplace; cp ErDiscrim*.so ../bin
"""

#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy

# linux
#include_gsl_dir = "/usr/include/gsl"
#lib_gsl_dir = "/usr/lib/x86_64-linux-gnu"

# mac os
include_gsl_dir = "/opt/homebrew/Cellar/gsl/2.7.1/lib"
lib_gsl_dir = "/opt/homebrew/Cellar/gsl/2.7.1/include"

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("ErDiscrim",
                             sources=["ErDiscrim.pyx", "robot-env.cpp"],
                             language="c++",
                             include_dirs=[numpy.get_include(), include_gsl_dir],
			     libraries=["gsl", "gslcblas"],
			     library_dirs=[lib_gsl_dir])],
)



