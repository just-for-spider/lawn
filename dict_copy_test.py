#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dict_copy_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/31 14:23:53
"""

dic = {'historyResultList': [{'name': u'月固定费', 'value': '126'}, {'name': u'增值业务费', 'value': '5.4'}], 'a': 100}

print dic['a']
t = dic['historyResultList']

del dic

print t

print dic['a']

