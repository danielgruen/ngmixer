import os
import glob
from distutils.core import setup

scripts=['ngmixit']
scripts=[os.path.join('bin',s) for s in scripts]

setup(name="ngmixer", 
      version="0.1.0",
      description="Run ngmix on data",
      license = "GPL",
      author="Matthew R. Becker, Erin Scott Sheldon",
      author_email="becker.mr@gmail.com, erin.sheldon@gmail.com",
      scripts=scripts,
      packages=['ngmixer'])
