#!/usr/bin/env bash

conda config --add channels conda-forge
conda env create -n resp python=2 -f environment.yml
source activate resp