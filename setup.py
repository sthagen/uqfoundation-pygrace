#!/usr/bin/env python
# 
# Authors:
#  Michael McKerns    (mmckerns@caltech.edu)
#  Daniel B. Stouffer (daniel.stouffer@canterbury.ac.nz)
#  Dean Malmgren
#  Mike Stringer

try: # see if easy_install is available
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False

# build the 'setup' call
setup_code = """
setup(name='pygrace',
      version='0.5',
      description='Python bindings and wrapper for grace',
      maintainer = 'Daniel B. Stouffer',
      maintainer_email = 'daniel.stouffer@canterbury.ac.nz',
      url = 'http://pygrace.github.com/',
      packages=['pygrace',
                'pygrace.Extensions',
                'pygrace.Styles',
                'pygrace.Styles.ColorBrewer',
                ],
      package_dir={'pygrace':'pygrace',
                   'pygrace.Extensions':'pygrace/Extensions',
                   'pygrace.Styles':'pygrace/Styles',
                   'pygrace.Styles.ColorBrewer':'pygrace/Styles/ColorBrewer',
                  },
     package_data={'pygrace.Styles.ColorBrewer':['*.dat'],
                   },
     scripts=['pygrace/Scripts/pg_cdf'],
"""

# add dependencies
grace_version = '>=5.1.14'
numpy_version = '>=1.0'
if has_setuptools:
    setup_code += """
      install_requires=("numpy%s"),
""" % numpy_version

# close 'setup' call, and exec the code
setup_code += """    
      )
"""
exec setup_code

# if dependencies are missing, print a warning
try:
    import numpy
    from os import system
    xmgrace_missing = system("xmgrace -v") #grep "Grace-" | sed -e "s/Grace-//"
    if xmgrace_missing: raise ImportError
except ImportError:
    print "\n***********************************************************"
    print "WARNING: One of the following dependencies is unresolved:"
    print "    Numpy %s" % numpy_version
    print "    Grace %s" % grace_version
    print "***********************************************************\n"

# end of file
