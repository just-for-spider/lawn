#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: obj_setattr.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/17 09:42:14
"""

#class A(object):
#
#    def __init__(self):
#        pass
#
#obj = A()

#obj = object()
#
#setattr(obj, 'tname', 't1')
#
#print obj.__dict__
#
#print obj.tname


class B(object):

    def __init__(self):
        print 'bbbb'
        pass


Q = B

a = Q()



bbbb
