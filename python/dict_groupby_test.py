#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dict_groupby_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/27 10:14:26
"""

from itertools import groupby


m = [1, 1, 2, 2, 2, 5, 5, 10, 10, 10, 10, 10]

d = {k: sum(1 for _ in g) for k, g in groupby(m)}

print d

