#!/usr/bin/env bash

# Requirements:
# pip install twine

# Environment:
name=resp
anaconda_env=resp

# Environment
source activate $anaconda_env
rm -rf ./build/*
rm -rf ./dist/*

# Version:
version=`python -c "from resp.Parser import Parser; print(Parser.__version__);"`

# Target (e.g.: pypitest, pypi):
target=https://test.pypi.org/legacy/
if [[ $# -eq 1 ]] ; then
    target=https://upload.pypi.org/legacy/
fi

# Package:
python ./setup.py sdist bdist_wheel
read -r -p "Upload $name@$version to '$target'? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
    twine upload ./dist/* --repository-url $target
fi