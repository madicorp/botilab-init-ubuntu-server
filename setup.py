from distutils.core import setup

from pip.req import parse_requirements
from setuptools import find_packages

requirements = [str(ir.req) for ir in parse_requirements('requirements.txt')]
with open('VERSION') as f:
    version = f.readlines()[0].strip()

setup(
    name='botilab-init-ubuntu-server',
    version=version,
    packages=find_packages(exclude=('venv', 'tests',)),
    url='',
    license='MIT',
    author='Pascal Ekouaghe',
    author_email='ekougs@gmail.com',
    description='Init botilab ubuntu server',
    install_requires=requirements
)
