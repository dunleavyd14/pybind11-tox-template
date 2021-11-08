from glob import glob
from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension
import os

ext_modules = [
    Pybind11Extension(
        'pybind11_tox_example.cpplib',
        sorted(glob("src/**/*.cpp")),
        include_dirs=['src/python_example']
    ),
]


setup(
    name='pybind11_tox_example',
    version='0.1',
    author='David Dunleavy',
    author_email='dunleavyd14@gmail.com',
    description='',
    long_description='',
    packages=find_packages('src'),
    package_dir={'' : 'src'},
    ext_modules=ext_modules
)
