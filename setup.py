from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'DillonB07\'s utilities'
LONG_DESCRIPTION = 'file: README.md'
# Setting up
setup(
    name="Dill-tils",
    version=VERSION,
    author="DillonB07",
    author_email="<dillonbarnes07@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    url='https://github.com/DillonB07/Dill-tils',
    license='lgpl-3.0',
    install_requires=[],

    keywords=['python', 'utils', 'dillonb07', 'lgpl-3.0'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
