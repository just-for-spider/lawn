#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: type_transfer.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/23 11:21:08
"""

aa = int('123')
print aa

bb = int(123.44)
print bb

bb = int(-123.44)
print bb

# err
#bb = int('123.44')
#print bb

# err
#cc = int('-123.44')
#print cc

# err
#dd = int('34a')
#print dd
#


aa = float('124')
print aa

bb = float('123.45')
print bb

cc = float(-123.44)
print cc

dd = float('-123.44')
print dd

ee = float('23.4v')
print ee
