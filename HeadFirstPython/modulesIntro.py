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
2. Create a setup.py file within that folder. The setup.py must contain the metadata required to transform the module
    into a distribution. 

Once done, the distribution must be built using the command `python3 setup.py sdist`. Then to install the distribution, 
we use `python3 setup.py install`. At the end of the process, the file structure becomes:

nester
├── build
│   └── lib
│       └── nester.py
├── dist
│   └── nester-1.0.tar.gz
├── MANIFEST
├── nester.py
└── setup.py

If we attempt an execution at this point, it causes a NameError since Python won't be able to find nester since all code
in Python is associated with a namespace. The code in the Python files are linked to the __main__ namespace, but when we
create our own custom modules, they're  put in a namespace with the same name as the module. Thus, the function needs to
be invoked with the name of the namespace (and consequently module) that contains it. So, we use `nester.print_lol()` 
instead of just `print_lol()`. This is called Namespace Qualification. 

An important distinction is the use of `from <module> import <functionName>` statements, which remove the necessity for 
namespace qualifications. However, if there's a function with the same name in the file as well, the imported one will
override the local function. 

"""

import nester

cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
nester.print_lol(cast)

"""
To share the code with the PyPI community, we used to have to do a commandline registration (telling the command line 
utilities the login credentials required). The command for this is `python3 setup.py register`. Pre-registration is no 
longer supported (or required), and hence the files can be directly uploaded with `python3 setup.py sdist upload`.  

Python, just like java, has the concept of a bytecode file. So, it generates a .pyc file (like a java's .class file) 
that it can execute directly and skip the compilation as long as the source code doesn't change. However, this is a 
run-time optimization performed by the python interpreter, and the original .py file is still the one we need the users 
to have. 
"""

# Usage of an extra argument passed to the function.

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman",
                ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

nester.print_lol(movies, 1)