#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: kk.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/08 20:03:16
"""

astr = "power:4,manaScore:0"

t = [e.split(':') for e in astr.split(',')]

for k, v in t:
    print k, v
