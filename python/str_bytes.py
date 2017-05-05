#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: str_bytes.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/04 13:53:28
"""

b = b'example'
print type(b)

s = 'example'
print type(s)


n = str(b)
print type(n)

m = bytes(s)
print type(m)


x = str.encode(s)
print type(x)






