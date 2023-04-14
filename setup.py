#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
    name="codebot-sniffer", version="0.1",
    description="codebot-sniffer - Detects AI generated source code using feature extraction with Machine Learning",
    author="Oscar Valenzuela",
    author_email="oscar.valenzuela.b@gmail.com",
    packages=['sniffer', 'sniffer.data'],
    entry_points={"console_scripts": ["sniffer=sniffer.scanner:main"]},
    install_requires=["ast-comments"],
    url='https://opensourcelicensecompliance.com',
    package_data={
        "sniffer.data": ["*.txt", "*.ini", "*.sig"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        ],
)
