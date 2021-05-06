#!/bin/sh
cd ./dist
rm *.gz
rm *.whl
cd ..
python3 setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*
