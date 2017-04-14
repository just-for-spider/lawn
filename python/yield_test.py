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



for i in fun(0):
    print i

for i in fun(1):
    print i


