#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: class_setattr.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/14 19:56:57
"""

class A(object):

    pass




a = A()

setattr(a, 'age', 18)


print a.age

