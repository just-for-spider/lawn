#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: func_param_none.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/10 16:36:16
"""

def fun(a, b=None, c):
    print b
    print a, c



fun(a=100, c=1000)



