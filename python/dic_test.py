#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dic_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/13 15:33:14
"""




dic = {'colname': [{'f1': 10, 'f2': 10}, {'f1': 11, 'f2': 12},]}

print dic.keys()[0]

dic1 = {'colname': [{'f1': 13, 'f2': 13}, {'f1': 14, 'f2': 14},]}

dic['colname'].extend(dic1['colname'])


for k, v in dic.iteritems():
    print k, v

print dic
for k, v in dic.items():
    print k, v



