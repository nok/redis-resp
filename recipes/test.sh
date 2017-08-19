#!/usr/bin/env bash

source activate resp
python -m unittest discover -vp '*Test.py'
source deactivate
