# -*- coding: utf-8 -*-

import os
from setuptools import setup
from setuptools import find_packages


path = os.path.abspath(os.path.dirname(__file__))
setup(
    name='resp',
    packages=find_packages(exclude=["tests.*", "tests"]),
    include_package_data=True,
    version='0.1.0',
    description='Making the Redis Mass Insertion simple.',
    author='Darius Morawiec',
    author_email='ping@nok.onl',
    url='https://github.com/nok/redis=resp/tree/stable',
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