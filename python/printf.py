#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: printf.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/05 15:44:50
"""

dic = {1: 2}


line = '%s' % dic

print line



a = "//div[@class='%s']"

print type(a)

b = a % u'大牛'

print type(b)

