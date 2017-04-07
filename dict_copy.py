#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dict_copy.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/06 11:34:48
"""


dic = {'name': 'ppl', 'age': 110}

dic_b = dic.copy()


print id(dic), dic
print id(dic_b), dic_b

