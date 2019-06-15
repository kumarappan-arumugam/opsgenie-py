#!/usr/bin/env python

import codecs

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

def get_requirements(req_file='requirements.txt'):
    with open(req_file) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]

with codecs.open("README.md", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name='opsgenie',
    version='0.0.1',
    author='Kumarappan Arumugam',
    author_email='kumarappan.ar@gmail.com',
    description='A Python SDK for OpsGenie Web/REST API',
    long_description=long_description,
    url='https://github.com/kumarappan-arumugam/opsgenie-py',
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development'
    ],
    keywords=['OpsGenie', 'Web Api', 'Rest Api', 'Alert Api']
)
