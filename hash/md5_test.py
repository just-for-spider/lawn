#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: md5_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/17 15:49:17
"""

import hashlib


author = 'wqj'
input = """aaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccccccccddddddddddddddd"""

md5 = hashlib.md5(input)
print md5
print type(md5.hexdigest())

raise Exception('this is a Exception')
