#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: map_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/22 16:52:11
"""

def add100(x):
    return x + 100

hh = [11, 12, 13]
print map(add100, hh)


def abc(a, b, c):
    return a * 10000 + b * 100 + c

l1 = [11, 12, 13]
l2 = [44, 55, 66]
l3 = [77, 88, 99]
print map(abc, l1, l2, l3)

print 'row 2 col'

print map(None, hh)
print map(None, l1, l2, l3)


#[111, 112, 113]
#[114477, 125588, 136699]
#row 2 col
#[11, 12, 13]
#[( 44,o77), (12, 55, 88), (13, 66, 99)]
