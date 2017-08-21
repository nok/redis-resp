# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


path = os.path.abspath(os.path.dirname(__file__))

# Version:
version = '0.1.0'

setup(
    name='resp',
    packages=find_packages(exclude=["tests.*", "tests"]),
    include_package_data=True,
    version=version,
    description='Making the Redis Mass Insertion simple.',
    author='Darius Morawiec',
    author_email='ping@nok.onl',
    url='https://github.com/nok/resp/tree/stable',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[],
    keywords=['redis', 'resp'],
    license='MIT',
)