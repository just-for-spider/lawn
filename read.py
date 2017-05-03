#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: read.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/03 14:40:40
"""


with open('foo.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print line.decode('gbk')
