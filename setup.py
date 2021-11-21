#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [ 'aiofiles', 'python-multipart', 'fastapi' ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Konstantinos",
    author_email='Panayiotou',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Web API for smauto-dsl",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='smauto_server',
    name='smauto_server',
    packages=find_packages(include=['smauto_server', 'smauto_server.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/klpanagi/smauto-server',
    version='0.1.0',
    zip_safe=False,
)
