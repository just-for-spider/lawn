#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: xjq.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/24 13:15:12
"""

import inspect


def fun():
    pass

print type(fun)


class Cla():

    def fun():
        pass

    @classmethod
    def fun1():
        pass

    @staticmethod
    def fun2():
        pass


i = Cla()
print Cla.fun.__class__

print i.fun.__class__

print type(i.fun1)

print type(Cla.fun2)

print type(i.fun2)


#<type 'function'>
#<type 'instancemethod'>
#<type 'instancemethod'>
#<type 'instancemethod'>
#<type 'function'>
#<type 'function'>
