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
    ext_modules = [Extension("ErForaging",
                             sources=["ErForaging.pyx", "robot-env.cpp"],
                             language="c++",
                             include_dirs=[numpy.get_include(), include_gsl_dir],
			     libraries=["gsl", "gslcblas"],
			     library_dirs=[lib_gsl_dir])],
)
"""
setup(ext_modules = cythonize(
           "dpole.pyx",
           language="c++",
           include_path=[numpy.get_include(), include_gsl_dir],
           library_dirs=[lib_gsl_dir],
     ))
"""


