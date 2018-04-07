from setuptools import setup, find_packages

setup (
    name = "Data Analysis",
    version = '0.0.1',
    url = "https://github.com/SomuSysAdmin/python/tree/master/DAPython/LearningPythonDA",
    author = 'SomuSysAdmin',
    author_email= 'letsomuknow@gmail.com',
    packages = find_packages(),
    install_requires = ['PyQt5',
                        'pandas',
                        'sqlalchemy',
                        'nltk',
                        'numpy',
                        "jupyter",
                        'python-twitter'],
    entry_points = {},
    extras_require = {'dev' : ['flake8',]},

)