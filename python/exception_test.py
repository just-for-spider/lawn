#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: exception_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/12 13:48:25
"""

dic = {'_rowkey': '100'}
print dic

dic['__rowkey'] = 1000

print dic

raise Exception('key err')

