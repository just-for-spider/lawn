#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: delta2senconds.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/29 16:08:39
"""

import re


def calc(input, pat=re.compile('\d+')):
    arr = pat.findall(input)
    arr.reverse()
    total = 0
    for i in range(len(arr)):
        n = int(arr[i])
        total += n * (60 ** i)

    print total






input = u'4分44秒'
input = u'10时4分44秒'
calc(input)

print 10 * 3600 + 4 * 60 + 44

