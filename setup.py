from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A simple package for pygame.'
LONG_DESCRIPTION = 'A package that allows to make buttons and textboxes in pygame.'

# Setting up
setup(
    name="pygame_functions",
    version=VERSION,
    author="DL#6569",
    author_email="<dldavejackson@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pygame'],
    keywords=['python', 'pygame', 'buttons', 'textboxes'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
