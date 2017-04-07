#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: pageno_calc.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/30 09:37:54
"""

counts = 368
pagenos = counts / 100 if counts % 100 == 0 else counts / 100 + 1

print pagenos

