#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: param_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/01 15:09:53
"""


def fly(*args, **kwargs):
    dic = kwargs.pop('b')
    print kwargs
    print dic

    for e in args:
        print e



dic = {'a': '100', 'b': 120}

dic['b'] = {'c': 100, 'd': '0-1'}

#fly(**dic)
b = {'c': 100, 'd': '0-1'}

fly(300, 400, a='100', b=b)


{'a': '100'}
{'c': 100, 'd': '0-1'}



{'a': '100'}
{'c': 100, 'd': '0-1'}
300
400



b = {'c': 100, 'd': '0-1'}

print b.get('e')
