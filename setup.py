#! /usr/bin/env python
import haikunator

from setuptools import setup

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(name='haikunator',
      author='Atrox',
      author_email='mail@atrox.me',
      description='Heroku-like random name generator.',
      license='GPLv3',
      version='0.0.1',
      url='https://github.com/AtroxDev/haikunator',
      packages=['haikunator'],
      test_suite='haikunator.tests',
      include_package_data=True,
      classifiers=CLASSIFIERS,
      platforms=['any'],
      install_requires=['six'])
