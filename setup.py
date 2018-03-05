# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

tests_require = ['six', 'pytest>=3.0', 'pytest-cov']

setup(
    name='py.snapshottest',
    version='0.0.1',
    description='Snapshot Testing utils for py.test',
    long_description=readme,
    author='Yavor Atov',
    author_email='yavor.atov@gmail.com',
    url='https://github.com/YAtOff/snapshottest',
    # custom PyPI classifier for pytest plugins
    entry_points={
        'pytest11': [
            'snapshottest = snapshottest.pytest',
        ]
    },
    install_requires=['six>=1.10.0', 'termcolor'],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'pytest': [
            'pytest',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    license='MIT',
    packages=find_packages(exclude=('tests', ))
)
