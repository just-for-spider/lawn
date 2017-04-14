#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: tuple_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/11 09:56:16
"""

dic = {'a': (1, 2)}

m, n = dic.get('b', (0, 0))

print m, n




0 0
