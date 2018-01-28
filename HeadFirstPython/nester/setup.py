from distutils.core import setup

"""
This module stores the metadata about our custom module nester.py.
The command required to build a distribution from this file is `python3 setup.py sdist`.
The command to install the built distribution after the previous command is `python3 setup.py install`.
"""

setup (
    name        = 'nester',
    version     = '1.1',
    py_modules  = ['nester'],        # Links the module's metadata with the arguments of the setup function.
    author      = 'Somenath Sinha',
    author_email= 'somu.sysadm@gmail.com',
    url         = 'https://www.somusysadmin.com',
    description = 'A simple printer of nested lists - now with indentation.',
)
