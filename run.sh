#!/bin/bash
rm -rf dist/*
rm -rf build/
pycodestyle --exclude='*testfiles*' . | grep -v 'build' | grep -v 'dist' | grep -v 'W605' > pep8.log
python3 setup.py sdist bdist_wheel > install-pip.log
pip3 uninstall botsniffer  -y >> install-pip.log
pip3 install dist/botsniffer*.whl >> install-pip.log
botsniffer ./ --train
botsniffer ./botsniffer/scanner.py --identify