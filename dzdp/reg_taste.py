#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: reg_taste.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/16 10:46:15
"""

import re

pat = re.compile("口味(\d+)\(.*?\)环境(\d+)\(.*?\)服务(\d+)\(.*?\)")

input = "EBUG:root:comment-rst: |口味3(很好)环境3(很好)服务3(很好)"

m = pat.search(input)
if m:
    print m.group(1)
    print m.group(2)
    print m.group(3)

