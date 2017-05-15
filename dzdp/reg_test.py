#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: reg_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/10 13:12:12
"""

import re

pat = re.compile('^http(s)?://www.dianping.com/search/category/\d+/\d+(/)?(g\d+)?(r\d+)?(p\d+)?$')

url = 'https://www.dianping.com/search/category/2/10/g110r1489p6'
m = pat.match(url)
if m:
    print m.group(0)

