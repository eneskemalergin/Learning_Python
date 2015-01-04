# What is PyPI?

''' PyPI is short version for Python Package Index that provides a centralized
    repository for third-party python modules on the internet.
    For now we have github to publish our code with everyone.
    '''

# Prepare your distribution

'''
    In order to share your newly created module, you need to prepare a
distribution. This is the Python name given to the collection of files that
together allow you to build, package, and distribute your module.

    Once a distribution exists, you can install your module into your local copy
of Python, as well as upload your module to PyPI to share with the world.

'''
# Step 1: Begin by creating a folder for your module

'''
    With the folder created, copy your nester.py module file into the
folder. To keep things simple, let’s call the folder nester:

'''

# Step 2: Create a file called "setup.py" in your new folder

'''
    This file contains metadata about your distribution. Edit this file by adding something similar to that:
from distutils.core import setup

setup(
    name            = 'nester',
    version         = '1.0.0',
    py_modules      = ['nester'],
    author          = 'EnesKemalErgin',
    author_email    = 'eneskemalergin@gmail.com'
    url             = 'eneskemalergin@gmail.com'
    description     = 'A simple printer of nested list',
    )

    
'''

# Now we have a folder and two file init. It's time to build a distribution

# Step 3: Build a distribution file

'''
    The distribution utilities include all of the smarts required to build a distribution. Open a terminal
window within your nester folder and type a single command: python3 setup.py sdist.

'''

# Step 4: Install your distribution into your local copy of Python
''' Staying in the terminal, type this command: sudo python3 setup.py install. '''

