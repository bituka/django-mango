#!/usr/bin/env python

import mango

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = ['mango']
requires = [
    'Django==1.4',
    'django-social-auth',
    'South==0.7.5',
    'django-endless-pagination==1.1',
    'django_extensions==0.9',
    'django_discover_runner==0.2',
    'gunicorn==0.14.5'
]
tests_require = [
    'Django==1.4',
    'django_extensions==0.9',
    'django_discover_runner==0.2'
]

setup(
    name=mango.__title__,
    version=mango.__version__,
    description='More Mango, less Django!',
    long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
    author=mango.__author__,
    author_email='',
    url='https://github.com/pypug/django-mango',
    packages=packages,
    zip_safe=False,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    tests_require=tests_require,
    license=open("LICENSE").read(),
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    )
)
