#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dic_tuidao.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/22 16:07:14
"""


dic = {'name': 'wqj', 'age': 100, 'sex': 'mail'}

dic_1 = {'_' + key: val for (key, val) in dic.items()}

print dic_1

