#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: yield_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/13 15:17:27
"""

def fun(a):

    if a:
        yield (100, 100)
    else:
        yield 100

    yield 10, 100, 1000


for m, n, q in fun(1):
    print m



Traceback (most recent call last):
  File "yield_test.py", line 25, in <module>
    for m, n, q in fun(1):
ValueError: need more than 2 values to unpack




