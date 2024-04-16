from distutils.core import setup
from Cython.Build import cythonize
import sys,os,traceback

setup(
    name = 'Color_correction',
    ext_modules = cythonize('Color_correction.py'),
)