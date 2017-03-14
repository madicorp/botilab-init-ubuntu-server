from distutils.core import setup

from setuptools import find_packages

setup(
    name='botilab-init-ubuntu-server',
    version='0.1.0',
    packages=find_packages(exclude=('venv', 'tests',)),
    url='',
    license='MIT',
    author='Pascal Ekouaghe',
    author_email='ekougs@gmail.com',
    description='Init botilab ubuntu server',
    install_requires=[
        'fabric3>=1.13.1',
    ]
)
