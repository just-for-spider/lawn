#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: class_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/27 15:22:24
"""

class A(object):

    num = 100

    def __init__(self):
        print __name__
        print self.__class__.__name__
        print self.__class__

        print 'num', A.num
        print 'num', self.num



a = A()

print __name__


