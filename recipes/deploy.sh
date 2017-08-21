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
target=pypitest
if [[ $# -eq 1 ]] ; then
    target=$1
fi

# Package:
python ./setup.py sdist bdist_wheel
twine register ./dist/$name-$version.tar.gz -r $target
twine register ./dist/$name-$version-py2-none-any.whl -r $target

read -r -p "Upload $name@$version to '$target'? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
    twine upload ./dist/* -r $target
fi