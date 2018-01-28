# Modules are used to organize code for optimal sharing.
# Distribution utilities are used to actually share the module.

""" A module is simply a file containing python code. The Python Package Index (PyPI) is a centralized repository for
3rd party Python modules. Note that block comments are possible using triple quotes! """

# To show the location of the built-in modules in function, we can type "import sys; sys.path". This gives the location
# where the python interpreter originally searches for modules.

"""

The nester.py module needs to be packaged properly for it to constitute a distribution. A distribution is a bunch of 
python files that together allow us to build, package and distribute our modules. To create a distribution, for 
nester.py, we have to:

1. Create a folder to contain the files, say, 'nester'.
2. Create a setup.py file within that folder.  

"""

