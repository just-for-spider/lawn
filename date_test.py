#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: date_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/22 10:28:42
"""
import datetime

opendate = '20160611115002'
"""2016-06-11 11:50:02"""

dt = datetime.datetime.strptime(opendate, '%Y%m%d%H%M%S')
str_dt = dt.strftime('%Y-%m-%d %H:%M:%S')
print dt, type(dt)
print str_dt, type(str_dt)

astr = '2017-03-01 至 2017-03-22'

newastr = astr.replace(' 至 ', ' ')
print astr, newastr

import re
str_list = ['4G全国套餐-136元套餐', '湖南融合套餐-沃潮16元套餐']
pat = re.compile('(\d+)元')
for e in str_list:
    m = pat.search(e)
    if m:

        print m.group(0), m.group(1)


def parse_package_fee(package_fee, pat=re.compile('(\d+)元')):
    m = pat.search(e)
    if m:
        print m.group(0), m.group(1)



for e in str_list:
    parse_package_fee(e)
