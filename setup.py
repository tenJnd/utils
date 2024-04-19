"""setup file"""
import os

from setuptools import setup, find_packages


def readme():
    """readme"""
    with open('README.md', encoding='utf-8') as file:
        return file.read()


version = 1.0

setup(
    name='jnd_utils',
    version=version,
    description='useful scripts',
    long_description=readme(),
    url='https://github.com/tenJnd/utils',
    author='Tomas.jnd',
    author_email='',
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.6',
    install_requires=[],
)
