#!/usr/bin/python3
import pathlib
import sys
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent
VERSION = '0.1'
PACKAGE_NAME = 'botsniffer'
AUTHOR = 'Oscar Valenzuela B.'
AUTHOR_EMAIL = 'alkamod@gmail.com'
URL = 'https://github.com/oscarvalenzuelab/botsniffer'
LICENSE = 'Apache-2.0'
DESCRIPTION = 'Detects AI generated code using ML'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=[
        'botsniffer',
        'botsniffer.data',
        'botsniffer.feature_extraction',
        'botsniffer.ml_model'],
    entry_points={"console_scripts": ["botsniffer=botsniffer.scanner:main"]},
    install_requires=["sklearn", "numpy", "pandas", "radon"],
    url=URL,
    package_data={
        "botsniffer.data": ["*.txt", "*.ini", "*.pkl"],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License'
    ],
)
