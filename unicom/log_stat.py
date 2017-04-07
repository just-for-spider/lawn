#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: log_stat.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/30 13:48:49
"""

import sys
import re


dt = sys.argv[1]

pat = re.compile('(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*?date:(\d{4}-\d{2}-\d{2}) page:(\d+)')
t = []
for line in sys.stdin:
    line = line.strip()
    m = pat.search(line)
    if m:
        if m.group(1) >= dt:
            t.append((m.group(2), m.group(3), m.group(1)))

t.sort(key=lambda e:(e[0], e[1]))

for e in t:
    print e
