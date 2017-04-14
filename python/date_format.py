#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: date_format.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/12 11:16:57
"""

import datetime

a = '2017年4月12日'

now = datetime.datetime.strptime(a, '%Y年%m月%d日')

b = now.strftime('%Y-%m-%d')


print b, type(b)



2017-04-12 <type 'str'>
