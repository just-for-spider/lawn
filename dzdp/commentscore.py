#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: commentscore.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/05 14:55:38
"""

input = '|口味：8.5|环境：8.2|服务：7.9'

import re


pat = re.compile('\|口味：([0-9\.]*)\|环境：([0-9\.]*)\|服务：([0-9\.]*)')

m = pat.search(input)
if m:
    print m.group(0)
    print m.group(1)
    print m.group(2)
    print m.group(3)

