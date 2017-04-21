#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: sort_tuple.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/19 20:23:59
"""

t = []
t.append((1, 'wwww'))
t.append((2, 'wwww'))
t.append((0, 'wwww'))
t.append((4, 'wwww'))

t.sort(key=lambda x: x[0])

print t


