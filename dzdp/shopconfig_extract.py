#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: shopconfig_extract.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/08 15:08:28
"""

import re


txt = """
userId: 0,
shopId: 5255504,
shopCityId: 2,
shopName: "肯德基", """

arr = re.split(',\s', txt)
print arr
