#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: yield_no.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/03 17:01:41
"""



def getvals(i):
    if i:
        yield 1


a = getvals(0)
a = list(a)
print type(a)
for q in a:
    print q


b = getvals(1)
b = list(b)
print type(b)
for q in b:
    print q




#<type 'generator'>
#<type 'generator'>
#1


<type 'list'>
<type 'list'>
1
