#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from Parser import Parser


def main(argv):

    # Arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--redis_cmd', type=str, default='')
    parser.add_argument('-i', '--input', type=str, default='')
    parser.add_argument('-d', '--delimiter', type=str, default=',')
    parser.add_argument('-p', '--pipe', action='store_true')
    args = parser.parse_args()

    # Parser:
    Parser(args.input, args.redis_cmd, args.delimiter, args.pipe)

if __name__ == "__main__":
    main(sys.argv[1:])
