#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: monitor.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/03 15:05:52
"""

import re

pat = re.compile('([A-Z]+)_(.*?)_(\d+)_(\w+)')

line = 'YYS_LT_13115917160_73dafe202fa711e783bc964791d484c0'

m = pat.match(line)
if m:
    print m.group(1)
    print m.group(2)
    print m.group(3)
    print m.group(4)

