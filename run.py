#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Desc

'''

# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 10-20-2015
# Last Modified:

import os

def run_cmd(cmd):
    print cmd
    os.system(cmd)


cur_dir = os.path.dirname(os.path.realpath(__file__))

os.chdir(os.path.join(cur_dir, 'moe-dict/src'))
run_cmd('./dict-json-to-term-txt.py')
