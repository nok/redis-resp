#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
from unittest import TestCase
from resp.Parser import Parser


class ParserTest(TestCase):

    def setUp(self):
        super(ParserTest, self).setUp()
        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.data_dir = os.path.join(current_dir, 'data')

    def test_invalid_file_path(self):
        file_ = os.path.join(self.data_dir, 'noname.txt')
        self.assertRaises(AttributeError, Parser,
                          file_path=file_, redis_cmd='SET {0} {1}')

    def test_invalid_command(self):
        file_ = os.path.join(self.data_dir, 'dump_comma.txt')
        self.assertRaises(AttributeError, Parser,
                          file_path=file_, redis_cmd='')

    def test_output_with_comma_del(self):
        file_ = os.path.join(self.data_dir, 'dump_comma.txt')
        redis_cmd = 'SET {0} {1}'
        code = "from resp.Parser import Parser;" \
               "Parser(file_path='{}', redis_cmd='{}')".format(file_, redis_cmd)
        proc = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        self.assertEqual(out, '*3\r\n$3\r\nSET\r\n$1\r\n1\r\n$1\r\na\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n2\r\n$1\r\nb\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n3\r\n$1\r\nc\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n4\r\n$1\r\nd\r\n')

    def test_output_with_whitespace(self):
        file_ = os.path.join(self.data_dir, 'dump_with_whitespace.txt')
        redis_cmd = 'SET {0} {1}'
        code = "from resp.Parser import Parser;" \
               "Parser(file_path='{}', redis_cmd='{}')".format(file_, redis_cmd)
        proc = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        self.assertEqual(out, '*3\r\n$3\r\nSET\r\n$1\r\n1\r\n$1\r\na\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n2\r\n$1\r\nb\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n3\r\n$1\r\nc\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n4\r\n$1\r\nd\r\n')

    def test_output_with_semicolon_del(self):
        file_ = os.path.join(self.data_dir, 'dump_semicolon.txt')
        redis_cmd = 'SET {0} {1}'
        code = "from resp.Parser import Parser;" \
               "Parser(file_path='{}', redis_cmd='{}', delimeter=';')".format(
            file_, redis_cmd)
        proc = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        self.assertEqual(out, '*3\r\n$3\r\nSET\r\n$1\r\n1\r\n$1\r\na\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n2\r\n$1\r\nb\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n3\r\n$1\r\nc\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n4\r\n$1\r\nd\r\n')

    def test_output_with_mult_cols(self):
        file_ = os.path.join(self.data_dir, 'dump_mult_cols.txt')
        redis_cmd = 'SET {0} {2}'
        code = "from resp.Parser import Parser;" \
               "Parser(file_path='{}', redis_cmd='{}')".format(file_, redis_cmd)
        proc = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        self.assertEqual(out, '*3\r\n$3\r\nSET\r\n$1\r\n1\r\n$1\r\na\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n2\r\n$1\r\nb\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n3\r\n$1\r\nc\r\n'
                              '*3\r\n$3\r\nSET\r\n$1\r\n4\r\n$1\r\nd\r\n')


