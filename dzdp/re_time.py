#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: re_time.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/16 11:37:40
"""

import re
import datetime

input = """DEBUG:root:time: 03-06  更新于17-03-06 22:30
16-12-31
DEBUG:root:time: 05-03"""

year = str(datetime.datetime.now().year)





pat = re.compile("\d+-\d+(-\d+)?")

for line in input.split('\n'):
    line = line.strip()
    m = pat.search(line)
    if m:
        dt = m.group(0)
        num = dt.count('-')
        #print dt, num
        if num == 1:
            dt = year + '-' + dt
        elif num == 2:
            dt = '20' + dt
        print dt
    else:
        print 'err:', line


