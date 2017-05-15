#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: strip_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/08 16:17:09
"""

a = "{xxxxxxx}"

print a.strip('{}')

print a.replace('{', "{aaa")

