#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: timeformat.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/18 09:31:37
"""

import datetime

now = datetime.date.today()
now = now - datetime.timedelta(days=1)

print type(now)
print dir(now)

now = now.strftime('%Y-%m-%d')

print now, type(now)
