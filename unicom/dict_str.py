#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dict_str.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/06 16:02:04
"""

import re

astr = """{u'respDesc': u'\u65e0\u8be6\u5355\u8bb0\u5f55\u30102114030170\u3011', u'respCode': u'2114030170'}"""

print astr.decode('unicode-escape')
