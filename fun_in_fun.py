#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: fun_in_fun.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/29 15:05:29
"""

def f1():
    def fun0():
        return 111
    def fun1():
        print 'f1.func1'
        print fun0()

    fun1()

f1()




