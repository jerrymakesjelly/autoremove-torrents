#-*- coding:UTF-8 -*-

from setuptools import setup, find_packages
from autoremovetorrents.version import __version__

setup(name = 'autoremove-torrents',
    version = __version__,
    description = 'Automatically remove torrents according to your strategies.',
    long_description = open('README.rst').read(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
    ], # Get classifiers from https://pypi.org/pypi?%3Aaction=list_classifiers
    keywords = 'python autoremove torrent',
    author = 'jerrymakesjelly',
    author_email = 'ganzhaoyu037@gmail.com',
    url = 'https://github.com/jerrymakesjelly/autoremove-torrents',
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = True,
    install_requires = [
        'requests',
        'pyyaml',
        'enum34'
    ],
    entry_points = {
        'console_scripts':[
            'autoremove-torrents = autoremovetorrents.main:main'
        ]
    }
)