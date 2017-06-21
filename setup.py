import os

from setuptools import setup

if os.environ.get('READTHEDOCS') == 'True':
	from distutils.core import setup

setup(
	name='ModernGL.ext.obj',
	version='0.2.0',
	description='ModernGL extension for loading obj files',
	url='https://github.com/cprogrammer1994/ModernGL.ext.obj',
	author='Szabolcs Dombi',
	author_email='cprogrammer1994@gmail.com',
	license='MIT',
	install_requires=['ModernGL'],
	packages=['ModernGL.ext.obj'],
	platforms=['any']
)
