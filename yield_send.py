#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: yield_send.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/05 16:55:31
"""


def g():
    print 1
    x = yield 'hello'
    print '2', 'x=', x
    print x, x, x
    y = 5 + (yield x)
    yield y


f = g()
print '----------'
print f.next()
print '----------'
print f.send(5)
print '----------'
#print f.next()
print f.send(100)
print '----------'



