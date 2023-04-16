#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
    name="botsniffer", version="0.1",
    description="botsniffer - Detects AI generated source code using feature extraction with Machine Learning",
    author="Oscar Valenzuela",
    author_email="oscar.valenzuela.b@gmail.com",
    packages=['botsniffer', 'botsniffer.data'],
    entry_points={"console_scripts": ["botsniffer=botsniffer.scanner:main"]},
    install_requires=["ast-comments"],
    url='https://opensourcelicensecompliance.com',
    package_data={
        "botsniffer.data": ["*.txt", "*.ini", "*.sig"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        ],
)
